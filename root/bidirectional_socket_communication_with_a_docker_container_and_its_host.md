---
title: "Bidirectional communication between a Docker container and its host"
layout: base
tags: ["public", "build"]
---

<div class = "toc">

[[toc]]

</div>

## Introduction

I wrote simple sockets code to allow a host machine and a Docker container
running on it to communicate bidirectionally.
I needed to do this because our machine learning model ran on a Docker container
and we needed to send data to/receive data from it.

## The problem

We want the machine learning model to be in a Dockerfile
to make setup and configuration easy.
But this introduces a new challenge:
how do we send data from the Jetson (host) to the machine learning model (Docker
container)?

If the code for the machine learning model were not in a Docker, we could simply
`import` the module into the webcam stream code, something like this:

```python
# webcam_stream.py
import ml_model
img = get_img_from_webcam_stream()
bounding_boxes = ml_model.detect_objects_in(img)
```

But we can't do this now because `ml_model` is running in a Docker container.
We need some way to pass the `img` from the webcam stream into the Docker
container, and get the `bounding_boxes` back.
So how? I thought a lot about this. There were a few different candidates:

1. Spin up HTTP server on the Docker container and make requests
2. Use a message broker like Kafka or RabbitMQ
3. Mount a host directory on the docker and read/write to files on that directory
4. Expose a port and build bidirectional communication over TCP

It seemed like a very simple task to send data to and from the same machine, so
I wanted to avoid the overhead of spinning up a HTTP server or message broker.
This left the last two options.

### Writing to and from files in a directory

Suppose you have a `webcam_stream.py` and `ml_model.py`
that both have access to a shared folder. 
If both Python files watch the folder for changes we can get kind-of real-time
communication.
Let `webcam_stream.py` write `frame_1.ndarray` to the folder.
Then `ml_model.py` can read that file in, detect the objects in that first
frame,
and then write a `frame_1_bbox.ndarray` file to the folder.
`webcam_stream.py` can then read *that* file in.

This is a pretty simple idea: the downsides are that 
i) file I/O is slow, and 
ii) you will have to write code to handle deleting old files.
It also didn't seem very elegant to have to constantly create and delete files.
Therefore, I chose not to use this approach in the end.
But since everything in Unix is a file, couldn't we use Unix sockets?

### Building bidirectional communication over TCP

Suppose we had an open port on `localhost:6000` 
and a way to send and receive data over that connection.
Then we could make `ml_model.py` constantly listen on that port
for image data from `webcam_stream.py`.
After receiving the image data it would then run it through the ML model
and send the bounding boxes back through the same connection.

Some pseudocode here:

```python
# webcam_stream.py
while True:
    img = get_img_from_webcam_stream()
    bounding_boxes = send_img_to_ml_model(img, port=6000)
```

```python
# ml_model.py
while True:
    img = recv_img_from_stream(port=6000)
    bounding_boxes = detect_objects_in(img)
    send_img_to_stream(bounding_boxes, port=6000)
```

## How to build bidirectional communication over TCP

I used a low-level Python library called `socket`

We first establish a connection using `socket.connect`
before sending any data over.

First we start a listener on the server side.
We *bind* the socket to an open port (in this case 6000)
and start listening for connections forever in a `while` loop,
calling `socket.accept` to accept incoming connections on that socket [^0].

[^0]: https://beej.us/guide/bgnet/html/ 

> Get ready—the accept() call is kinda weird! What’s going to happen is this:
someone far far away will try to connect() to your machine on a port that you
are listen()ing on. Their connection will be queued up waiting to be accept()ed.
You call accept() and you tell it to get the pending connection. It’ll return to
you a brand new socket file descriptor to use for this single connection! That’s
right, suddenly you have two socket file descriptors for the price of one! The
original one is still listening for more new connections, and the newly created
one is finally ready to send() and recv(). We’re there!

The client side is simple: 
we just use `socket.connect` to connect to the remote socket. 

Here's what that looks like on the server side:

```python
# ml_model.py
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('localhost', 6000)
    sock.bind(server_address)
    sock.listen(1)

    try:
        while True:
            print('waiting for a connection')
            connection, client_address = sock.accept()
            ...
```

