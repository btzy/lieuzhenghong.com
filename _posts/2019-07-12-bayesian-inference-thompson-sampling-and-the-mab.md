---
layout: base
date: 2019-07-12
title: "The beta-Bernoulli bandit, Thompson sampling, and Bayesian inference"
tags:
  - academic
  - economics
  - behavioural economics
  - quantitative economics
  - statistics
  - explanation
  - bayesian inference
  - explanation
  - public
permalink: "/{{ page.date | date: '%Y/%m/%d' }}/{{page.fileSlug}}/"
---

I'm using the work I do at my internship to run a behavioural economics
experiment. Trying to run this experiment has led me down an incredibly deep
rabbit hole, and I wanted to write down some of the things I've learned before
I inevitably forget.

I also wanted to use this blog post to defend many of the decision points I
made---there were many points where I had to make a decision to use one
approach or another, and I spent many hours thinking and reading about the best
approach.

---

## Background

I'm trying to send SMSes to customers telling them to install an app.
Behavioural economics predicts that people are loss-averse, so I am trying to
find out if sending SMSes that have a loss-aversion framing

> "install the app
> now, or you'll lose your 4500THB cashback"

has a greater effect than sending
SMSes that have a positive framing

> "install the app now, to get 4500THB
> cashback"

The question is:

**How can we find out which SMS is best?**

The gold standard of causal inference is to do a randomised experiment:
randomly divide my 2400 participants into groups of 800 each, then send 800 the
neutral (control), 800 the positive, and 800 the negative. Record the number of
successes (clicked SMS) and failures (did not click SMS) for each treatment.

By the Central Limit Theorem all of these will be normal distributions. We can
then do the usual t-tests/chi-squared test and test that there is a
statistically significant difference between the means. (More precisely, we
reject the null hypothesis that there is no difference between the means).

This is Good and Rigorous™ — but the problem is nobody is going to let you run
it because this is leaving money on the table. Only 800 customers are going to
get the optimal treatment, but that means 2/3rds of them will be getting a
suboptimal treatment.

Is there a better way? Specifically, is there an optimal way to send the SMSes
so that we can "know" which treatment is best with some notion of certainty,
yet still get the most number of people receiving the optimal treatment at the
end of the day?

**Why this can be modelled as a multi-armed bandit problem**

It turns out that this is an incredibly-well-studied field, with a lot of applications everywhere from medical trials to (of course) marketing.

The explanation of the multi-armed bandit is incredibly intuitive, and it's
something you just grok the instant you hear about it.

> You are walking around the casino floor where there are ten slot machines,
> each with a different probability of paying out. How should one pull the slot
> machines in order to maximise one's payout over the long run?

There are two tradeoffs here. On the one hand, we want to _explore_ in order to
find out what the best slot machine is. The best way to be sure of what the
actual probabilities of the payouts are is to pull every arm equally.

But on the other hand, do we really _care_ about what the actual probabilities
of _all_ the payouts are? Does it really matter if slot machine #4 could have
a probability of 0.01--0.03 if we are pretty sure that slot machine #5 has a
probability of 0.40-0.60? Fundamentally we want to _exploit_: if we are already
90% sure that this slot machine is the best one, we shouldn't keep pulling the
others to "explore", because that will in expectation reduce our earnings.
[This
post](https://lilianweng.github.io/lil-log/2018/01/23/the-multi-armed-bandit-problem-and-its-solutions.html#bandit-strategies)
was incredibly helpful for getting the intuitions, and I'll refer to this post
again and again.

In the same way, it's suboptimal [^1] to run a "pure exploration strategy" of
800/800/800 split. Once we've made, say, 100 pulls each, we should be more or
less "sure enough" about the probability of each treatment, and therefore we
should "shift gears" and start the exploitation.

[^1]: Here I should clarify --- suboptimal _for what_? For a scientific experiment where the goal is to discover a fact about the world, then we shouldn't care about exploitation at all. We want the highest possible statistical power, and that means maximising exploration. But of course in this case where money is on the line, some balance of exploration and exploitation must be struck.

---

OK, so now I've shown that if we want to maximise our payout (also called the
"cumulative reward"), then a pure exploratory strategy is suboptimal. That
leads to a very natural follow-up question:

