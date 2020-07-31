---
layout: base
title: Building a deep learning pipeline + model with Keras and PlaidML
date: 2019-09-17
tags:
  - programming
  - deep learning
  - data science
  - internship
  - public
---

I built and iterated on a deep learning model that replicates the outputs of
an existing rule-based system while having 100x faster inference. As a
prerequisite to iterating on the model I also built a deep learning pipeline
that did:

- Data reading and cleaning
- Feature extraction and selection
- Data normalisation
- Model checkpointing and saving

I iterated over 6 major model configurations (training ~50 models overall) and
got the model RMSE to fall from 0.23 (simple RNN) to 0.128. This significantly
improves upon a baseline model (RMSE = 0.22) but there is still room for improvement.

The pipeline I built will speed up future iteration significantly. I will
continue the project with the Oxford Strategy Group (Digital), where I might
lead the team of consultants.

(Summer 2019 internship with Inzura)

---

## Motivation

Inzura AI has a proprietary algorithm called the "Driver Profiler", which is a
complex rule-based system that measures how drivers drive. It derives
quantities like acceleration and velocity from GPS data. It looks up driver
position in a road network database to check for speeding (this road network
database allowed me to do data analysis on average speeds in [another project I
did for
Inzura](/2019/09/12/big-data-analysis-on-a-distributed-raspi-cluster.html)).

From all this data it identifies speeding/braking/accelerating/turning events
and scores them. For instance a hard acceleration would be scored poorly.

Finally, it aggregates all the events to give a "trip score", which is how
safely the driver drove on the trip.

This rule-based system works well but has two limitations. First, the database
lookups take a lot of time (latency) and necessitate an always-online device.

Second, most of the code for the driver profiler is written in Python. Richard
Jelbert, the CEO and co-founder of Inzura, wanted to deploy a version of the
driver profiler on dashcams. However, dashcams are embedded systems that run
C/C++.

A deep learning model solves both of these problems in one fell swoop. Once
trained, it can run inference completely offline, and there are libraries that
compile Keras models to C++. Additionally, offline inference means _real-time
inference_: the model could provide real-time feedback to a driver on his
performance, which is something that was impossible before.

## Feature selection / extraction

There was a lot of data in every second of the trip, but I restricted myself to
values that could be calculated relatively quickly and did not require any
database lookups. That meant only things like velocity, acceleration, turn
radius, not road type or speed limit.

I eventually settled on four features:

1. Absolute velocity
2. Tangential acceleration
3. Radial acceleration
4. Angle

## Data cleaning

There were anomalies in the data: whitespace issues, null values, wrong values,
etc. I had to write code that fixed all of that, which was trivial but tedious. [^1]

