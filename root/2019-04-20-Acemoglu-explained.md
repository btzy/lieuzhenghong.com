---
layout: base
title: "Explaining Acemoglu's model of directed technical change: a primer"
author: "Zhenghong Lieu"
tags:
  - academic
  - economics
  - macroeconomics
  - explanation
  - public
  - draft
permalink: "/{{ page.date | date: '%Y/%m/%d' }}/{{page.fileSlug}}/"
---

<style>
	.question-box {
		display:flex;
		justify-content: center;
		flex-wrap: wrap;
		background-color: yellow;
		padding: 10px;
	}
	.question-box p {
	}

	table {
		border: 1px solid black;
		border-collapse: collapse;
	}
	table td {
		text-align: center;
		border: 1px dashed black;
		padding: 5px;
	}
</style>

## Table of contents

0. Introduction and nontechnical explanation of the paradox
1. We can solve the paradox by directed technical change
2. But why would technical change be directed? Market effects
3. Implications of the model, and comparisons to other models:
   - Schumpeterian-Solow model

## Introduction and nontechnical explanation

I first want to begin with a seeming paradox. Call this **The Paradox**.
Consider these two facts:

1. The number of highly-skilled workers has increased greatly over the past few
   decades.
2. The skill premium[^1] has increased despite a huge increase in high-skilled
   workers.

This seems counterintuitive. We know the labour market is determined by supply
and demand. Therefore, it seems like the skill premium should decrease. We
must conclude that something is making the skill premium go up despite the
large influx of high-skilled workers.

What could it be? The answer is **directed technical change**: despite the fact
that there are much more high-skilled workers nowadays, high-skilled workers
have become much more productive than low-skilled ones, and therefore they
command a higher wage.

But why have high-skilled workers become much more productive than low-skilled
ones? Here's one possibility.

### The nature of technological progress this few decades (e.g. computer, microchips) has been more suited for high-skilled workers.

At first glance, this explanation seems plausible. But if you think about it,
it falls apart. See Acemoglu:

> At the expense of oversimplifying, we can say that the microchip could have
> been used to develop advanced scanners that would increase the productivity of unskilled workers, or advanced computer-assisted machines that would be used by skilled workers to replace unskilled workers. (p.31)

In other words, technology itself does not confer disproportionate benefits on
either group: what matters are the innovations that build upon that
technological breakthrough.

### The large increase in the number of high-skilled workers has made it more profitable for innovators to develop technologies that boost their productivity.

The real reason for directed technical change is actually a **market size
effect**. Innovators focus their efforts on developing technologies that
maximise their profit, and how much they can sell their R&D for depends on how
many people use their technology. The more high-skilled workers there are, the
more innovators develop for them, and the larger their productivity grows. This
nicely turns the supply-and-demand story on its head, and gives us our answer
to the paradox.

[^1]: The wage premium $$\omega$$, is defined as $$\frac{w_H}{w_L}$$.

Here, I present Acemoglu's model of directed technical change, that formalises
all we've just talked about. Why Acemoglu's model specifically?

1. It is the only model in Oxford's macroeconomics course that talks about
   directed technical change/ high- vs low-skilled workers.
2. It nicely explains **The Paradox**.

<div class='question-box'>
<p><b> Review questions </b></p>
<p> What was the empirical motivation for Acemoglu's model of directed technological change? </p>
<p> How can the skill premium go up even as the relative supply of high-skilled workers goes up?</p>
</div>

## Formalising the paradox

The production function, as well as our utility function, is given by

\begin{equation}
Y = [(A_H H)^\rho + (A_L L)^\rho]^{1-\rho}
\end{equation}

There are high-skilled goods produced by high-skilled labour, and low-skilled
goods produced by low-skill labour. We will ignore capital. Note here that this
is a CRS production function.

We shall first disregard the technology growth function (how $$A_H$$ and
$$A_L$$ change over time).

Because this is a competitive market, workers are paid their marginal productivities:

\begin{equation}
w_L \equiv MPL = A^\rho_L \left[A^\rho_L + A^\rho_H\left(\frac{H}{L}\right)^\rho\right]^\frac{1-\rho}{\rho}
\end{equation}
\begin{equation}
w_H \equiv MPH = A^\rho_H \left[A^\rho_L \left(\frac{H}{L}\right)^{-\rho} + A^\rho_H\right]^\frac{1-\rho}{\rho}
\end{equation}

