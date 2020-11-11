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

and so I will be redacting
i) the questions that were asked
ii) my specific post-mortem thoughts on how I approached/tackled the questions,
iii) some of the personal thoughts that Hongyi shared with me.

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

On 23rd of September I received this email from Russell:

> Hi Zheng Hong,
>
> Thanks for taking the test. We are happy with the outcome and would like to
> invite you to a technical interview on Google Meet with two of our engineers. 
> 
> What is your availability for a 2h interview like over the next two weeks?
> 
> In preparation for the interview, you may find the following document helpful:
> 
> https://docs.google.com/document/d/1Y0X2hatsN-kbzVu9ICVJyeB67V1PyrqtOV7Cg94Btc4

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

I wrote a very long document preparing for the resume deep dive
(over 40 pages).
For every project mentioned in my resume I wrote the following: 

1. Brief background/motivation
2. What it was
3. Why it was impressive (relevance/impact of the project)
4. What the architecture was:
  - diagram
5. Interesting technical decisions I made
6. Technical challenges I experienced

It was actually pretty hard to do this because I had forgotten a lot of the
details of the projects, particularly the technical details/challenges.
I still remembered the big picture but not the debugging/small decisions.

Additionally I prepared a self-introduction, gathered questions to ask,
and also did several more mock interviews.

### How the second round went

It started off with the resume deep dive, and I absolutely bombed it.
Here are my post-mortem thoughts which I wrote immediately after the interview:

I think I bombed this section. I think I chose the wrong topic to talk about,
which was because I had prepared it with Joshua the night before.
So everything seemed to go OK when I explained the schema
and demonstrated how it could be used to represent any arbitrary analogue
board state.

But they didn't seem to be impressed.
First they asked "How do you encode the rules?"
I said it was a deliberate engineering decision _not_ to encode the rules
because this allows us to represent all games. If you encode rules
you can't represent games like e.g. Hearthstone.
Also, it's meant to evoke the analogue feel when players enforce the rules themselves.
But I don't think they were convinced---or rather, it's not as technically
impressive if you don't encode the rules.
I felt that they weren't impressed with the schema.

I also told them about the fact that I decided to handle promises in the
"wrong" way: making the init function blocking
instead before allowing any other methods to be called.
The point is that we were able to isolate the Promise object into one singular
method call (boardGameInit) or something. The disadvantage is an optimisation
loss because it now blocks. But what we gain as a result is that the rest of
our codespace can be synchronous and we don’t have to worry about promise
handling in the rest of our codebase which simplifies development greatly — not
polluting the codebase.

"Can we see some code?"
I showed them the init function.
They asked me whether there was any other way to implement it,
I said you could do `Promise.all().then(() => whatever)`. They asked me
what's the difference between using `async` and using `Promse.all()`.
I replied that it was basically making it look nicer and avoiding
promise chaining.
But I don't think that was a very good answer.

There was a period of silence and I could tell that they were trying to get
_some_ positive signal out of me. I was feeling pretty deflated at this point.
I wanted to tell them about another project
but I would have to tell them the context of the project
and we wouldn't have time for that.
They asked for the most challenging bug that I faced
and I told them about the rather esoteric bug
with `os.fstat` and `os.stat` being affected by `os.seek`
(which is not what the top answer on SO said---the answer was wrong).
But I don't think this was that impressive either.

I think that my signal wasn't strong enough here.

Then we moved on to the technical interview.

**redacted my thoughts on the technical interview**

On hindsight, these questions were quite open-ended
and not like the questions I practiced for on Leetcode.
It was a bit sad because I feel like I could do better.
Overall, though, I think I came up with an OK solution.
It wasn't asymptotically optimal but the solution was quite clean
and I correctly identified a time-space complexity tradeoff.

After the technical interview we had a Q&A section.
I asked questions I wanted to know the answer to:

1. What do you wish you had known about OGP before you joined?
2. What do you like about OGP and what don't you like about OGP?
3. How does OGP decide on what projects to work on?

Chin Ying and Nikhil both independently gave the same answer,
which was quite funny.
Both pointed to the autonomy as the best part of OGP
and the worst part as the bureaucracy involved with the civil service.
Nikhil also said that he feels like the team is growing a bit too fast
in the sense that he doesn't get to know the new members of the team as well.

