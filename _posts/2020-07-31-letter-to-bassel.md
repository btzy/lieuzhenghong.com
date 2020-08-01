---
title: "Letter to Bassel in August 2020, after my Finals results"
date: 2020-08-01
layout: base
tags:
  - private
  - diary
permalink: "/{{ page.date | date: '%Y/%m/%d' }}/{{page.fileSlug}}/"
---

Dear Bassel,

Have been putting this email off for so long---
not because I didn't want to send you an email, but simply because
whenever I got down to writing it, there was always a new and exciting thing
happening over the horizon,
and I would decide to delay the email to incorporate that new thing.
Now that things have settled down somewhat, here is the email that
I should have sent a month ago!

## Table of contents

[[toc]]

## On exam results

Celine got a First as well! It was a pretty funny experience.
We were in the garden inside the Schwartzwald when the email came in,
and so we didn't realise that our results were available until
we checked our phone an hour after that and were inundated with friends
asking us for our results.
We briefly considered going on our planned hike before checking the results,
but I rightly pointed out that neither of us would enjoy the hike if we didn't
get to check our results first.

And so we went up to the attic and started checking our results.
It was satellite internet and it loaded so incredibly slowly
(even slower since we were both very anxious).
Mine loaded first and I saw the First Class and I was ecstatic!
And then Celine's one loaded as well and we just exploded, we were so
incredibly happy.

Anyway, Celine and I are both very pleased.
I am incredibly, incredibly pleased, of course---
I did actually expect a First, but being ranked 5th in the level is far higher than
what I expected or deserved.

