---
title: "A market-based mechanism to preserve Indonesia's forests (or any other resource)"
layout: base
author: Lieu Zheng Hong
date: 2020-08-19
tags:
  - exploration
  - game theory
  - mechanism design
  - economics
  - incentive
  - public
---

[[toc]]

## Introduction

Enormous swathes of virgin forest in Indonesia are being cut and burned down
all the time and this contributes significantly to the climate crisis.
How can we stop this? I propose a decentralised market-based mechanism
that has the following desirable properties:

- Scalable
- Decentralised
- Bounded cost for the philantropist
- Owners of the land are better off

Norway has some sort of agreement with Indonesia where they pay Indonesia
\$1 billion to reduce their forest emissions: see links
[here](https://www.wri.org/blog/2019/02/indonesia-reduces-deforestation-norway-pay)
and
[here](https://news.mongabay.com/2019/02/indonesia-to-get-first-payment-from-norway-under-1b-redd-scheme/).

This is great and should be applauded.
But this sort of enormous government-to-government approach
has its problems. First of all, what can _we_ do as private citizens, apart
from lobbying our governments? Also, this approach is _slow_:

> The two countries signed the \$1 billion pact in 2010, under the REDD+
> (reducing emissions from deforestation and forest degradation) mechanism. In
> exchange for the funding, Indonesia would have to slow its emissions from
> deforestation, which accounts for the bulk of its CO2 emissions. That
> it’s taken so long for the first payment to be announced is due to a
> combination of the structuring of the agreement and a change in the
> Indonesian government since the 2010 signing.

I present a market mechanism that might help safeguard the forests, but doesn't
require long and protracted intergovernmental negotations and can work with
only a few dollars of funding.
The idea is probably not original and I would greatly appreciate if someone
could point me to the relevant literature.

## The mechanism in brief

In brief, the idea is as follows:
philantropists can sell a _ticket_ attached to some forested area
that pays out _if and only if_ that area remains pristine.
With satellite imagery, we can easily tell whether an area has been logged or not,
and this would serve as a source of truth.

Here's how it would work.
Suppose we have a philantropist that wants to preserve some area of forest.
And suppose his maximum willingness to pay for this area of forest is \$50,000.
And now suppose we have some satellite feed of this area
(e.g. [zoom.earth](https://zoom.earth/)).
Then what the philantropist can do is say the following:

"I will pay \$50,000 to the person who buys this ticket if and only if <AREA>
remains forested by <DATE>, as determined by satellite imagery."

And then he simply puts this ticket up for auction. Once someone wins the bid,
the buyer pays the philantropist. The philantropist then puts his funds in escrow,
and some trusted third-party determines whether or not the area has remained
forested by the date specified in the ticket---whereupon the funds will either
be released back to the philantropist, or to the buyer of the ticket.

How does this work? The buyer has an incentive to hunt down the farmer/owner
of the forest and come to some deal to make sure that the farmer/owner
doesn't cut down the land. This will probably take the form of a side payment.
And if the farmer is savvy enough he can of course purchase the ticket himself
and earn free money from doing nothing at all.

This mechanism has several attractive qualities.

Firstly, it's _decentralised_: there is no government intervention needed.
This is also _scalable_: any person could conceivably sell such a ticket for as
small or as large an area as they want, so if any citizen
wanted to be a Keeper of the Grove it they could do it _today_, without
having to lobby their governments to do something. All you'd need is a trusted
third party to i) hold funds in escrow and ii) verify the forest cover of the area,
both of which could be incentivised with some fees.

## Possible problems with this mechanism

- Collusion amongst buyers when there are multiple plots on auction
- Unintended consequences
  (buyers of tickets start coercing, intimidating, or assassinating farmers
  to prevent them from cutting down the forest)
- The owner of the land doesn't get the surplus, instead it'll probably be some
  finance bro paying the owner of the land some marginal return,
  and that rubs me the wrong way

## Conclusion

Of course, this works with any resource that we want to preserve, not just Indonesia's forests.

Have I missed something? Interested in implementing this? Send me a message, please.

## Things I cut

The key here is to realise that a) the forests are a _positive externality_
in the sense that they sequester carbon and reduce global temperatures, and
b) we are much richer than many of the Indonesians who own the forests, and
they need to eat.