Russell answered the question how OGP decides what projects to work on.
He said it's a lot about requirement gathering from government.
The main difference between OGP and the rest of GovTech is not---as I previously thought---
building products for the citizen vs. building products for civil service,
but rather about the process: it's more of startup culture, iterating quickly,
having annual monthly hackathons to iterate and ideate, rather than a more
requirements-driven development process.

I thought that I bombed and I couldn't bring myself
to be positive at the end---I must have given a bad impression.
I should have tried to stay positive and wished them a good day.

I would give myself a 4/10 for the resume deep dive and
a 6/10 or 7/10 for both technical interviews.
I would definitely not consider either technical interview "Strong Hire":
only a "Weak Hire" signal.
And I would not hire me based on the resume deep dive.

I don't want to be fully negative, however. I think I did an decent-to-good job
asking for clarification, communicating my solution, and
communicating when I got stuck. There was no need for a trace here
because it didn't require much complicated algorithm.
And I think I performed overall OK with the speed of the technical interview,
even though I didn't finish all the parts.

Overall, I don't fancy my chances: I think it's more likely that I don't
get moved to the next round than that I do.
I would calibrate my posterior as 30% that I get moved to the final round.

## The final round

I was really disappointed about my performance and couldn't sleep well for
one or two nights afterwards. I kept thinking about what I should have said
and what I should have done and I just felt very bad.
I honestly thought I bombed it for sure.

Russell said that he would get me a reply by Friday. Friday came and went with
still no reply, and I was really antsy.

I followed up with him on the Monday after (after even more sleepless nights)
and was very, very pleased to get the following reply on the 13th of October:

> Hi Zheng Hong,
> 
> I'm pleased to inform you that we'd like to proceed you to the next round of
> interview:- a 1-hour interview with the Director of Open Government Products. 
> 
> This interview will not require any hands-on coding from you, but instead will
> focus on your engineering experiences and interests. Specifically, you will be
> asked to discuss in detail work that you've done before, and to articulate
> engineering decisions and trade-offs you've made in these experiences. We are
> assessing for how you think and problem-solve engineering problems and
> situations, as well as your interests in joining the team.
> 
> What's your availability like over the next two weeks, for a one-hour video
> interview with Director of OGP?
> 
> Regards,
> 
> Russell Chan

### What it was about

### Preparing for the final round

Didn't prepare as much as I would have liked, 
because my momentum was honestly flagging at that point,
and I felt that I had already written a lot of

Also in general I find it more difficult to prepare for nontechnical interviews.
When I was preparing for a technical interview, 

So nothing really happened until the day before, where I started thinking
about all the technical decisions I had made in the past.
I examined all the individual technical
and engineering decisions that I have made in the past and I wondered to myself:
_why_ did I make the decisions that I made? What did I consider,
and how did I come to a conclusion?
And after some thought, I concluded that I tend to view any technical decision
as a balancing act between many competing factors.

I've come up with a taxonomy of trade-offs, split into two dyads of trios:
I have never actively _used_ this taxonomy,
but I definitely weigh these in my mind
even if they never bubbled up to the level of formal analysis.
But I'll take it for a test drive in my future engineering decisions
to see if this formalism is helpful.

By no means is this taxonomy universal or exhaustive:
it just happens to be the factors that _I've_ considered when building the
kind of software that I build.

## Developer-facing

1. Complexity: how hard is the codebase to understand/build/reason
   about? In general, complexity is king: complexity has knock-on effects
   on both maintainability and velocity.
2. Maintainability: how hard is it to maintain, extend, or modify the
   codebase over a period of time?
3. Velocity: how fast can you write and ship your code?

## User-facing

1. Performance: how quickly does the code run?
2. Robustness: how well does the codebase handle unexpected behaviour
   (e.g. packet drops, user clicks Submit twice)? how well does your code scale?
3. User-friendliness: how intuitive are your interfaces/abstractions?

And I thought a lot about how each of the technical decisions I made fit into
this framework. I might make a blog post about it sometime, but
in the interview Hongyi didn't seem to like it much.
I also prepared several behaviourals like why I wanted to join OGP.

### How the final round went

Overall, I think this interview went reasonably well.
I would give it a 70% probability that I get accepted.
I really enjoyed this interview even though it was quite hard,
I really vibed with Hongyi and I appreciated his
piercing questions,
his frankness,
and his willingness to go over time in the interview for me.

Here is the postmortem I wrote: 

#### Questions Hongyi asked

