---
date: 2016-04-23
title: "daily report: my first post"
layout: base
tags:
  - daily report
  - progress report
  - private
  - diary
permalink: "/{{ page.date | date: '%Y/%m/%d' }}/{{page.fileSlug}}/"
---

<link rel = 'stylesheet' type='text/css' href='/stylesheets/syntax.css'/>

## daily report for 2016-04-23

Today I woke up at 1030 extremely tired. I slept at about 2am last night, having
Mission-Impossible-d home (did not bring keys--went to the window and grabbed
the window keys, then went to my room's window and climbed in that way)

I woke up at 1030 and started to use the computer all the way until 1530. (which
is the time of this writing). Here's what I did:

1. Learn how to regex (I learned it so I could do a regex to check for .html
   files in the request.url of node.js server).
2. Learned a little bit about the web OSI: wires -> IP --> TCP --> HTTP

I'm trying to get my node.js server a little bit more functional. Mark suggested
that I extend it such that it handles nonstandard GET requests, that is:

```javascript
localhost/add?a=5&b=10
```

```ruby
def show
    @widget = Widget(params[:id])
    end
end
```

The full quote was the following:

> Mark Theng, [23.04.16 14:53]
> uhh, create an api?

> Mark Theng, [23.04.16 14:53]
> if you can get something like localhost/add?a=5&b=10 to work

> Mark Theng, [23.04.16 14:54]
> then you can do your ajax client

> Mark Theng, [23.04.16 14:54]
> then, if you're feeling ambitious, you can install socket.io

**Update 2016-04-23 17:20**

Just managed to get localhost/add?a=5&b=10 to work!

```javascript
else if (url.parse(request.url, true).pathname  === '/add') {
    let str = url.parse(request.url,true).query;
    let acc = 0;
    for (var item in str){
        acc += parseInt(str[item]);
    }
    response.writeHead(200, {'Content-Type': 'text/html'});
    response.write('<p> The answer is: ' + acc);
    response.end();
 }
```

**Update 2016-04-23 18:25**

Wow so shag. Took me the better part of an hour to figure out how to do syntax
highlighting in Jekyll. I thought that it was automatic but turns out only
Rouge, the engine, is automated--you still have to download the css file, of
course. Stupid mistake to make, but I'm stupid.
