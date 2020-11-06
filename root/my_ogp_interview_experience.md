---
title: My experience interviewing for OGP
date: 2020-11-05
layout: base
tags:
    - public
    - diary
---

<div class = "toc">

[[toc]]

</div>

## Introduction

I thought I'd share the process of what interviewing with OGP was like,
and how I prepared for it.
This is mainly for posterity, 
but it might also help others who are thinking of applying to OGP too.

I wrote post-mortems just after the interview 
talking about how I thought I did,
and it's very interesting to compare how I _thought_
I did to the feedback I got 
(ergo how the _interviewers_ thought I did).

Overall, I really enjoyed the interview process, 
(or as much as it's possible to enjoy interviews, anyway)
thanks in large to how well they were conducted.
I thought that I did very well
for it being my second-ever proper technical interview,
and I prepared very well for it.

I've clarified with Russell (OGP HR) what I am or am not allowed to say:

> my general principle which I'd say to OGP officers (and I counting you in that
> fold by extension) is go ahead and share freely, but dont go and share
> something that would give any reader an unfair advantage into the actual
> hiring process 
>
> e.g. the stuff we tell u about what we're looking for - yeah you
> can go ahead and share that too. 
>
> but the actual questions we use and ask, please don't

and so I will be 
i) redacting the questions that were asked, and 
ii) redacting my specific post-mortem thoughts on how I approached/tackled the questions.

## An overview of the interview process

The interview with OGP consisted of three rounds:

1. an offsite Codility assessment asking ~easy-medium Leetcode-style questions;
2. an onsite with OGP's SWEs doing a resume deep dive + two technical questions;
3. a technical resume deep-dive and several behavioural questions with 
   the Director of OGP, Li Hongyi.

I started talking to Russell on the 24th of August and received the offer on the
28th of October. The timeline was as follows:

- 24th August: spoke with Russell
- 18th September: asked for the Codility assessment
- 23rd September: passed the first round
- 7th October: did the second round
- 13th October: passed the second round
- 27th October: did the third round
- 28th October: got the offer!

It could have been sooner but I purposely spaced the interviews out
so that I could have time to prepare for them (more on this later).

## The first round

### What it was about

>  Thank you for your interest in applying for an internship at Open Government
>  Products. As part of our initial evaluation, we would like you to complete
>  the following coding test within the next 14 days. I will send you the
>  Codility test link in a separate email. After clicking the link you will be
>  able to practice with a demo or start the test.
> 
> This requires up to 100 minutes of uninterrupted time, so do set aside time
> for your attempt. After submitting all your solutions you will be presented
> with your score for each task, so that you can find out how you performed.
> Your performance will be taken together with your CV in considering you for
> further interviews. Be assured that we will not look at the test score alone,
> but will be looking out for how you write code and go about tackling the
> problem.

The first round was an offsite interview on the Codility platform.
Russell told me that the questions would be quite easy and were mainly
to filter out people who could not code. 
And they did indeed turn out to be easy-medium Leetcode-style questions.

### Preparing for the first round

I spent the most time preparing for this round.
Overall, I spent around 40 hours doing ~60 questions over 1 month,
most of which were LC Mediums,
and about 20 hours doing mock interviews,
for a total time expenditure of ~60 hours.

I did ten mock interviews in this order: 
one with Kuan, 
one using interviewing.io,
one with Joel, 
four using Pramp,
two extra with Mike,
and one with Nick. 

Firstly I started doing questions from Q1 on LC --- this is a bad idea,
then I started doing the ones that were in LC's list of 
"100 Top Interview Questions",
then I worked through Yangshun's list. 
It started off very painful and slow,
and I was honestly a very rubbish coder.
Rather early on in the process I did an interview with Kuan
and got absolutely wrecked, not being able to solve the problem in time at all.
I felt really bad and this spurred me on to work harder.

Thankfully I improved very quickly 
(much quicker than I thought, actually).
After ~30 problems I got relatively decent.
In particular, I got quite good at doing DFS/BFS problems
after doing just a couple of them.
I did a `interviewing.io` mock interview around this time,
very unconfident after my poor performance with Kuan,
and was surprised that I could actually solve the problem
given to me very quickly. The feedback I got that I was actually
quite fast and competent compared to other interviewees! 
This was encouraging.

Eventually I got fast enough that doing the LC problems
became (mostly) quite fun and easy,
and I could bang out several in a day.
Once I got reasonably good at LC problems, 
I started doing Pramp interviews and there I was given
positive feedback as well: of the four interviews I did,
I was always able to come up with the solution before the time limit
(The questions did tend to be on the easy side, to be fair),
and all interviewers gave feedback that I was able to solve the problem
quickly.