##### Tell me about yourself

I recited my prepared spiel:

> I'm Zhenghong and I've just graduated from the University of Oxford
> where I read Philosophy, Politics, and Economics. Despite what my degree
> might suggest, I've always been incredibly interested in computer
> science and so I've done courses in algos and DS, computer architecture,
> functional programming and so on.

> I like SWE a lot because I like to design and build things with
> measurable impact, and I love delighting my users. (It also scratches my
> creative itch).

> Previously, I built an Electron app for a civil engineering firm which
> streamlined their building inspection process a lot. It saved about 300
> engineer-hours a month. I found this very rewarding because I could see
> directly how my app improved their workflow and delighted the engineers.

> In a previous internship I designed and built an automated SMS sender.
> It uses Bayesian statistics and unique tracking URLs to send optimal
> reminder messages. Seeing the number of active users increase day-by-day
> was really wonderful.

> I always have a backlog of new ideas and love building side projects.
> I'm currently building a real-time, multiplayer board game engine with
> TypeScript, React, and ExpressJS, and am trying to write and sell the
> best puzzle books that money can buy on Amazon.

> I think the work OGP does aligns very well with my own desire to delight
> users and build software that matters.

##### Which project do you want to talk about?

launched into my prepared spiel my taxonomy and all this.
I mentioned that complexity is king, but sometimes you have to add complexity
in order to get some features you want.
I gave some examples, including my choice to use React in my army CRUD app
(bad example of adding complexity with no gain),
and my choice to rewrite our codebase in TypeScript for my board game project
(good example of adding complexity for gains in maintainability).

He listened politely and said:

##### Okay so I understand the theoretical part of software engineering, can we talk about a project you actually did?

Went back and forth a bit where I explained that I don't really remember the
specifics of the technical decisions that I made a long time ago, the board
game engine is relatively fresher in my mind, but when I spoke with Nikhil and
Chin Ying about it, they weren't very impressed with it.

##### Okay, so since you've talked about the board game engine with Nikhil and Chin Ying, tell me about the work you've done in a commercial context.

So I told him about the Bayesian SMS sender. I gave him the background with
Inzura being an insurtech company, us having signed a contract with Thailand's
second largest insurer, etc etc... and so I built a system to send optimal SMSes
to users.

