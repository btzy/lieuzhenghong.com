---
layout: base
date: 2017-09-24
title: "Sep 2017 report"
tags:
  - progress report
  - monthly report
  - milestone
  - private
  - diary
---

This post marks the end of an era. The chrysalid years are over, and I fly to
Heathrow to begin my new life as a student tomorrow night.

I am wary, yet cautiously optimistic about the new academic demands Oxford will
soon impose on me. I have always been able to coast on by in my education,
accepting mediocre grades in return for not studying at all (being a supremely
lazy person). I won't accept mediocrity any more and I look forward to studying
as hard as I can and getting the best grades my brain (and Fate) will allow.

Since my [last post]({{ '/_posts/2017-08-22-life-report-aug-2017' | url }}) I have done the following:

- Embarked on my CS study plan
- Went to OUMSSA orientation camp

## CS self-study plan and milestone goals

In my previous post I mentioned that I have a "new and very ambitious goal": to
be accepted into Georgia Tech's [Online Master of Science Computer Science
(OMSCS)](http://www.omscs.gatech.edu/) in three years' time.

This is a good goal but I realise that it's useful to signpost the endgoal with
various milestones along the way. To be accepted by OMSCS is after
all a very lagging indicator.

That's why I **aim to do at least one technology internship over the
next two summers**.

A "technology internship" is defined as an internship in which I am expected
to program as part of my job scope. It would of course be best to intern at a
Big 5 company. Failing that, I wouldn't mind interning either at a bank
(perhaps doing some financial analysis--make use of my PPE knowledge), a
"normal" tech company, a startup, GovTech, or working under a professor.

I will have to start looking for internships at the end of Michaelmas term this
December. To that end, I think I will have to bring forward my data science and
data analytics learning.

There are a couple of programs out there:

- Udacity's [Data Analyst Nanodegree](https://
  www.udacity.com/course/data-analyst-nanodegree--nd002)