**The Pramp and interviewing.io practices were REALLY helpful.**
They are not just helpful in mocking the interview conditions
(which is something that you would expect),
but also helpful because you can see other people work through
and explain the problem, and I learned/stole the best techniques 
of presenting my answers from the other interviewees.
I learned so much.
Mike's method of "tracing" the execution of the program before
running it was honestly genius.
The mock interviews also surfaced my weaknesses/bad habits.
I was getting repeated feedback that i) I was going too fast
and ii) I was too eager to jump into the problem and code without
talking through it first, which often got the interviewer lost,
e.g.:

> You can move very quickly. Make sure the interviewer is keeping up.

After several attempts I was able to improve on this
and in the second round (spoiler) Nikhil and Chin Ying noted
that I was good at communicating how I would go about solving the problem.

In any case, after the Pramp interviews (22 Sep) 
I felt reasonably confident that I would be able to solve most easy-medium
LC-style questions. 
So I decided to pull the trigger and request the Codility link.

### How the first round went

The first round went great: I can't talk about the problems,
but I was able to write nice, elegant, optimal (algorithmically speaking) 
solutions for both of them.
I would say that problem 1 was an LC Medium and problem 2 an LC Easy
in difficulty.
Codility gives you a score immediately after you submit the solutions;
I submitted the solutions and got full marks and I knew that I would
get into the second round.
    
## The second round

### What it was about

#### Resume Deep Dive

> We will be looking at your resume and getting you to share more about what you
> have worked on in the past. We’re interested in depth instead of breadth, so
> err on the side of specificity. Be prepared to share technical details about
> what you’ve worked on, including drawing diagrams on the whiteboard if
> necessary (for on-site interviews).
> 
> In particular, we’re trying to answer the following questions about you:
> 
> - What did you do?
> - How is it impressive?
> - How did you do it?
> 
> In addition, we’re very interested in finding out how you think and how you
> work, so it would be useful to come prepared to explain any interesting
> engineering decisions that you had to make in the course of your work.

#### Coding Test

> We ask messy, open-ended tasks, i.e. not ones that are predicated on
> algorithm, data structure knowledge, but rather technical assessments which
> have multiple solutions by design. This is so that you don’t have to have
> studied any particular topic to put together a good solution, but rather so
> that we get a deeper sense as to how you write code to work and iterate toward
> a good solution.

### Preparing for the second round

I wrote a very long document preparing for the resume deep dive.

### How the second round went

## The final round

### What it was about

### Preparing for the final round

### How the final round went

## Results

## Feedback I got

initiative => strong, working on all sorts of stuff, blog it out, outline my thoughts, interview prep
ability => resume deep dive with nikhil and chinying not that impressive (question mark), but Hong thought the bayesian SMS was deep enough (dispelled doubts about technical depth)

CHin ying noted familiar with complexity, made it about halfway trhough the question, i do plan and talk about high level approaches and considerations, but coding ended up a bit chaotic. Need to work on explaining the code (but great I explained it before i started writing). He said I had more experience i would be able to handle the edge cases

Nikhil's question: went a lot more smoothly, got stuck but managed to get unstuck which is good, he said I could code fast, i knew what i could do to refactor, i knew algo complexity, decent,

More generally on communication: I'm a good communicator especially on the technical interview, Everyone noted I was able to speak clearly and well, BUT i do tend to talk extensively/waffle at the theoretical or high level, and it takes some time to get to the actual nuts and bolts <— this was hongyi's feedback. Overall strong communicator

My personal suggestion (from Russell) —> great at documenting and preparing, but don't be compelled to say eveyrthing you prepare.

especially for someone who comes from a nontraditional background, I have a good technical depth and side projects

"work is very good, nontrivial side-projects, especially for someone non traditional , but technical depth not as good as the best engineer candidates" — verbatim quote from hongyi

strong initiative —> good fit for team

strong communicator (only minor tuning needed)

strong POTENTIAL for technical depth

## On the whole, what did I do well?

## On the whole, what could I have done better?

## Closing thoughts


## Acknowledgements

- Kevan, for linking me up with Russell in the first place
- Russell, for being wonderful throughout the whole process
- Celine (gave me the push to start preparing the behaviourals)
- Joshua (for talking through the board game engine project with me)
- Joel (BIG thanks to him)
- Nick (for mock interviewing me and for giving me confidence)
- Mike (we did two mocks together)
- Wei Heng, who did a mock with me and also pushed me to practice more
  