**What is the optimal strategy to maximise cumulative reward?**

Now that we have intuition firmly in our heads, it is useful at this point to
introduce some mathematics so that we can more formally specify the problem.

I'll not focus here on the general multi-armed bandit (MAB) problem. Instead
I'll specify the Bernoulli bandit, and I'll modify slightly the description
from [this paper](https://web.stanford.edu/~bvr/pubs/TS_Tutorial.pdf)

> _(Bernoulli Bandit)_ Suppose there are $K$ actions and $T$ time-steps,
> and when an action is played, it yields either a success or a failure. Action
> $k \in {1, ..., K}$ produces a success with probability $\theta_k \in
> [0,1]$. If there is a success, then $r_t = 1$, else $r_t = 0$. The
> success probabilities are unknown to the agent, but are fixed over time. The
> objective is to maximise the cumulative reward $\sum^T_{t=1} r_t$ over
> $T$ periods, where $T$ is relatively large compared to the number of arms
> $K$.

Let's first think about a few simple strategies. Let's start with the worst:

1. Random -- choose an arm at random every period.

First of all, the random strategy is exactly that---random---and the expected
cumulative reward for this strategy is simply

$$\sum^K_{k=1} \frac{T}{3} \theta_k.$$

For instance, if $\theta = \{0.3, 0.4, 0.5\}$ and $T=300$, then the random
strategy would give $\mathbb{E}[r] = 30 + 40 + 50 = 120$.

Notice that the Random strategy is exactly the "random assignment" algorithm of
assigning 800/800/800.

Can we do better? Let's try the following:

2. "Dumb" Greedy(N) -- pull each arm N times. Pick the arm with the highest sampled
   $\theta$; call it arm $K^{*}$. Then always pull arm $K^{*}$ henceforth.

Note the two degenerate cases: if $N=0$, Dumb Greedy picks an arm at random
and pulls it all the way. If $N=T/K$, the greedy approach reduces to the
random strategy. For intermediate values of N, we _first_ pull all arms N
times, to get a better idea of the distribution, then checks the best arm and
pulls that. Greedy(N) dominates random choice, because it
gets _some_ information about which arm is best, and uses that information to
inform its choice.

This strategy's effectiveness follows a U-shaped curve: it's no better than
random choice if you just pick a random arm at t=0 and pull it forever, or
forever pick a random arm. By the law of large numbers, the more you pull, the
more certain you are about the true means of the arms, but the less time you
have to pull the best arm. This captures our intuition of exploring and
exploiting: the knowledge you gain from exploring is good, but only if you
manage to exploit that knowledge.

_TODO (questions for author): How much better is Greedy(N) than random? What is the optimal N?_

It would be good if we had some measure of not just the mean, but also how
_certain_ we were of our estimate of the mean. If I flip a coin 10 times and get
1 head and 9 tails, I am much less certain of its fairness as if I were to flip
that coin 500 times and get 50 heads and 450 tails.

It turns out that measure does exist, and it's called ...

**The beta distribution**

The beta distribution can best be thought of as "a distribution of probabilities
--- that is, it represents all the possible values of a probability when we
don't know what that probability is."

[This Stats.SE thread entitled "What is the intuition behind beta
distribution"](https://stats.stackexchange.com/questions/47771/what-is-the-intuition-behind-beta-distribution)
has loads of fantastic answers, and it's where I got that explanation from. I
would certainly recommend reading through David Robinson's answer.

Here's how I would explain it:

We know that the treatments are Bernoulli with parameter $p$. Then in $N$
repeated trials the treatments must follow a binomial distribution with $B(N,
p)$.

Suppose we conduct N trials and observe $\alpha$ successes and $\beta$
failures. Then the beta distribution $Beta(\alpha+1, \beta+1)$ gives us the
_range_ of "reasonable estimates" of the binomial distribution parameter $p$.

![](/img/thompson-sampling/beta_distribution_1.png)

This image by Raffael Vogler very nicely shows why a beta distribution gives us
what we want. We wanted a measure of the mean but also a measure of our
certainty that the mean is what we think it is. Here we can see that while the
orange curve has a higher mean (0.9), our "best estimate" of its true value is
quite diffuse. On the other hand, we're quite sure that true value of the
second curve (in yellow) lies close to 0.8.

Furthermore, the beta distribution has a lovely property in that we can
"update" the beta distribution very easily as we get more data. Suppose we have
2 heads and 8 tails: the beta distribution is $Beta(3, 9)$. We flip the coin
again. It comes up heads. Then the beta distribution easily updates to
$Beta(4,10)$.

Armed with this knowledge of beta-distributions, we can try the following strategy.

Can we do better? Let's try the following:

1. "Smart" beta-Greedy: At every time step, calculate $\hat{\theta}$ of every arm,
   then pull the arm with the highest $\hat{\theta}$ and update the
   $\hat{\theta}$ according to the result.

How "Smart" beta-Greedy works: Initialise each arm with $\hat{\theta} =
\mathbb{E}[Beta(1, 1)] = 0.5$. The $Beta(1,1)$ distribution is a uniform
distribution over [0,1], and is what's known as an _uninformative prior_: we
assume that all rewards are equally likely.

At the start, seeing that all thetas are equal, we pull an arm at random;
call this arm $k$. We update $\hat{\theta_k}$ appropriately.

We update as follows:

- If we do get a reward: $(\alpha_k, \beta_k) = (\alpha_k+1, \beta)$
- If we do not get a reward: $(\alpha_k, \beta_k) = (\alpha_k, \beta+1)$

Finally, pick the best $\hat{\theta}$, which is given by
$\frac{\alpha_k}{(\alpha_k + \beta_k}$. Repeat this process.

This greedy algorithm is smarter than "dumb" greedy, because it constantly
reevaluates what the best arm is with our new beta updating rule. This is
pretty good, right?

_Can we do better?_

Take a look at this image from _A Tutorial on Thompson Sampling_.

![](/img/thompson-sampling/beta_distribution_2.png)

There are three possible arms. The greedy algorithm would always choose action
1, because action 1 has the maximal expected mean reward. "Since the
uncertainty around this expected mean reward is small, observations are
unlikely to change the expectation substantially, and therefore, action 1 is
likely to be selected _ad ininitum_."

It seems reasonable to avoid action 2, since it is extremely unlikely that
$\theta_2 > \theta_1$, but the algorithm should try out $\theta_3$, because
if you take a look at that distribution in red it's quite plausible that its
mean reward exceeds 0.6. "The algorithm fails to account for uncertainty in the
mean reward of action 3, which should entice the agent to explore and learn
about that action." (p. 10-11)

Let's try and capture some intuition here. The problem with "Smart" Greedy is
that it can be misled by an initial lucky or unlucky streak, and get stuck in a
suboptimal maxima of exploitation. We could modify "Smart" Greedy to pull every
arm N times first, just like "Dumb" Greedy(N), but here's another way to do it:

1. ε-Greedy -- like "Smart" Greedy, but with probability $\epsilon$ pull an
   arm at random.

The ε-greedy algorithm takes the best action most of the time, but does random
exploration occasionally. This will prevent the algorithm from getting "stuck"
on a local optima: 5% of the time it will try action 3, for instance, and learn
more about it. Eventually the ε-greedy algorithm will converge onto the best
action.

_TODO (questions for author): How good is ε-Greedy compared to Smart Greedy?_

But again ε-greedy is not optimal for two reasons. First, if we're already dead
certain about the best lever, we don't want it to pull a random bad lever ε of
the time! Second of all, it wastes pulls exploring arms we're already certain
about. In this case we want to explore action 3, and we don't want to explore
action 1 at all. Yet the ε-greedy algorithm will select action 1 and 3 with
equal probability.

This is suboptimal. We need something that intelligently allocates exploratory
effort: go where your estimates are the most uncertain. Can we do better?
Enter...

**Thompson sampling**

Thompson sampling is a very subtle modification of the "smart" greedy
algorithm: so subtle, in fact, that I missed it the first time! Here's the
difference: instead of choosing the highest expected theta value, _sample_ the
theta values from the beta distributions.

Take a look at the image again:

![](/img/thompson-sampling/beta_distribution_2.png)

The expected rewards are $\theta = [0.6, 0.4, 0.4]$. The greedy algorithm
selects the action with the highest expected reward: that is, action 1.
Thompson sampling _samples_ from the beta distributions: in other words,
$\hat{\theta_k} \sim Beta(\alpha_k, \beta_k)$. It then pulls the arm with the
maximum sampled reward.

This is genius! Why? Consider a typical sample. Sampling action 1 will give us
a value very close to 0.6. Sampling action 2 will give us a value very close to
0.4. Sampling action 3, on the other hand, will give us a wide range of values,
_including_ values greater than 0.6. This means that action 2 will pretty much
never be chosen, but there's a good chance of action 3 being chosen! In other
words --- Thompson sampling nicely directs exploration effort towards the
unknown.

I ran 10,000 simulations, and here are the results...

**Bayesian inference vs frequentist inference**

Once I have the results ....

I can use [Fisher's exact
test](https://en.wikipedia.org/wiki/Fisher's_exact_test) or the normal approximation to the binomial distribution.

By the CLT, we know that all three treatments must be normally distributed.

Bayesian inference: there is a closed form, but I can use simulation to compare
the three beta distributions:

[Given several beta distributions, what is the probability that one is the
highest?](https://mathoverflow.net/q/90361)

A paper from NIPS 2011 ("An empirical evaluation of Thompson Sampling") shows, in experiments, that Thompson Sampling beats UCB. UCB is based on choosing the lever that promises the highest reward under optimistic assumptions (i.e. the variance of your estimate of the expected reward is high, therefore you pull levers that you don't know that well). Instead, Thompson Sampling is fully Bayesian: it generates a bandit configuration (i.e. a vector of expected rewards) from a posterior distribution, and then acts as if this was the true configuration (i.e. it pulls the lever with the highest expected reward). [^2]

[^2]: Pedro A. Ortega (https://stats.stackexchange.com/users/9572/pedro-a-ortega), Best bandit algorithm?, URL (version: 2017-03-24): https://stats.stackexchange.com/q/24027

Call the different SMS treatments A, B, and C, and the probability of someone
installing the app $$r$$ can be conditional on either one of these treatments.
The _value_ of each treatment $Q(\cdot)$ is the expected reward given that
treatment, $Q(A) = \mathbb{E}[r|A]$.

**A little wrinkle**

[Formulas for Bayesian A/B Testing](https://www.evanmiller.org/bayesian-ab-testing.html#notes)

Why do I use Bayesian methods?

- Frequentist approaches require me to set sample size for adequate power, and
  this sample size depends on effect size. But I have no good prior for effect
  size
- Sample size large

**Contextual bandits**

Agarwal 2013 [Thompson Sampling for Contextual Bandits with Linear
Payoffs](http://proceedings.mlr.press/v28/agrawal13.pdf)

**Top-two Thompson Sampling for Best-Arm Identification**

[Simple Bayesian Algorithms for Best-Arm Identification](https://arxiv.org/pdf/1602.08448.pdf)

Now suppose we have
