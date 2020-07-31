---
layout: base
date: 2016-05-10
title: Meeting with Mrs Hauw, swimming with Xiao Hui and future plans
tags:
  - daily report
  - progress report
  - private
  - diary
---


The following paragraphs were written on 7th May:

> I woke up at 1030 today, having slept at 2am the previous night. I was late to
> the Ulu Pandan place, arriving at 1215. I met with Mrs Hauw and Dr Bimler.

> I got to meet Li Yicheng, Carol, Brenda, Mun Kit and I caught a glimpse of
> Delphine. 
> 
> Mrs Hauw explained that the 8--12 year olds were participating in a competition
> called Code Xtreme or something along those lines. It's a three-hour hackathon
> where kids are supposed to use Scratch to build something that fits the theme of
> FinTech. 
> 
> As expected, Mrs Hauw said that she was shorthanded and wanted me to help with
> the Scratch team until July. Well, July is fine. It will serve multiple
> purposes: one, it's a probation period for Mrs Hauw to see what I can do, and
> two, it's a chance for me to learn more about pedagogical techniques.
> 
> I hope to impress her with my consistency and willingness to work hard. Also,
> I've been trying to build a database app for Carol, who is trying to create a
> maths question repo for her kids. 

## Swimming with Xiao Hui

After the meetings I met up with Xiao Hui and we went swimming. She was wearing
a red sweater and I thought she looked cute in it. She is extremely
fast/I'm extremely slow (she swam 30 laps to my 26). Afterwards we went for
dinner at a prata place at J8 where she only ate two kosong prata. Then we went
to have green tea shaved ice but that's not really my thing. Then we went to
NTUC and just walked around lol.

## Carol's database app

I'm trying to build a database for Carol. The idea is to create a maths-question
repo, divvied up by topic. Questions are screenshots from PYPs and other
sources. The MVP DB has to contain the following features:

1. Users can upload images to the db through mobile and desktop client;
2. Users can tag the images with metadata (autocomplete features present);
3. Users can query questions by various criteria.

Progress on the database app has been extremely slow. This is because I'm having
to configure and learn many many frameworks just to get the basic stuff running.
Here's what I have had to use/config:

1. Node.js
2. Expressjs
3. Mongodb
4. Multer -- for file upload 
5. Pug (Jade) -- templating engine to serve up the images
6. Compass -- just to make CSS easier.

I'll also have to learn things like **promises** and **async-await**. Right now
I've been struggling with the app. There is a problem where ```res.render``` is 
being called before my manipulations are complete, which results in an empty
page. 

## Meeting with IDA

Thanks to Dr Balakrishnan, I've been able to get in touch with the iDA. Turns
out that a couple of them are already helping kids on their own time, be it
21C Girls, Mendaki, SINGA etc. I am taking off tomorrow to meet them at their office.
I'll try and find out what they've been up to and how I can work with
them. 