Combining these two equations we get the _skill premium_ $$\omega$$:

\begin{equation}
\omega \equiv \frac{w_H}{w_L} = \left(\frac{A_H}{A_L}\right)^\rho \left(\frac{H}{L}\right)^{-(1-\rho)}
\end{equation}
\begin{equation}
= \left(\frac{A_H}{A_L}\right)^{(\sigma-1)/\sigma} \left(\frac{H}{L}\right)^{-(\frac{1}{\sigma})}
\end{equation}

where $$\sigma$$ is the elasticity of substitution: $$\sigma \equiv \frac{1}{1-\rho}$$[^2]

Taking logs on both sides gives
\begin{equation}
\ln \omega = \frac{\sigma-1}{\sigma} \ln(\frac{A_h}{A_l}) - \frac{1}{\sigma}\ln(\frac{H}{L})
\end{equation}

Let's take a look at this last equation, and plot it in a graph with x-axis
$$\frac{H}{L}$$. We can see that as the number of skilled workers increases
($$H \uparrow$$), the lower the wage premium.

![An increase in skilled workers causes a decrease in the wage
premium](/img/acemoglu_explained/wage_premium.png)

An increase in skilled workers ($$H^{*} \rightarrow H'$$) leads
to a decrease in wage premium (movement from A $$\rightarrow$$ B).

<div class='question-box'>
	<p><b> Review questions </b></p>
	<p> What is the production function stated by Acemoglu?</p>
	<p> What is the skill premium?</p>
	<p> What is the elasticity of substitution? How does it relate to \(\rho\)? </p>
</div>

[^2]: How do we get the elasticity of substitution?? How is it defined? TODO

---

## Solving the paradox by directed technical change

We have just formalised the result that as the relative ratio of high-skilled
workers increases, the wage premium decreases. This is great, but how then can
we explain the empirical finding that the skill premium $$\omega$$ has
increased over the decades? The answer is a combination of both elasticity of
substitution $$\sigma$$ and a _skill-biased technical change_. Looking once
again at the previous equation, we see that $$\omega$$ can increase if the term
$$\frac{\sigma-1}{\sigma} \ln(\frac{A_h}{A_l})$$ increases.

Under what circumstances will this term increase? Well, one way is to increase
$$A_h$$. But an increase in $$A_h$$ will only increase this term if $$\sigma >
1$$. If workers are not very substitutable ($$\sigma < 1$$), an improvement in
the productivity of skilled workers _reduces_ the skill premium. This case
appears paradoxical at first but is in fact quite intuitive. As Acemoglu says:

> Consider, for example, a Leontieff (fixed proportions) production function.
> In this case, when $$A_h$$ increases and skilled workers become more
> productive, the demand for unskilled workers, who are necessary to produce
> more output by working with the more productive skilled workers, increases by
> more than the demand for skilled workers. In some sense, in this case, the
> increase in $$A_h$$ is creating an “excess supply” of skilled workers given the
> number of unskilled workers. This excess supply increases the unskilled wage
> relative to the skilled wage.

Okay. So suppose $$\sigma > 1$$. Then, an increase in $$A_h$$ will indeed increase the wage premium by shifting the line upwards.

![Skill-biased technology change can offset an increase in skilled labour,
causing the wage labour to increase](/img/acemoglu_explained/wage_premium_2.png)

Figure 2 illustrates. Despite the increase in H/L, skill-biased technology change causes
the wage premium to increase from $$w^*$$ to $$w^{**}$$.

Great---we have solved the paradox by introducing skill-biased technical
change. More explicitly, the relative productivity of skilled workers,
$$(A_h/A_l)^\frac{\sigma-1}{\sigma}$$, must have increased.

## Acemoglu's model with endogenous directed technical change.

I've just shown that one can have an increase in the ratio of high- to low-
skilled workers IF the coefficient of substitution $$\sigma > 1$$ AND technical
change is directed towards high-skilled workers.

But that begs the questions: why _was_ technical change directed towards
high-skilled workers? Now we attempt to _endogenise_ technical change (i.e.
try and find a reason _within_ the model why technical change was directed).

We have our utility/production function once again:

\begin{equation}
Y = [(A_H H)^\rho + (A_L L)^\rho]^{1-\rho}
\end{equation}

Here, let's introduce some innovators. Innovators can produce innovations,
$$A_H$$ or $$A_L$$, that increase the productivity of all high- or low-skill
workers. Let the fixed cost of producing an innovation be B and let the
marginal cost of producing the new technology be 0. Then the marginal benefit
of providing a new technology is simply the marginal increase in productivity
($$H$$ or $$L$$) multiplied by the price of that good; this gives $$p_H H$$ and
$$p_L L$$ respectively.

We can see that innovators will only choose to produce an innovation if they
stand to make a profit: in other words only when $$B < p_H H$$.

Here, there are two factors that affect innovation: price and market size.

**Price effect**: the larger the price of the good $$p_H$$, the more profit
innovators stand to make.

**Market size effect**: The more high- or low- skilled workers $$H$$, the more
profit innovators stand to make.

There is a further equilibrium condition. At equilibrium, the marginal benefit
of providing both high- and low- skilled technologies must be equal. Otherwise,
people would start developing more technologies of the other one to make more
profit.

This gives us the following condition:

$$p_h H = p_l L$$

By consumer optimisation,

$$\frac{p_H}{p_L} = \frac{MU_H}{MU_L}$$

After all, consider the case where LHS > RHS. Then, it would be a Pareto improvement to
substitute 1 unit of H for 1 unit of L.

But we know here that the production and utility functions are the same! Thus,
$$MU_H == MPH$$ and $$MU_L = MPL$$.

Therefore, we can reuse the previous result

$$\frac{p_H}{p_L} = \left [ \frac{A_H H}{A_L L} \right ] ^{\rho-1}$$

Substituting in the equilibrium condition, and replacing $$\sigma = 1/(1- \rho)$$
gives us

$$\frac{A_h}{A_l} = \left(\frac{H}{L}\right)^ {\sigma - 1}$$

This gives the result that when $$\sigma > 1$$, more technology will be
produced for the higher-skilled worker if H/L increases (i.e. the market size
effect dominates). In other words --- **directed technical progress**! This is
something we previously assumed in the exogenous case, but now we have shown
how directed technical progress is in fact caused by a large supply of
high-skilled workers.

Okay, we've shown that if $$\sigma > 1$$, when $$H \uparrow$$,
$$\frac{A_H}{A_L} \uparrow$$. But what about the skill premium?

\begin{equation}
\omega \equiv \frac{w_H}{w_L} = \left(\frac{A_H}{A_L}\right)^\rho \left(\frac{H}{L}\right)^{-(1-\rho)}
\end{equation}

Substituting the result we got for $$\frac{A_h}{A_l}$$ into the equation, as well as the fact that $$\sigma \equiv \frac{1}{1-\rho}$$, we obtain

$$ = \left(\frac{H}{L}\right)^{\sigma-2} $$

This result tells us that if $$\sigma > 2$$, then an increase in relative
supply of high-skilled workers increases the skill premium. Note that this is
different from the exogenous model. In the exogenous model, as long as $$\sigma > 1$$
both the level of skill-biased technology and the skill premium increase.
In the endogenous model, if $$1 < \sigma < 2$$ the level of technology does
increase, but the skill premium actually decreases (the increase in supply
outweighs the increase in technology).

![](/img/acemoglu_explained/acemoglu_endogenous_sigma_1_2.png)
![](/img/acemoglu_explained/acemoglu_endogenous_sigma_2.png)

| Level of $$\sigma$$ | Exogenous model                        | Endogenous model                       |
| ------------------- | -------------------------------------- | -------------------------------------- |
| $$0 < \sigma < 1$$  | $$\omega \downarrow$$ $$A_L \uparrow$$ | $$\omega \downarrow$$ $$A_L \uparrow$$ |
| $$1 < \sigma < 2$$  | $$\omega \uparrow$$ $$A_H \uparrow$$   | $$\omega \downarrow$$ $$A_H \uparrow$$ |
| $$\sigma > 2 $$     | $$\omega \uparrow$$ $$A_H \uparrow$$   | $$\omega \uparrow$$ $$A_H \uparrow$$   |

## Comparison to other models

In the Schumpeter-Solow case, demand for innovation is gotten from $$\hat{k}$$,
level of capital per effective labour unit. The greater $$\hat{k}$$ is, the
more profit innovators stand to make.

TODO

## Conclusion

TODO
