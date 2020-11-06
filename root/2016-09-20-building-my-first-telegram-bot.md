---
layout: base
date: 2016-09-20
title: Building my first Telegram bot
tags:
  - programming
  - software
  - public

permalink: "/{{ page.date | date: '%Y/%m/%d' }}/{{page.fileSlug}}/"
---

I built my first Telegram bot, Charge Bot. The first commit was 3 days ago (18th
September) but I first started working on it on 27th August. Then I took a three-week
break and resumed working on it on 17th September.

You can check the bot out on Telegram [here.](https://telegram.me/charge_game_bot)
The Github repo is [here.](https://github.com/lieuzhenghong/charge-bot/)

This checked a couple of technical firsts for me:

1. First Telegram bot
2. First time I used Python to write anything substantial
3. First deploy on Heroku
4. First time using non-ASCII characters and working with UTF-8 encoding
5. First time using a linter (pylint)

There are also a couple of non-technical firsts:

1. First time building a multiplayer "game"
2. First time building anything my friends can use
3. First time building something for public consumption (apart from a blog)

It was also the first time I wrote anything for public consumption.

Overall, I am quite happy with this project. The scope was manageable and it did
not balloon (probably because it was a game and, being a game, the scope is rather
clearly defined; what also helped was the limitations of the Telegram medium).
At the same time, I was able to incorporate user feedback and suggestions.

## How it works

The Python code to write a Telegram bot is extremely trivial.
It is just a while loop that sends HTTP requests with a long timeout (long
polling). Upon receiving a response, it sends the next request.

There is another way which is push instead of pull (doesn't send requests: waits for
Telegram to send updates to you) but it is far more involved and wasn't suitable for a
first-time project.

Anyway, here's the code:

```python
def get_updates():
    while True:
        string = URL + 'getUpdates?offset={0}&timeout={1}'.format(
            read_offset(), 3600)
        req = requests.get(string)
        handle_updates(req)
```

That's it. But there was a gotcha: As my background is in Javascript where all responses
are asynchronous, the line `req = requests.get(string)` tripped me up. If you were to write
that in Javascript you would get `req == undefined` or something like that and thus
`handle_updates(req)` would throw an error.

For Python, the synchronous nature of the code means that the assignment operator will
actually stop the evaluation until it returns a proper result. That means no callback is
needed and the code becomes very simple.

## Snafus

### Modularisation

This was something that I had a lot of trouble with, despite Mark's best efforts to help me.

My code is divvied up as follows:

```
* index.py (should be main.py): is the main file, imports everything
* network.py: sends requests and handles responses
* lobby.py: code that allows players to create and join a game
* game.py: game code
* charge_keyboard.py: the inline keyboard needed for the game
```

I was unable to understand the idea of a function that called another function (also known
as... a callback function LOL). Here's what I had trouble with:

```python
# network.py
def setPushDataTo(func):
    global callback
    callback = func

def pushDataToDispatcher(data):
    global callback
    callback(data)

# index.py

import network

def init():
    """Initialises the app and sets up all callbacks"""
    network.setPushDataTo(dispatcher)

def dispatcher(data):
    ...
```

Basically, this pattern allows a function in one file to call a function in another file,
_without importing_. The reason why we cannot import is because we don't want a two-way
import (index imports network, not the other way round).

But we still need some way for the "child" to communicate with the "parent" and the way
to do it is by setting the callback function in the "child" to the parent's function.

I am not sure I am explaining it clearly...I'll come back in a few days to this post
and see.

### Deploying on Heroku

Heroku was a real pain to set up...the documentation was lacking and I spent two nights'
worth just trying to figure it out.

The gist of it is that you have to have a `requirements.txt` file, a `Procfile` and a
`runtime.txt` file.

The "Getting Started with Heroku" tutorial mentioned the first two but not the last one!!

Basically, `requirements.txt` is just a list of dependencies... that's quite straightforward
I still don't know what `runtime.txt` does but I had to put in the line `python-3.5.2` in
order for Heroku to deploy my app with Python 3. I needed Python 3 because of it's native
Unicode handling.

What I mean by that is: when Python2 receives a response as a string, it doesn't actually
use Unicode encoding. In order to get it as Unicode you have to put a `u'` in front of it.
Python 3 does this all by itself.

The Procfile is also not straightforward. Basically the Procfile tells Heroku what kind of
dyno your app is (web, worker, something else), what file to run with what program. So
like this:

`worker: python index.py --loglevel=info`

(Weirdly, typing python3 index.py throws some weird error and I don't know why and haven't
been able to Google)

## Bad code

This app was developed very haphazardly, and it shows. I used tons of global variables
because I'm very bad. Coming from a Javascript background I don't know how to use classes,
like, _at all_. So it's good that I'm learning Python.

I tried refactoring but it was truly a huge pain and I actually had to rollback to the
previous commit because I fucked everything up. 😭

## Learning points and future plans

I want to make as many bots as I can in the future, because Telegram is by far the most-used
app on my phone. It was extremely smart of the Telegram team to expose this API to developers--
this has allowed it to eclipse Whatsapp even further.

For my next app, I will definitely try and use the webhooks push method.

Heroku has a free dyno tier so I have **no idea** why I'm paying 8 dollars a month to DigitalOcean.
I think that I will move my automated transaction tracker over to Heroku as well.

I mentioned the bad code: for my next app I am going to try and write it **right** and I
know everyone says that but I mean it, I'm going to aim for 0 warnings on pylint!!!

Overall, this was a good learning experience, I had fun. Am pretty psyched to build my
next Telegram bot!
