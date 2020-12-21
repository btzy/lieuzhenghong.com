# Thesis TL;DR

## Abstract

How should electoral districts be drawn? In the U.S., many states attempt to limit gerrymandering by requiring that districts be "reasonably compact", but also require that plans respect "the integrity of communities of interest". Yet mandating compactness may come at the cost of communities of interest. In order to achieve a compact district shape, one may need to disregard communities of interest and assemble highly heterogeneous districts as a result, adversely affecting democratic outcomes like representation and responsiveness. Are compactness and community fundamentally conflicting goals?

I make two contributions in this work. First, I develop a new compactness metric---human compactness---that improves upon previous measures by incorporating a notion of travel times. Second, I use a Markov Chain Monte Carlo (MCMC) approach to generate a large sample of districting plans. I find mixed evidence for a trade-off between compactness and homogeneity depending on the compactness measure used. I further find that my human compactness measure consistently identifies more homogeneous districts, suggesting that a judicious choice of compactness metric can in fact encourage keeping communities of interest together.

## Introduction (front part)

- We care about how districts are drawn because of representation:
formalistic and descriptive/substantial representation

Formalistic representation is about accountability: gerrymandering
lets incumbents stay in power regardless of their performance and
are thus unaccountable. 
Hence legislators have tried to prevent this using compactness measures

Descriptive/substantial representation is about their
elected representatives fighting for their electorate's interest:
this is usually best done when districts are homogeneous/
keep communities of interest together

However, one might think that compactness and district homogeneity
would come apart: a perfect square might be very compact
but cleave a community of interest in two, that sort of stuff.
So we want to know if there's a tradeoff
and my thesis addresses this.

## Two key research questions

1. Is there a tradeoff between compactness and communities of interest?
2. Do some compactness measures better encompass communities of interest than others?

## Methodology

1. Generate a large and representative subset of plausible districting plans
2. Evaluate compactness and spatial diversity scores on that subset of plans
3. Analyse the overall relationship between compactness and communities of interest (as operationalised by spatial diversity)


## Human compactness and why the inter-voter distance is important

"Paramount to the idea of single-member districts is that there is great value in voters who live in the same area being put in the same district. Eubank and Rodden [2019] write:

> "Voters in the same area are likely to share political interests; voters in the same area are better able to communicate and coordinate with one another; politicians can better maintain connections with voters in the same area; voters in the same area are especially likely to belong to the same social communities --- all suggest the importance of voters being located in districts with their geographic peers."
    
Due to the fact that voters in the same area share many things in common, A point-wise distance measure that tries to put people together in the same district could be a remedy for the key claim levied against compactness---that it splits communities of interest. A wealth of empirical evidence supports the above statement. \cite{arzheimer2012} find that constituents support less strongly candidates that live far from them, even controlling for strong predictors of vote choice like party feeling and socio-economic distance. Similarly, \cite{dyck2005} find that voters living further away from a voting site are less likely to turn out to vote. In part, voters strongly support proximate candidates because they think that these candidates better represent their interests. If voters prefer a representative who lives close to them, then we can satisfy the most voters by drawing districts where everyone lives close to everyone else---only then can that district have a representative who lives close to everybody.
    
In contrast, districts that put people with unrelated, faraway others carve voters out of their natural communities and are thus to be avoided. We care about whether co-districtors live in the same area and belong to the same communities of interest, not just the compactness of their electoral district. And point-wise distance metrics deliver exactly that.j

## Why Euclidean distance is insufficient

"Suppose there is a city on a hill example"

Suppose there is a city on a hill. On the West side is [a] mild, long incline toward the rest of the city, which is in a plane. On the East side is a steep cliff, either impassable or with just a narrow, winding road that very few people use. While the next residential center to the East is much closer to the hilltop on a horizontal plane, it is much further on all sorts of distances that we think might matter: transportation time, intensity of social interactions, sets of shared local public goods and common interests, etc. Thus, for all practical purposes, one probably wants to include the hilltop in a Western district rather than an Eastern one. More general notions of distance can handle this.
    
Here we see the key problem with using Euclidean distances in point-wise distance metrics. The "impassable" region on the East would have a short Euclidean distance, and any districting plan that put the hilltop with the Eastern district would be unfairly penalised by these point-wise distance metrics. Evidently, using driving durations instead would give us more accurate scores. Using driving durations, the impassable region would have a long driving duration, accurately reflecting the political geography. In this and many other cases like it (e.g. large bodies of water), driving durations better reflect a state's unique political geographies.

**NOTE:** let's see if we can find these in real life

## What I actually did

1. Use Recom neutral ensemble to generate 10,000 districting plans for each state
2. Calculate spatial diversity and all compactness scores
3. DO data analysis:
   - Some initial analysis looking at New Hampshire and Idaho
    showing that there is a difference in the best plans under each compactness measure
   - Correlation matrix showing that compacntess measures correlate with one another but human compactness less so:
  "this result is encouraging because it shows that these metrics are able to get at the same concept of compactness despite having completely different theoretical backgrounds".
   - Did some scatterplots that basically say the same thing:
   compactness measures are similar but not too similar
   - Spatial diversity varies a lot between states but little within states:  may be due to the fact that the plans I generate are meant to resemble plans that a non-partisan districting committee would draw
   - KDE plot of districts and spatial diversity: the smaller (by area)
   the district, the higher the diversity. Most probably an urban-rural effect.
4. Data analysis part 2:
   - Running multivariate OLS regressions with country dummies finds no effect of different compactness measures on spatial diversity; only human compactness sees a significant negative effect
   - Previously we were doing the regression with *all* of the plans: now consider the *subset* of plans:
     - I look at Top 100/90/75/25/10%, 5% plans under each compactness measure and find similar results (5% and 2% sample size too small for significance but coefficient is the same)
     - I look at the mean spatial diversity of the top plans under each compactness measure, performing a difference in means test.
     Only human compactness has a mean spatial diversity significantly lower than the mean spatial diversity of all plans.
     - I then perform a more robust difference in means test: 
     I look at the mean spatial diversity of the most compact plans *of each state*, and compare it with the mean spatial diversity of all plans, and again, human compactness beats them all


## What needs to be done next

- One thing we could do is run all the correlations and difference-in-means tests with Euclidean distance human compactness.
I suspect that there won't be much of a difference 
(possibly nothing that approaches statistical significance)
- The other thing we could do is after running all of them with Euclidean distance
    human compactness, find states/plans where they differ a lot
    and see where they differ
- Another thing we could do if we don't want to run it on all the plans is to pick a plan, calculate ED human compactness for each point in that plan,
and compare that to DD human compactness. See if they meaningfully differ.
- Either way we have to come up with the Euclidean distance metric and generate plans. If only we had a pipeline to make this faster. 