[^1]: I watched [this Youtube talk](https://www.youtube.com/watch?v=MiiWzJE0fEA) on a probabilistic programming language that can _infer_ missing data using Bayesian techniques. This is definitely something I want to explore.

## Keras generator

I wrote a Python generator to read the training data into my Keras model.

A
[generator](https://stackoverflow.com/questions/1756096/understanding-generators-in-python)
is a "function which returns an object on which you can call next, such that
for every call it returns some value, until it raises a `StopIteration`
exception, signaling that all values have been generated. Such an object is
called an iterator."

The big benefit of a generator is that they deal with data one piece at a time,
and so we don't have to put the whole dataset into memory. With a small number
of trips this isn't a problem---50,000 trips may only take up ~2GB in
memory---but will be an issue in the future.

One hiccup: A generator must be infinite in order to work with Keras. That is,
when it reaches the end of the training data is must loop back again to the
start. This took some effort to code (I discovered this [very helpful
link](https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly#)
too late) but will be very helpful when we start training with millions of
trips.

[TODO] code here

## Normalisation

[TODO] code here

I wrote some simple code to calculate the mean and variance of each feature. I
fed the mean and variances into the Keras generator in order to normalise each
feature before it was used to train the model.

This was actually quite a slow process: it took about 30 minutes to run. (This
is to be expected as there are ~340 million numbers to add). This is a prime
candidate for parallelisation with the [Raspberry Pi 4 cluster
computer](2019/09/12/big-data-analysis-on-a-distributed-raspi-cluster.html).

## Model checkpointing

[Checkpointing my
model](https://machinelearningmastery.com/check-point-deep-learning-models-keras/)
helped to save my progress by constantly saving intermediate models. What you
do is you train on the training set and only save a model when the validation
loss is lower than the best validation loss so far. That means that one can
save the best-performing model without worrying about overfitting.

But of course this meant that my initial train/test split would not work. I had
to divide it into train/validation/test with a 40000/5000/5000 split.

Here's what checkpointing looks like:

```
Epoch 00033: val_loss improved from 0.14147 to 0.14128, saving model to cnn_6.7-33-0.1413.hdf5
Epoch 34/50
200/200 [==============================] - 465s 2s/step - loss: 0.1418 - val_loss: 0.1359

Epoch 00034: val_loss improved from 0.14128 to 0.13595, saving model to cnn_6.7-34-0.1359.hdf5
Epoch 35/50
200/200 [==============================] - 440s 2s/step - loss: 0.1391 - val_loss: 0.1395
```

## Iteration

I started off with 10,000 trips. Each trip has length anywhere between
180-10000+ seconds. I extracted the four features at every time step. Null
values were taken to be 0.

The ground truth is _six_ subscores that range from 0 to 1: my models try to
minimise the root-mean-squared-error (RMSE) between its predicted subscores and
the actual subscores.

### Mk I: Simple RNN

```python
model = Sequential()
model.add(SimpleRNN(128,input_shape=(None,4)))
model.add(Dense(6)) # Returns a 6x1 vector: predicting 6 different scores
model.compile(optimizer='adam',loss=root_mean_squared_error)
```

Train and test loss 0.23. I had to abandon the RNN because the training was too
slow. It took 40 minutes to train one epoch of 10,000 trips. This is because
each trip had a different length and so I couldn't increase the batch size. We
could have padded with 0s, but at the time I didn't want to, and decided to
move to CNNs instead.

I thought a CNN architecture might work here because I knew the rule-based
system was detecting "events".

### Mk II: CNN with linear activation

Train and test loss 0.22---not much difference from the RNN model, but by
introducing padding I was able to increase the batch size and thus reduce
training time by 10x, to 3-4 minutes per epoch.

```python
model = Sequential()
model.add(Conv1D(filters=30, kernel_size=5, strides=2, padding='same',
				 input_shape=(5000,4)))
model.add(MaxPooling1D(pool_size=2))
model.add(Conv1D(filters=30, kernel_size=5, strides=2, padding='same'))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(64))
model.add(Dense(6))
model.compile(optimizer='adam',loss=root_mean_squared_error)
```

### Mk III: CNN with RELU

Changing the convolutional layers to use RELU rather than linear activation
functions made a big difference (thanks Jon Chuang), reducing the loss from
0.23 to 0.20 --- just scraping a win against the naive prediction. (Mk III).
Furthermore, it seems like I would get more gains from training with more
epochs.

```python
model = Sequential()
model.add(Conv1D(filters=30, kernel_size=5, strides=2,
				 padding='same', activation='relu',
				 input_shape=(5000,4)))
model.add(MaxPooling1D(pool_size=3))
model.add(Conv1D(filters=30, kernel_size=5, strides=2,
				 padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=3))
model.add(Conv1D(filters=30, kernel_size=5, strides=2,
				 padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=3))
model.add(Conv1D(filters=30, kernel_size=5, strides=2,
				 padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=3))
model.add(Conv1D(filters=15, kernel_size=5, strides=2,
				 padding='same', activation='relu'))
model.add(Flatten())
model.add(Dense(64))
model.add(Dense(6))
model.compile(optimizer='adam',loss=root_mean_squared_error)
```

### Mk IV: CNN with many more filters and dropout

(Henceforth, I'll be omitting the code because all CNNs look the same, I was
just tweaking the parameter size and adding more layers)

I then moved in a different direction --- instead of going deeper (adding more
layers), I went wide (adding more filters). This was Mk. IV with 4 CNN layers
and 100/160 filters. Sadly, the model didn’t perform that well. But I learned
two things from this:

1. Training speed was not affected! In other words, adding more filters gives
   you more power “for free” --- at the cost of memory.
2. Wide filters do not overfit --- in other words, go hog wild with adding
   larger layers.

### Mk V: CNN with batch normalisation

Emboldened by this, I decided to build Mk. V: exactly like Mk III, but
increasing the size of the convolutional layers.

I trained 7 more models, trying a combination of different techniques:

- 5.1 add dropout layer --- training loss 0.2044, test loss 0.2050
- 5.2 change max pool layers to have size =2
- 5.3 change stride size = 1: training and test loss 0.20
- 5.4 append another Conv1D layer at the end with stride size = 2, training
  loss 0.2042, test loss also 0.204
- 5.5 remove pooling layers : almost bricks the computer, huge-ass dense layer
  (2.6 million parameters): training loss 0.1964, test loss 0.2146
- 5.6 add back the pooling layers: training loss 0.1977, test loss 0.200
- 5.7 add batch norm in between Conv1D layers.

I knew that all of these models were underfitting as they were not doing much
better than the benchmark. So I decided to use MORE layers.

### Mk VI: CNN with MORE layers

```python
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
conv1d_1 (Conv1D)            (None, 5000, 100)         2100
_________________________________________________________________
conv1d_2 (Conv1D)            (None, 5000, 100)         50100
_________________________________________________________________
max_pooling1d_1 (MaxPooling1 (None, 2500, 100)         0
_________________________________________________________________
conv1d_3 (Conv1D)            (None, 2500, 100)         50100
_________________________________________________________________
conv1d_4 (Conv1D)            (None, 2500, 100)         50100
_________________________________________________________________
max_pooling1d_2 (MaxPooling1 (None, 1250, 100)         0
_________________________________________________________________
conv1d_5 (Conv1D)            (None, 1250, 100)         50100
_________________________________________________________________
conv1d_6 (Conv1D)            (None, 1250, 100)         50100
_________________________________________________________________
max_pooling1d_3 (MaxPooling1 (None, 625, 100)          0
_________________________________________________________________
conv1d_7 (Conv1D)            (None, 625, 100)          50100
_________________________________________________________________
conv1d_8 (Conv1D)            (None, 625, 100)          50100
_________________________________________________________________
max_pooling1d_4 (MaxPooling1 (None, 312, 100)          0
_________________________________________________________________
conv1d_9 (Conv1D)            (None, 312, 100)          50100
_________________________________________________________________
conv1d_10 (Conv1D)           (None, 312, 100)          50100
_________________________________________________________________
max_pooling1d_5 (MaxPooling1 (None, 156, 100)          0
_________________________________________________________________
conv1d_11 (Conv1D)           (None, 156, 15)           7515
_________________________________________________________________
conv1d_12 (Conv1D)           (None, 78, 15)            1140
_________________________________________________________________
dropout_1 (Dropout)          (None, 78, 15)            0
_________________________________________________________________
flatten_1 (Flatten)          (None, 1170)              0
_________________________________________________________________
dense_1 (Dense)              (None, 64)                74944
_________________________________________________________________
dense_2 (Dense)              (None, 6)                 390
=================================================================
```

- Mk 6.1: I removed batch normalisation and added more layers for a total of 12
  convolution layers. This gave me the lowest test loss so far. **Train/test loss 0.1928/0.1857.**

The reason why the test loss is smaller than the training loss is because of
dropout. From [a StackOverflow post](https://stats.stackexchange.com/a/205831/229360):

> One possibility: If you are using dropout regularization layer in
> your network, it is reasonable that the validation error is smaller than
> training error. Because usually dropout is activated when training but
> deactivated when evaluating on the validation set. You get a more smooth
> (usually means better) function in the latter case.

- Mk 6.2: I trained for more epochs (40 rather than 20) and got a train/test
  loss of **0.1698/0.1820**. I realised that the model was beginning to overfit
  and so I got 40,000 more trips.

- Mk 6.3: I trained for 50 epochs on 50,000 trips. Training time per epoch took
  ~20 minutes, which meant the entire training took **15 hours**. I got a
  training loss of **0.163** and a test loss of **0.1599**. This is good news
  --- adding more data stopped the model from overfitting.

- Mk 6.4: forgot to write what I did

- Mk 6.5: Instead of batch normalisation, I normalised _all_ the inputs and
  trained the same model again. This really helped! The neural network was able
  to achieve the lowest-ever training and test loss. **Training loss: 0.1475.
  Test loss: 0.1280**

- Mk 6.6: removed dropout layer and trained for 25 epochs.

- Mk 6.7: Instead of stopping the training at a specific number of epochs, I
  decided to start checkpointing, and continuously train until the validation
  loss plateaued. In this way I could plot a [learning
  curve](https://stats.stackexchange.com/questions/51490/how-large-a-training-set-is-needed/51527#51527)
  and determine whether I needed more data or a more powerful model.

  Here I made [silly embarassing mistake #2](#pointing-the-validation-set-to-be-the-same-as-the-test-set). I fixed it but didn't have the time to rerun the training.

I stopped the deep learning project here to focus on the Raspberry Pi cluster project.

## Silly, embarassing mistakes I made

### Not taking advantage of multiprocessing

In the `predict_generator`
[function](https://keras.io/models/model/#predict_generator) there are
several arguments you can pass it to enable multi-CPU operation. One argument
was `multiprocessing=True` which I did set. But what I had neglected to
change was `workers`, which defaults to 1 if unspecified. Once I set
`workers=10` we got---predictably---a 10x speedup in training.

### Using the same data for both the validation and test set

A silly mistake I made with list slicing meant that my validation set was the
same as my test set. I saw the validation loss keep decreasing to 0.09 and
was incredibly pleased; I thought it was too good to be true. It was!

## My thoughts

Before I started this project I had a naive idea of deep learning. I was
implicitly assuming the following:

1. Nice clean-ish data
2. Nice environment to do deep learning already set up for you
3. Nice well-defined requirements and unambiguous loss metric

None of those assumptions held true in this project. In particular I had to
set up CUDA on my machine (to enable GPU acceleration) and that was really
difficult. Eventually I used PlaidML instead of Tensorflow for the backend
because it played nice with my GPU.

There's _so much glue code_ that goes into a "business" machine learning
model. The actual Keras machine learning code that specifies the model is only
a couple dozen lines, but I have hundreds of lines of code that clean the data,
normalise the data, choose the right subset of the data, read the data, save
the model, run predictions with that model, ... and so on.

Finally, there are many insidious bugs that can bite you silently in deep
learning projects. This is probably due to my relative inexperience---I hope
that by documenting the silly mistakes here, I'll not make them again.

## Things I've learned

This was the first non-toy deep learning project I have done. Because there
was no senior data scientist to guide me, I made many silly mistakes and
didn't follow best practices.

The most novel part for me was learning about, and writing, the architecture
that supports the deep learning model.

Input normalisation improves training significantly. I saw the training/test
loss fall from 0.16 to 0.13 just by normalising the input.

In the course of the project I went through some of the courses in Andrew
Ng's [Deep Learning
Specialisation](https://www.coursera.org/specializations/deep-learning). I
didn't find the specialisation very useful but it was good in giving me some
deep learning intuitions.

## Conclusion

Although I didn't get to finish the project, I still learned a lot. I had to
touch every single part of the deep learning pipeline---not just the model
code itself---which I really appreciated. A big thanks to Richard for
giving me this opportunity.