We wanted to call you but you never replied to our WhatsApp message :(
Celine is coming back tomorrow (2nd August) --- should we call then or the day after?

## What we've been up to

I thought that this summer would be a chill one but it turns out that
interesting projects just keep popping up at me, and now I have a huge backlog
of things that I need to do. This summer is actually (much) busier than my
exam revision period, which isn't great, because this was supposed to be a relaxing
summer spent with Celine.
(It helps a lot that I'm doing self-directed stuff that I like, though).

### Game theory post is up

I wrote a post about the modified Blotto game I told you about
[here](https://lieuzhenghong.com/explorations/pap_exploration/pap-smc-grc.html).

It got a lukewarm reception from the eminent scholars of Reddit.com.
But one guy who is a CS PhD student said that he'd think about the algo
complexity of solving the modified Blotto game. Haven't heard anything from him since though.

### Travelling: Ben's place, Celine's parents', and the Schwartzwald

We left Oxford to go to Brussels to visit Ben,
the old alumnus of Merton who studied Compsci and Philo way back in 83 or something.
His daughter goes to New now, studying chemistry.

We really enjoyed ourselves there: I had snail for the first time in my life,
and it was actually pretty good. I've never seen a more middle-class Englishman
in my life before though: Ben is like fourth or fifth generation Oxford,
top civil servant in the EC, lovely big house in the middle of Brussels,
a bit ditzy but very smart... He was such a gracious host and we
enjoyed ourselves very much.

Here's a picture of us with Ben and his family when we cooked lunch for them:

![Ben and his family](/img/summer_2020/ben_and_fam.jpg)

Then afterwards we went to Celine's parents', and there was basically a basement
for us to live together. (I'm in it now).

We went on a nine-day trip to the _Schwartzwald_ (Black Forest), which was
amazing. The AirBnB we lived in was a house in a village of twenty-eight people,
high up in the mountains (~900m above sea level),
and the views were breathtaking. The air was so clean and fresh,
everyone drinks the water that comes right out of a natural spring
(they literally pipe the water from the spring into the houses with no cleaning
required --- this _blew my mind_), the animals were very cute, and there
was absolutely no light pollution so on a clear night one can see hundreds or
thousands of stars.

Everyone in the village is either a rancher or a pensioner, except our hosts,
Patricia and Dieter.
(Patricia is a tour guide + dive instructor: Dieter is a social worker).
The people were so friendly, and our hosts exceptionally so.
They grow a lot of trees and plants around their property, and I
got to try i) a lot of different fruits I'd never tried before
(redcurrants and _mirabelles_), and a lot of different fruits that I've never
seen in the wild e.g. cherry tree.

We also saw tons and tons of wild raspberries and strawberries around.
We went on a hike and started taking all that we could find and filled
an entire box, but we couldn't even make a dent in the number.
It's crazy how much shit just grows wild. The strawberries were AMAZING.
They were very small, but they were so incredibly sweet. In fact they taste
almost artificial, like strawberry-flavoured candy.
(But of course they are 100% natural).

I'll get Celine to give me the pictures and I'll send you some pictures very soon!

### Rejected Harvard offer, and will most likely be starting work in Singapore in September 1

I applied to defer from Harvard for a year but they didn't allow me to, so I'm
planning to reject the offer and reapply next year.
(Will have to bug you for references again, unfortunately!)

And so I started talking to IMDA and asking them if they wanted to accept me
for a year first. So I will be working for IMDA for a year,
applying in December 2020, and deciding to matriculate in August 2021.

### Other projects I have been working on

#### MGGG GSoC

I've been trying to develop and deploy an upstream feature on their flagship
web app called Districtr. I am implementing contiguity and cut edge functionality.
When the user draws a districting plan, the server will return whether or not
that districting plan is contiguous, how many cut edges there are, and where
the number of cut edges falls in the distribution of some subset of plans in the
space of possible plans (generated with MCMC).

The main problem is that the codebase is pretty large and difficult to
wrap my head around. I don't know where everything is and I don't know what will
break when I touch this or that, so progress has been slow.

#### Unsupervised trip clustering with Inzura again

My ex-boss Richard, the CEO of the auto insurance startup I was working at
last summer, reached out to me again. He wanted me to do some
unsupervised trip clustering. I know that TESL has a section about clustering,
but I haven't read it yet --- do you have any advice?

Basically we have some trips, which you can think of as a tuple of GPS points

$$ [(x_1, y_1), (x_2, y_2), ... (x_t, y_t)] $$

where $t$ is the length of the trip (varies from trip to trip), and $(x_t, y_t)$
is the lat/long of the device at that second.
From these raw GPS points we calculate
_derived quantities_ such as turning, acceleration, braking, velocity, and so on.
So we now have a tuple of derived quantities:

$$ [(a_1, b_1, c_1, ... ), (a_2, b_2, c_2, ...), .... (a_t, .... y_t)] $$

The task is as follows. Given many of these tuples of derived quantities,
can we start to cluster them? For instance, trips that have low velocity
(e.g. the person is walking and not driving a car) might form a cluster,
and trips that have very high velocity (person on a high speed train/plane)
might form a cluster. Or there might be other clusters like driving on a
country road v. on a highway, in a traffic jam v. in smooth traffic, and so on.

One issue I thought of is that these are possibly very high dimensional points,
and additionally, each tuple (representing a trip) is of different length.
AFAIK, Regular k-means clustering only deals with points---but these are tuples, not points.
I could just take the mean to give an aggregrate score (so one $1xN$ point per trip)
but that would lose a lot of information.

#### Revamping my personal website

My personal website was a bit long in the tooth, and I didn't understand the
previous static site generator (Jekyll, written in Ruby) well enough.
I also took the time to redesign some of the ugly-looking pages

#### Board game engine

This was going rather swimmingly for quite a while, but getting real-time
multiplayer working is quite difficult. I will continue working on
this side project when the other projects have concluded.

#### Path tracer with Ross

Haven't started on this yet because of all the stuff I've been doing,
but I hope to do this soon. Ross is very much smarter than me so I
need to make use of this opportunity.

#### Learn systems design/React/Express for technical take-home interview

I was recently approached by a Hong Kong startup (it was basically one of those
GitHub scrape + email blasts) asking if I would be willing
to take on a full-time job in Hong Kong. Obviously I am not willing, because
I much prefer clearing some of my bond first. But the take home assignment was
quite interesting, and Sebastian (this guy who did BPhil Philo at Merton last year)
said that it would be "really good practice" as it is the kind of thing I'd be doing
as a software engineer.

The problem is that I haven't touched many of the technologies in several years,
and some I haven't learned at all. And the deadline is Thursday -- so I'll
be pretty busy these couple of days learning all of this stuff from scratch!
Should be fun.

#### Self-studying A8, A9, A12, and the Introduction to Statistical Learning

Haven't started on this yet either. I was planning to do it before I started
Harvard, but other projects seem to have crowded it out. Hopefully I can get
some synergy between the clustering project and this one.

## On the calligraphy I wrote for you

The little thing I wrote for you is an excerpt from a Classical Chinese poem.
This Tang Dynasty poem tells the story of the poet and his close friend,
two scholar-officials posted far from their homes.
His close friend has received a new, prestigious official posting
hundreds of miles away: they may never see each other again.
Despite being written almost fourteen hundred years ago,
the poem reflects aptly my feelings.

I have translated it as best I can with reference to several online translations,
but I am of course no poet:

```
《送杜少府之任蜀洲》

城闕輔三秦，風煙望五津。
與君離別意，同是宦游人。
海內存知己，天涯若比鄰。
無為在歧路，兒女共沾巾。
```

```
<<Sending Off Vice Prefect Du on His Way to His Post in Suzhou>>

O'er the spires and walls of the Three Qins, our land,
There in wind and white mist, the Five Rivers descend.
We must say our farewells, leave each other behind
For the faraway posts that our liege lord's assigned.

Though the vast seas bind us, we remain bosom friends;
We are neighbours in heart, though apart at sky's ends.
Though our paths must now part, and I hold you most dear,
Lest like children we weep, let us hold back our tears!
```

The line I wrote for you translates to

"Though the vast seas bind us, we remain bosom friends;
We are neighbours in heart, though apart at sky's ends".

And I thought that was apt: as long as we have interests in common,
geographic distance cannot faze us.
(It's probably even more apt nowadays---remember when we were just
across the street but had to Zoom?)

## Conclusion

I am very sad to bid farewell to you, a beloved teacher, mentor, and friend.
Hopefully we will get to see each other again soon in person,
or collaborate on something exciting together.

Thank you so, so much for everything that you've done for me.
Apart from the many tutes you've taught me (intro Micro, Core Micro, QE,
and revision tutes), you also helped me with my thesis (remember when we were
in your garden way-back-when in April 2019?), with game theory, and with lots
of other things beside.

I still remember most fondly our spicy noodle dinners with Filip and Martin,
the Chinese New Year banquet with the Warden, dinner and board games at your place,
lunch at Liddell... I really don't think I could have asked or dreamed of a better tutor.
It was truly my good fortune and an absolute honour to have been your student
these past three years.

With much love
Zhenghong