- DataCamp's [Data Scientist with Python](https://www.datacamp.com/tracks/data-scientist-with-python), [Data Scientist with
  R](https://www.datacamp.com/tracks/data-scientist-with-r), and [Quantitative
  Analyst with R](https://www.datacamp.com/tracks/quantitative-analyst-with-r)

The Udacity nanodegree is $699 USD and Datacamp's programs work on a
subscription basis: $25 USD/month. Not sure which one to go for... need to do
more research. At the moment, though, I have my hands full with the Nanodegree
as well as the programming languages course.

In September, I started my CS study plan and finished the following courses:

- NAND2Tetris, Part I (IIT)
- Algorithms: Design and Analysis, taught by Tim Roughgarden (Stanford)
- How to Code: Simple Data (UBC)

I'm currently working through:

- NAND2Tetris Part II

I aim to finish it before matriculation.

It was a real slog to finish these courses, as I compressed a 6-week course
into 1 week (N2T I) and I didn't give myself any breaks. Unfortunately I don't
think this blazing fast pace is sustainable.

After finishing these three courses, I realise that my old academic plan is not
ideal. In my rush to "finish" all the courses I don't think I have allocated
enough time to synthesising the knowledge gained in the courses, which is what
truly matters. I think that if I don't do any project that uses the knowledge
I learn in the course, I will forget what I have learned extremely quickly.

That's why I feel that my academic plan should include a "review week" or
"synthesis week" where I build a project that makes use of everything I learn
in the courses.

I should also make sure to add "breather weeks" after an intense period of
studying. I think a good breakdown is as follows:

- 8-week timetable (term time)
  - 6 study weeks
  - 1 recess week
  - 1 project week
- 6-week timetable (holiday)
  - 4 study weeks
  - 1 recess week
  - 1 project week

Lastly, apart from doing projects, I should also dedicate my time to solving
algorithmic problems in order to "crack the coding interview". It would be good
if I could dedicate some time to practice questions on Leetcode. [Teach
Yourself CS](http://www.teachyourselfcs.com) recommends 100 problems:

> For practice, our preferred approach is for students to solve problems on
> Leetcode. These tend to be interesting problems with decent accompanying
> solutions and discussions. They also help you test progress against questions
> that are commonly used in technical interviews at the more competitive
> software companies. We suggest solving around 100 random leetcode problems as
> part of your studies.

If I want to be prepared for the internship then I will have to solve at least
50 problems by the end of Trinity Term. That's ~1.5 problems per week.

### Algorithms: Design and Analysis (Algos I)

A very rigorous course. The lecturer took me through the "greatest hits" of
computer science. In six weeks I learned the following:

- Big O notation and how to calculate the running time of recursive algorithms
  using the Master Method
- Strassen's matrix multiplication algorithm
- Quicksort, Mergesort, and analysing the running time of randomised algorithms
- Graph search (DFS, BFS); computing strongly-connected components
- Greedy algorithms: Dijkstra's algorithm for graph search

Data structures: heaps, binary trees, hash tables, bloom filters. I learned
what each data structure is, what operations they support (and their running
times), and their limitations and applications.

There were 6 programming assignments. I was only able to finish 4 of them; I
could not get the right answer for Quicksort (although my sorting algorithm
works fine) and I couldn't calculate strongly-connected components at all.

I wish that I had more support in my computer science journey. When I get stuck
it's hard to find help. That's the good thing about studying computer science
in NUS (or any university for that matter): you can get help very easily. I
have to go at it alone, and this comes with its own difficulty. If everything
goes smoothly one can be even more productive than studying in university
because you can go at your own blistering pace and you don't have to follow the
pace of the curriculum. But once you get stuck, it's very hard to progress on
your own.

Here's an example of what I mean. I spent almost a week trying to debug my
implementation of Dijkstra's algorithm. I stared at the algorithm very
closely, implemented and reimplemented it in a clean-room environment...
nothing worked. The problem was it couldn't reach vertices it was supposed to
be able to reach. I kept poring over the algorithm again and again and looked
at how I was reading the text file... nothing.

After consulting with many friends (many couldn't help me because they were
busy or unwilling to debug for me---can't say I blame them!) someone finally
found the problem. It turns out that the problem was caused by the adjacency
list representation I was given.

Consider the adjacency list representation for an undirected graph:

```
1 [2,4], [3,8]
2 [3,6]
3 [4,2]
4 [1,7]
```

This adjacency list representation means that there is an edge between 1 and 2
with distance 4, and an edge between 1 and 3 with distance 8.

What my implementation did was faithfully transcribe this representation which
would be incorrect. It built an edge `1 -> 2` with distance 4 but not the
corresponding edge `2 -> 1`.

The correct representation of the graph should be as follows:

```
1 [2,4], [3,8], [4,7]
2 [3,6], [1,4]
3 [1,8], [2,6], [4,2]
4 [1,7], [3,2]
```

I would never have found this bug in a million years as I had tunnel vision-ed
on the algorithm and the input processing. It never once occurred to me to
check the input itself.

### How to Code: Simple Data (μMSc I)

A gentle introduction to programming best practices based off
[SICP](https://mitpress.mit.edu/sicp/).

This is part of a 6-course Software Development MicroMasters offered by edX.
The whole thing costs 832.50 USD and I'm not sure whether or not to pay for it.

The course uses a language called Beginning Student Language (BSL), a subset of
Racket. The cool thing about DrRacket the IDE is that it allows you to paste
images right within the IDE and use it as a variable. So you can create
graphical/interactive programs very easily.

The course taught a way to design functions and programs. Something I found
really interesting was the way we were taught to write functions that operate
on lists. Instead of writing a for loop over a list, we were forced to write a
recursive function instead acting on the head of the list and the rest of the
list. Here's what that looks like:

```
(def (sum_all loi) (
  (cond [(empty? loi) 0]
        [else (+ (first loi) (sum_all (rest loi)))]
  )))
```

instead of, for example,

```python
def sum_all(loi):
  i = 0
  for e in loi:
    i += e
  return i
```

The course also teaches you to write unit tests for every function you write:
the `check-expect` function of Racket made testing very low-friction. I
realised that writing tests really _is_ all it's cracked up to be, provided you
write the correct test cases: it gives you the assurance that the part of the
code is correct and this helps debugging immensely because you won't waste your
time looking at already-correct code.

I really like the course so far although it's not as "hard" as Algorithms I. I
will definitely continue with the MicroMasters Series.

### NAND2Tetris I and II (N2TI, N2TII)

A project-based course that has you write an operating system starting from
NAND gates.

This is absolutely my favourite course. I really like how this course gives me
a big-picture, 30000-feet view of computer architecture.

In the first part of the course you build a computer first by building
electrical gates using a hardware description language. After you build basic
gates like XOR, AND, and MUX (multiplexer), you progress to build not-so-basic
gates like adders, finally progressing to the ALU, RAM, and the CPU. You also
learn to write in machine code and build an assembler for that machine code. I
had a ton of fun building the assembler.

The second part of the course has you writing the majority of the software for
the course. As the compilation is two-tier (high-level language -> VM ->
assembly code) you first write a VM -> assembly translator. Then you write a
program in Jack, the Java-esque high-level language of the course. For my
project I wrote a ["dropship chess"
simulator](https://github.com/lieuzhenghong/nand2tetris-dropship-chess) and
plan to return to it soon (to fix bugs).

![dropship-chess-1](/img/chess/dropship-chess.jpg)

After writing a Jack program you then write the compiler for Jack (where I am
now). Finally, you write the OS for the computer and you'll have built
a computer that can play Tetris (in my case, chess) from scratch!

I think what makes this course so surprisingly manageable is the very
successful way in which the course designers manage complexity. At every step
the complexity of the system increases but it never becomes unmanageable,
because learners can simply abstract away the implementation they did in the
previous module/level of abstraction.

## Some preliminary thoughts on my future

I am extremely fortunate to have a scholarship. At the age of 21 I am now
completely financially independent, and how many can say that?

I am really looking forward to managing my money in Oxford: budgeting
for rent and food, saving up for the big things I want to buy and do, investing
to secure my future financial independence...

I plan to save 200 pounds per month for "delayed gratification" stuff and
invest 300 pounds a month. I will try to live on 800 pounds per month, 300 of
which will go to rent. We'll see if I can live on 500 pounds per month (I
probably can if I cook sometimes).

I'm worried about balancing work with my extracurriculars. There are a lot of
clubs I want to join and I may consider doing a sport or choir or whatnot but
can I do that while studying hard for PPE and CS?
