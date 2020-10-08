---
title: "Pair work: the One Weird Trick to finally ship your side projects"
layout: base
author: Lieu Zheng Hong
date: 2020-10-08
tags:
  - exploration
  - productivity
  - scratchpad
  - public
  - draft
---

<div class="toc">

[[toc]]

</div>

**_This is a draft._**
_Epistemic status: somewhat uncertain._

_Time taken to write this draft_: ~30 minutes ideation, ~1h writing.

## Introduction

I may have stumbled upon the _One Weird Trick_ for maintaining momentum
on side projects. If your side projects are collaborative (most of mine are,
these days), the following (which I call _pair work_) really helps:

1. Commit to a date and time period (~2h) with your partner.
2. Get on a call.
3. One person shares screen. You might use
   a collaborative editor.
4. Work together.

This feels so pedestrian that it doesn't seem worth writing about.
Maybe everyone already does this but somehow I've missed the memo.
In any case---if you haven't been doing this already, I highly recommend trying it.

I want to distinguish _pair work_ from _group work_.
"Group work" often means
to portion out a task into smaller subtasks and
assign each person a small bit.
But I think this approach is paradoxically suboptimal.
Paradoxical, because surely working in parallel is faster than working serially?--
but in thought work, the bottleneck isn't raw execution speed.

Also, I specifically use the term _pair work_ because
I don't just mean pair _programming_---
I believe there are benefits to
pair reading-the-documentation,
pair understanding,
and so on.

I can personally vouch for the effectiveness of this strategy,
particularly if you have a project that's been mothballed for quite a while now.
Joshua and I meandered around for weeks without any progress until we decided
to debug together. We got more done in two hours than we did the past three weeks.

Why and how is pair work so effective?
In my experience, there are three main benefits:
pair work acts as a strong commitment device,
it removes blockers effectively,
and shares information amongst all collaborators "for free".
It's very effective despite the apparent loss of parallel productivity
because the bottleneck in knowledge-based side projects is not raw productivity,
but rather motivation, faulty assumptions, and incomplete information.

## Pair work acts as a commitment device

This is by far the most important benefit to me.
When I start side projects, I always want to work on them but other life stuff
gets in the way: be it revising for exams, preparing for a job interview,
meeting friends, binge watching YouTube, and the like.
Making a public commitment to someone gets you 80% of the way there
because you'll be afraid to let them down.
But setting a time to _work together_ with a collaborator gets you the last 20%, because
without the commitment to work together it's too easy to come up
with plausible-sounding reasons to excuse yourself.

## Pair work helps remove blockers

Even if you sometimes have the motivation,
you might be put off by a tedious part of the project.
This is me whenever I'm faced with "weed-clearing" work like setting up builds
or debugging `import` incompatibilities.
The problem is that the tedious parts of the project still need to be done,
and the more you put it off the more you ruin your productivity.
Tedious work is much less so when done together with your collaborator.

Working together also helps
when you don't have a clue about how to tackle a particular problem.
For instance, I was stuck on a pretty nasty bug when building the board game engine,
which blocked me for days as I would dread even _trying_ to solve the problem
after banging my head against it fruitlessly for so long.

Talking through a bug with someone else helps a lot;
talking through a bug with someone else _also involved in the project_
helps immensely.
And obviously two minds are better than one;
any problem that appeared insurmountable alone always seems to fall quite quickly.

Pair work also surfaces incorrect assumptions.
Most (if not all) misunderstandings arise because one person has a faulty assumption/
mental model.
Through the process of argument and discussion that naturally occurs in pair work,
these assumptions can quickly be uncovered.

For instance, Joshua is a very experienced data scientist but has little JS experience.
He had an incorrect understanding of `async` and `await`
(specifically, he didn't believe that `await` blocked execution)
and thus he incorrectly rewrote my code.
But when working together, I was able to surface this incorrect assumption.
This misunderstanding might otherwise have gone unnoticed for a long time.

## Pair work puts everyone on the same page

It may be faster for two people to split up and work on different things initially,
but this causes two silos of knowledge to be formed,
and it becomes very difficult to work together in the future
unless significant time is invested familiarising each other with the
knowledge of each part. The cost of `brain merge`-ing may be greater than
the gains from parallelisation.

This happened when Joshua read up on the multiplayer server architecture
and I did all the client-side work.
But that meant that Joshua knew nothing about what I was doing on the client side
and what difficulties I was facing, and _mutatis mutandis_ for me.
This would result in us often talking past each other
when discussing how to implement new features.
With such a small team and such an interconnected codebase
we couldn't _not_ know every part of the system.
I think had we worked together from the start, initial progress would be slower
but overall progress would be faster.

## Caveats

This doesn't work without a partner, obviously.
There are also some tasks where you _do_ want to work in parallel,
like tasks of an exploratory nature e.g. lit review (just to cast a wider net),
or trivial tasks where being blocked is not an issue.

You might also get frustrated sometimes if you and your partner disagree on what to do
or how to do something.

You could probably do pair work with three people (trio work?),
but no more than that.
So this would not be feasible with extremely large projects or extremely
large teams.

## Why this eluded me for the longest time

I hated group work in school.
Everyone felt that everyone else was not doing their fair share of the work,
or disagreed on what should be done,
or believed that others' work was not up to snuff.
It was overall a very grim experience,
and I just assumed that would translate to pair work as well:
that's just setting N=2, right?
But there's a world of a difference between
_working as a group of two_ (splitting the work half-half)
and _working as a pair_ (doing all the work together).

Now that I've started working in pairs I really can't recommend it enough.
It helps a lot that
i) I've grown up and am now (I hope) less difficult to work with,
ii) I get to choose who I work with on my side projects,
iii) I _want_ to work on my side projects---life just gets in the way.

## Conclusion

So far, I've found pair working extremely effective:
primarily as a commitment device
but also
with the (significant) side benefits of being able to unblock yourself quicker
and having knowledge automatically shared amongst collaborators.
If you do try it out (or have already been practicing it for a while),
I'd love to hear from you about your experiences, and if there are any
pitfalls to watch out for---shoot me an email.