I then walked through the architecture using the two diagrams that I had prepared:
[here](https://lieuzhenghong.com/img/sms_pipeloop/sms_pipeloop_0.png)
and
[here](https://lieuzhenghong.com/img/sms_pipeloop/sms_pipeloop_1.png)
I asked if everything made sense and he said that it did, and he asked:

##### Can you explain this multi-armed bandit?

He didn't know what a multi-armed bandit was so I explained what it was:
I gave the example of a row of slot machines and you need to find the best-paying one,
and mentioned the explore-exploit tradeoff.

He asked some good questions here. First he asked about minimising uncertainty,
and I said that's at the core of the explore-exploit tradeoff.
I said that if you were a scientist/psychologist/economist what you want
is to minimise the uncertainty of which arm is best, and so you would divide
the SMSes equally to do so.
But since we were doing business here. we want to strike a balance between
the two extremes of dividing the SMSes equally vs exploiting a local optimum
greedily losing out on gains.
I think I explained this quite well and he got it.

##### Does your MAB code do the message sending automatically?

Didn't really understand what he meant by "automatically", there were a couple of
clarifying questions and attempts before I got what he was trying to ask.
So basically he was asking if my code decides how many SMSes of each type to send
automatically, or I have to manually tell the code to send X of this type,
Y of that type, etc. I said that it all happens magically/mathematically:
I tell the code to send 1,000 SMSes and it will calculate the magic numbers to send
X of this type, Y of that type, etc.

##### How does your code decide what to send/how much of each message to send?

I asked him to refer to the series of graphs I drew on the page
[here](https://lieuzhenghong.com/2019/09/16/using-thompson-sampling-to-optimise-SMS-effectiveness/),
and explained it to him. It was OK overall, I think there was a bit of confusion
when I talked about sampling the curves, but he got it in the end.
I feel like I should have impressed upon him more how magical this sampling solution
was, but oh well.

##### Okay so you've gone through the architecture and I get that, but were there any specific difficult technical decisions that you had to make? What was the hardest part of this project?

I said that the hardest part of this project was building all the disparate
parts and keeping in mind how they fit together, but he interrupted me and said---

##### Yes, yes, I get the general difficulty of software engineering, but were there any specific technical difficulties that you encountered?

I can't remember what answer I gave to this but it wasn't very good.
He prompted me a bit:

##### Did you run into any issues? Like for instance if the API was rate limited, or if you had to do the database calls a certain way?

Yes, now that he mentioned it, the API was indeed rate-limited.
I called the Ant API folks to ask if they could raise the limits
(they couldn't)
but the way I solved it was simply to sleep 0.5 seconds between POST requests.
But I said this was not that exciting.

This was the only part I smoked him a bit: I talked about batching the queries
to reduce the number of database calls---but I didn't really explain this well---
and also sorting the indices since I knew that the user IDs were indexed,
and I said "I think it's called a cache hit". This was true, but only for
a different project. This ended a bit lamely, he didn't ask any follow up questions.

I could have communicated my difficulty better by saying something along these lines:
"I understand what you're trying to ask, and what signal you're trying to get from me,
but unfortunately I can't remember the specific technical decisions I made
in this project. If you prompt me then it will come to mind but otherwise I tend
to forget these small roadblocks once I solve them because they seem trivial
in hindsight."

##### Would you do anything differently in this project?

I said that if I had more time, I would have fixed two things:

1. I spoke about how much of a bodge the Nginx server log-`grepping` was,
   it was fragile, etc. I said that someone suggested that I use a AWS Lambda
   function to update the SQL database on GET request.
   This would certainly have been more robust, more scalable, etc,
   but of course this would mean that I had to learn AWS Lambda and set up a gateway
   and all that and this was time I did not have.
2. Dry run CLI: I accidentally sent the same batch of SMSes twice to the same users
   because I didn't have a proper CLI, I just commented out the line of code in
   the main function that actually sent the SMSes. One time I forgot to
   comment it out and
   So I should have done `argparse` and added a `actually-send` flag
   to prevent such a mistake.

##### Okay so I get that you would have done things differently had you had more time. Like it's understandable that you wouldn't have a proper CLI since you had no time. But suppose I gave you the same amount of time to build this same project again. What would you do differently?

I thought very long about this question and really blanked.
Nothing I thought of seemed good: I said
"I would like to say I would write tests... but that takes time.
Do I need a DB? Can I get rid of it? ... probably not... I don't know,
I don't see how my architecture can be made even simpler".

So he started to prompt me:

##### So there are two parts of your architecture, correct?

I said, yes --- essentially, there's the automated SMS sending bit,
and there's the Bayesian SMS tracker business that maximises the SMS effectiveness.

##### What were the results of your three different SMSes?

I said that it was a null finding: all three types of SMSes were equally effective.
I said that this contradicted my priors which were informed by behavioural economics
literature --- I expected the loss-aversive SMS to do better.

##### How would you be able to find out if the SMSes were better or worse than each other?

Now I finally understood what he was getting at.
He was trying to make the following point: since the automated-SMS-sending
part is very easy, and the Bayesian stuff is hard, you should first try
and find out whether you even _need_ the Bayesian stuff.
So I said, yes actually you're right, we could first send out a thousand SMSes or so
to get initial priors to see if we needed it (but see my note after this para).
I said that I wanted to push back against this suggestion a little bit,
because while I agreed that he was right,
but if I had done that, my CEO would not have been able to tell the Thai CEO
that we were using "advanced statistical techniques" to "maximise user uplift"
(I used my hands to do air quotes). He laughed and said, OK, point taken.

I think that was the end of the resume deep dive, at this point it was 1650
(ten minutes until the scheduled end of the interview).
He said that he's conscious of time but he's willing to go over if I was too.
I said yes definitely. I took this as a good sign.

##### Why don't you like your job at IMDA?

This was the easiest question for me because I have been thinking about it a lot!

- I can see the writing on the wall: they've pigeonholed me as a policy scholar
  and will want to rotate me around
- Incorrect Job title symptomatic of management-focused culture
- Bloated organisation with few developers
- Bad development culture (waterfall, requirement-gathering by "strategy teams")

And also I said:

> There are some not-very-flattering questions that occasionally come to my mind
> when working at IMDA:
>
> - Why are we doing this?
> - Is this project actually useful for Singapore, or is it just sexy
>   with a lot of buzzwords?
> - Are we doing this to meet some Senior Director's KPI/make them look
>   good?
>   To be clear, I do
>   believe that the people up top in IMDA care a lot too: it's just that
>   the message may have gotten lost in transit after passing through the
>   Byzantine civil service apparatus.

I think he liked this answer because he agreed with everything I said and
it echoed his experience some years ago.

##### What are you doing to change it?

This was quite a curveball question! Was not expecting this.

I told him the first day of work I spoke to my immediate superior and asked him
whether or not we were maximising our impact working on this autonomous robot
project rather than doing something like form OCR which would save a lot of
hours doing data entry for many SMEs.
I also said that I'm trying to push to work on some projects but I have no idea
how this could be done.

I actually flipped the question on him and asked him what he would do if he
were in my situation. He actually gave a pretty good answer, a "four-step approach"
which he said is what he did himself when he was a scholar at IDA.

1. Demonstrate competence by doing the nonsense projects much quicker than they expect
2. Carve out space for yourself: "I can do your stupid project really quickly,
   can I have some time to do an alternative project?"
3. Start personal projects and demonstrate competence
4. Use that demonstrated competence to spin off your own team

He mentioned that don't think of the bureaucracy as an immovable object,
but rather a puzzle box that can be undone with the right tugs and pulls in the
right places. You don't need to rotate if your supervisor loves you, for instance.

I said that all sounds good, but why would I rather push hard against the cogs
of the bureaucracy when I can join an organisation that empowers and supports
me to do alternative projects?

This question was quite interesting!
On analysis,
I think he's trying to find out whether I am a typical sinkie
who will just give up when faced with the bureaucracy.
He's probably looking for people with low Agreeableness.
So I think that the fact I challenged my superior on the first day probably
reflected well on me.

I should have linked to my work on Inspector's Gadget as an idea of how some
low-hanging fruit projects can improve the efficiency of private industry.

##### Why do you want to work at OGP?

Thank god Celine nudged me to prepare this question!
I very quickly ran through the four pre-prepared reasons:

> The more I read about and hear about OGP from the people I've spoken
> with and interviewed with, the more I want to be part of the team.
>
> I want to be on a team working on meaningful projects,
> I want to be on a team that delights users rather than phoning it in

(and here I mentioned XY problems and OGP's work on JARVIS),

> I appreciate the autonomy and the fact that engineers are expected to push for change,
> I appreciate the flat hierarchy and I believe in you.

On the last point, I referenced what I said about IMDA, and said that in contrast,

> From everything that I've seen and heard, I believe that you really care
> about benefiting Singapore and don't care about more venal
> considerations like looking good/getting promoted.

I think this was a good answer.

##### If I took you on at OGP and gave you latitude, what sort of projects would you do?

I said that I don't know because I don't know much about the public service
and would need to do research/look around at what OGP is doing before having an idea
myself.

##### Sure, I get that, but what are some suggestions you have anyway?

I told him about my frustrations with Data.gov.sg, the difficulty with getting
updated EMA data when I wanted it this year, and I said I didn't know if the problem
was solvable but I would like it to be solved.

I also said that I didn't know if government was still using paper forms
despite FormSG and maybe we could prototype the OCR thingy I mentioned earlier.

These are pretty lame suggestions but I had already told him that I didn't
know because I would need to do some research before having ideas,
so I think it's acceptable.

In hindsight I should have prepared for this question.

Finally he asked if I had any questions for him, and I had prepared a couple:

#### Questions I asked
##### _Where do you see yourself and OGP in five years? Will OGP survive your departure?_

lieu, [27.10.20 17:13]
Three yaers from now stilla t OGP, five years after

lieu, [27.10.20 17:14]
OGP is in a pretty strong position, key infrastructure in place, forms, website, link-sharing etc

lieu, [27.10.20 17:14]
Five years from now all of the IT teams will be obsolete

lieu, [27.10.20 17:15]
150-250 people

lieu, [27.10.20 17:15]
working websites, digital forms, payments, etc

lieu, [27.10.20 17:15]
10 years —- singapore as a model of what modern government looks like

lieu, [27.10.20 17:17]
the civil service stopped enforcing values as an exclusionary criteria

lieu, [27.10.20 17:20]
kids in school —- why can't they view materials online? why can't compare prices across hospitals? can't compare prices across HDB flats?
if you're trying to find data on scammers, police can't understand whatsapp

##### _OGP is moving fast, breaking things, scooping scholars --- are you stepping on anyone's toes? How do you deal with that?_

lieu, [27.10.20 17:23]
Most of the IT teams stonewall OGP because OGP are moving them out of the job

lieu, [27.10.20 17:23]
If they were doing anything good they would not be in that scenario

lieu, [27.10.20 17:26]
the one thing I can do is that I am willing to lose —- you have outside options

lieu, [27.10.20 17:30]
Look at bureaucracy as a puzzle box , as something you can move in the right way


I think I could have prepared a bit better.
I think I should have expected the question of what sort of projects
I would like to do at OGP, or paused a bit before answering this question.
But overall I explained most questions well,
I was quite well prepared for most of the questions he asked,
and I'm quite happy with the things that I said off-the-cuff.

I remained positive throughout the interview
(it was easier because I thought it was going well),
I was able to admit when I didn't know something,
I made sure to check understanding ("does that make sense") when explaining things,
and I didn't lie or smoke him.

Something I could have done better is to pause for a bit before answering questions,
and try to speak slowly. I think he probably has a higher tolerance for speaking
quickly than most (he seems pretty smart) but I should pause/slow down for impact.

## Results

I was really happy the next morning to receive the following email:

> Hey Zheng Hong,
> 
> Congratulations! We'd be happy to extend an offer for you to join the team in
> a Software Engineer role! Good job at the various interviews :) Do you have
> time this Friday or next week to chat for half an hour? I share more in terms
> of feedback, the offer, and we can discuss what next steps and your
> considerations could look like.
> 
> Regards,
> 
> Russell

Funnily enough, I was actually happier receiving the second email
because I thought I bombed it, whereas I was kind-of expecting to get the offer
because I thought the interview went well.

## Feedback I got

initiative => strong, working on all sorts of stuff, blog it out, outline my
thoughts, interview prep ability => resume deep dive with nikhil and chinying
not that impressive (question mark), but Hong thought the bayesian SMS was deep
enough (dispelled doubts about technical depth)

CHin ying noted familiar with complexity, made it about halfway trhough the
question, i do plan and talk about high level approaches and considerations, but
coding ended up a bit chaotic. Need to work on explaining the code (but great I
explained it before i started writing). He said I had more experience i would be
able to handle the edge cases

Nikhil's question: went a lot more smoothly, got stuck but managed to get
unstuck which is good, he said I could code fast, i knew what i could do to
refactor, i knew algo complexity, decent,

More generally on communication: I'm a good communicator especially on the
technical interview, Everyone noted I was able to speak clearly and well, BUT i
do tend to talk extensively/waffle at the theoretical or high level, and it
takes some time to get to the actual nuts and bolts <— this was hongyi's
feedback. Overall strong communicator

My personal suggestion (from Russell) —> great at documenting and preparing, but
don't be compelled to say eveyrthing you prepare.

especially for someone who comes from a nontraditional background, I have a good
technical depth and side projects

"work is very good, nontrivial side-projects, especially for someone non
traditional , but technical depth not as good as the best engineer candidates" —
verbatim quote from hongyi

strong initiative —> good fit for team

strong communicator (only minor tuning needed)

strong POTENTIAL for technical depth

## On the whole, what did I do well?

I prepared a lot (~60 hours!) and it paid off: not just in the fact
that I got a lot better at writing LC-style code very quickly,
but also that I prepared good answers to behaviourals/explanations to my projects.
This was noticed by them.

## On the whole, what could I have done better?

I need to take note of the "small" technical decisions I make in the future
so I don't forget them and can demonstrate technical depth. 
In general for projects I did a few years ago
I will have forgotten all the details but the architecture/big picture stuff
sticks.

Stay positive even when I think I bomb the interview!

## Closing thoughts

I really enjoyed the interview process, fraught as it was,
and my coding skills improved a lot.
I really appreciated OGP's transparency and honesty which was a real
breath of fresh air.
And they really took great pains to demystify the interview process
as much as possible

## Acknowledgements

- Kevan, for linking me up with Russell in the first place
- Russell, for being wonderful throughout the whole process
- Celine (gave me the push to start preparing the behaviourals)
- Joshua (for talking through the board game engine project with me)
- Joel (BIG thanks to him for introducing me to Kevan)
- Nick (for mock interviewing me and for giving me confidence)
- Mike (we did two mocks together)
- Wei Heng, who did a mock with me and also pushed me to practice more
  