And on the client-side:

```python
# webcam_stream.py
server_address = ('localhost', 6000)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(server_address)
    ...
```

Once a connection has been accepted we can start the bidirectional sending.
Sadly it's not as simple as sending the image and receiving the bounding boxes.
There are two main complications: 
*serialisation* and *deserialisation* of the data, and
knowing when the message has ended.

### Serialising and deserialising the data

We use `np.save` and `np.load` to serialise and deserialise 
the numpy arrays to and from a `BytesIO` object.

### Knowing when the message has ended

TCP connections are open-ended, which means that the receiving server
doesn't know when to stop receiving.

[This Python sockets guide](https://docs.python.org/3/howto/sockets.html)
puts it nicely:

> ...you need to realize that there is no EOT on a socket...
> If the connection has not been broken, you may wait on a recv forever, because
> the socket will not tell you that there’s nothing more to read (for now). Now
> if you think about that a bit, you’ll come to realize a fundamental truth of
> sockets: messages must either be fixed length (yuck), or be delimited (shrug),
> or indicate how long they are (much better), or end by shutting down the
> connection.

The simplest way to solve this problem is to simply close the connection after
we've
sent out the image. 
But we don't want to close the connection because 
we want to get a response back from the server (namely, the bounding boxes).
So we'll have to specify the message length instead. [^1]
We'll simply prepend the message with the message length.
The problem is that the message length itself can also vary, 
so we'll need to pad it to ensure the first `N` bytes will be guaranteed to be the header.
If you don't pad the message length then you might read part of the array in 
as your message length. 

[^1]: HTTP specifies message length using a "Content Length" or "Transfer Encoding" header field: see 
[this SO link](https://stackoverflow.com/questions/4824451/detect-end-of-http-request-body#4824738)
for details.

First we save the `numpy` array into a `BytesIO` object using `np.save`.
We can get the message length using `message.getbuffer().nbytes`, 
and can pad the message length string using Python's string formatting.

```python
# webcam_stream.py
msg_len = message.getbuffer().nbytes
HEADER_SIZE = 10
b_msg_len = bytes(f"{msg_len:<{HEADER_SIZE}}", 'utf-8')
```

The `:<{HEADER_SIZE}` thing right-pads the formatted string with zeros
so that it is exactly 10 characters long.
Here's an example of what that looks like:

```python
>>> f"{12345}"
'12345'
>>> f"{12345:<10}"
'12345     '
>>> bytes(f"{12345:<10}", 'utf-8')
b'12345     '
>>> bytes(f"{12345:<10}", 'utf-8').decode('utf-8')
'12345     '
# on the server side
>>> int(bytes(f"{12345:<10}", 'utf-8').decode('utf-8'))
12345
```

On the Docker container we first receive the message length and decode it.
**(Note that since we are using UTF-8 encoding, a numeric string of length 10
will be 10 bytes long!)**
We then keep receiving until the number of bytes we've received
equals the message length. 
We then send it to the object detection model and send the bounding boxes back.

```python
# ml_model.py
HEADER_SIZE = 10

# First receive the header to know how long the message is:
b_msg_len = connection.recv(HEADER_SIZE)
msg_len = int(b_msg_len.decode("utf-8"))

# Then receive the data in small chunks until we receive msg_len bytes
full_data = BytesIO()
while (full_data.getbuffer().nbytes < msg_len):
    data = connection.recv(4096)
    full_data.write(data)
full_data.seek(0)
print("All data received!")

# Now loading and using the object detection model
img = np.load(full_data, allow_pickle=True)
bboxes = detect(img, 0.3, 0.4)[0]

print("Sending data back to the client")
bbox_bytes = BytesIO()
np.save(bbox_bytes, bboxes)
bbox_bytes.seek(0)
connection.sendall(bbox_bytes.read())
```

This solution has its limitations: it won't work if 
we wanted to send multiple images in a single connection. 
If we sent multiple messages then there would be no guarantee 
that the first 10 (or whatever) bytes of the message buffer 
would be the message length. 
But since we close the socket and re-open a new one after each frame,
this is not a problem.
