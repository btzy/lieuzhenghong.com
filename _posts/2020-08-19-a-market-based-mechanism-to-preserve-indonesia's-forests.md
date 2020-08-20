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

## Background

Norway has some sort of agreement with Indonesia where they pay Indonesia
\$1 billion to reduce their forest emissions: see links
[here](https://www.wri.org/blog/2019/02/indonesia-reduces-deforestation-norway-pay)
and
[here](https://news.mongabay.com/2019/02/indonesia-to-get-first-payment-from-norway-under-1b-redd-scheme/).

> The two countries signed the \$1 billion pact in 2010, under the REDD+
> (reducing emissions from deforestation and forest degradation) mechanism. In
> exchange for the funding, Indonesia would have to slow its emissions from
> deforestation, which accounts for the bulk of its CO2 emissions.

This is great and should be applauded.
But this sort of enormous government-to-government approach
has its problems. First of all, what can _we_ do as private citizens, apart
from lobbying our governments? Also, this approach is _slow_: the first payment
was paid out almost _ten years_ after the agreement was signed.

> That it’s taken so long for the first payment to be announced is due to a
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
People would bid on the price of this ticket and the highest bidder would
stand to gain (Ticket Payout Price - Price Paid for Ticket).
With satellite imagery, we can easily tell whether an area has been logged or not,
and this would serve as a source of truth.

## An explanation of the mechanism

Here's how it would work.
Suppose we have a philantropist that wants to preserve some area of forest.
And suppose his maximum willingness to pay for this area of forest is \$50,000.
And now suppose we have some satellite feed of this area
(e.g. [zoom.earth](https://zoom.earth/)).
Then what the philantropist can do is say the following:

> "I will pay \$50,000 to the person who buys this ticket if and only if $AREA
> remains forested by $DATE, as determined by satellite imagery. Otherwise,
> the $50,000 will go to a reputable $FOREST_PROTECTION_CHARITY
> both buyer and seller have agreed upon."

And then he simply puts this ticket up for auction. Once someone wins the bid,
the buyer pays the philantropist. The philantropist then puts his funds in escrow,
and some trusted third-party determines whether or not the area has remained
forested by the date specified in the ticket---whereupon the funds will either
be released to the buyer, or to the forest protection charity.

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

## FAQs

### Why not pay the owners directly? Why the need for this complicated scheme?

How are you going to track down the owners of the land if they live in a forest
in the middle of nowhere? Is there a unified land ownership and designation map?
Is your Indonesian good enough to find out? How likely is it that that the land
ownership map is constantly updated?
What happens if ownership has changed hands without your knowledge?
What happens if the land is co-owned by several smallholders in some sort of
sharecropping arrangement? And so on.

An Indonesian friend of mine wrote to me:

> A universal land designation map was initiated in 2014, but it hasn’t come to
> completion yet because the project has been delayed over and over again.

Rather than having to spend effort to track them down ourselves,
the idea is to pay middlemen an "information arbitrage" fee:
to provide the service of tracking down the owners of the land.
The hope is that these middlemen who buy the ticket will have low-cost ways to
contact and convince the farmers.

### Wouldn't this incentivise owners to just sit on the forests and not do anything to collect their payout?

That is the entire point of this mechanism, yes.

## Possible problems with this mechanism

In a previous version of this mechanism I suggested that the \$50,000 would either
be released to the buyer, or returned back to the philantropist. I realised
that this would incentivise "philantropists" to sell a lot of tickets,
then commit arson so as not to pay out to make a profit.
Any mechanism must ensure that the philantropist can _never_ gain from this transaction.
That's why I introduced the charity. While it's possible that the charity could
collude with the seller, if they are a reputable forest protection charity
trusted by both parties then they probably i) have a good reputation,
ii) won't want to burn down forests
(they should value the forest more than they value the money).

- Collusion amongst buyers when there are multiple plots on auction
- Unintended consequences
  (buyers of tickets start coercing, intimidating, or assassinating farmers
  to prevent them from cutting down the forest)
- The owner of the land doesn't get the surplus, instead it'll probably be some
  finance bro paying the owner of the land some marginal return,
  and that rubs me the wrong way

## Conclusion

Of course, this works with any resource that we want to preserve, not just Indonesia's forests.
You can even sell tickets on areas where the land has _already_ been cut down,
and pay out iff the land gets reforested

Have I missed something? Interested in implementing this? Send me a message, please.

## Things I cut and links

The key here is to realise that a) the forests are a _positive externality_
in the sense that they sequester carbon and reduce global temperatures, and
b) we are much richer than many of the Indonesians who own the forests, and
they need to eat.
