---
title: Report on CS107E Assignment 1
layout: base
tags: ["public", "computer science", "programming"]

---

## Introduction

I managed to rope Wei Neng in to do CS107E with me.
This may or may not be part of my plan to self-study
a Stanford CS degree in my spare time.
CS107E is a computer systems/computer architecture course.

> CS107e: Computer Systems from the Ground Up is a variant of CS107 that teaches the fundamental concepts of computer systems through bare metal programming on the Raspberry Pi. Bare metal programming means you will not run an operating system on the Raspberry Pi and will make minimal use of libraries. This course also serves as an introduction to embedded systems. The course starts with the microprocessor and moves up to the C programming language, without skipping anything in between. The goal is to build a solid understanding of all aspects of how modern computers execute programs and how program development tools work.

> Assignments build upon each other by adding more and more functionality to a core library. They culminate in a simple personal computer shell using a keyboard and display. Finally, students do a project of their choosing where they build a complete hardware-software system.

I took NAND 2 Tetris back in 2017 and I really enjoyed it;
however it trades off depth for breadth 
in its whirlwind tour-de-force from bottom to top.
I wanted to take a second course to solidify my understanding
and fill in the gaps.
And since I've always loved the idea of building
software on the bare metal,
this "build an OS from scratch on the Raspi"
was very appealing.

And it comes highly recommended as well.
This is what someone said on Reddit:

> I just took 107E this quarter. I would highly, highly recommend 107E over 107. Be prepared for a giant time commitment and more work than 107... but take 107E.
> ...  
> That doesn’t even begin to touch the material. Frankly, in terms of time commitment and difficulty, 107E is more challenging than 107. For the first 4-5 weeks, you don’t even have print statements. All you have is, literally, a blinking LED light on your Pi to tell if you’re buggy or OK. You build literally everything from the ground up, with your own code, starting with no operating system and debugger, and there are times when things get hard. Crushingly hard, like spend multiple nights on a single bug hard.
>
> Also, the grading expectations, at least nominally, are high. The course is curved (this quarter at least), but according to the website, to get an A you have to do 3 or more extensions; get the full system bonus (no major bugs in code); have an outstanding final project; trend towards + in code quality; etc. That’s a lot. Now, the requirements aren’t really that stringent, but this course will easily demand 20 hours a week and your best effort to get the extensions in and avoid falling behind.
> 
> But there’s no feeling quite like when you get your code working, or your console working at the end of the quarter. The workload is high — don’t let the “no exams” fool you, it’s more than 107 easily! — but the reward is incredible, and you get to program on a Raspberry Pi! You get to wire things up on breadboards, mess around with LEDs, transistors, resistors, break things, build things...
> 
> For our final projects this quarter, someone built a freaking Rubik’s cube solver robot! Another person built Pac-Man with NES controllers; another person, a piano game using touch sensors on a glove you wear like Michael Jackson; yet another person, a robotic tea kettle. 107? You’ll be banging your head against some inane heap allocator running on a machine you can’t even see, at the same time you’re building these cool things in 107E.
> 
> The topics covered are actually quite close to 107, as well. Naturally, the focus of 107E is a bit different, as hardware, not just the software that runs on it, is always part of the equation. You build software for your GPIO pins, then your memory allocator, then your strings library, then your graphics library and frame buffer handling... You’re building up a fully-working system in layers each week, step by step, working towards a console with commands you can type. But along the way, you’re also covering assembly, memory allocation, system architecture, processing, etc. and your understanding of those topics is no less than that of a 107 student.

Unfortunately because there seems to be some problem
with my Raspi TTY, I had to share with Wei Neng
and we work through the assignments together.
This is very much against the Stanford Honor Code but 
I couldn't care less since
i) I'm not a Stanford student, 
ii) pair work keeps me accountable, and
iii) the only thing that happens if I cheat is 
cheating myself of my own learning, so I won't cheat.

## What did we have to do?

*Time taken:* about 10 hours for everything all-in

In Assignment 1 we were tasked to write a "Larson scanner",
which is basically just blinking some lights in
an aesthetic-looking scanner pattern.
The catch is that we had to write it in assembly.
In order to make lights blink on the Raspi
you have to write an "ON" bit to the GPIO memory address.
Because it's assembly, there are no functions, while loops,
or even variables.
And in order to 

## What was hard about the task?

Something that was very hard is that you can't
just use any number as an immediate.
So for example
if you try to do `mov r1 #584`
the code won't compile and it will give an error like
`invalid constant value`
or something like that.
The rules are something that I haven't bothered to learn yet
(it has something to do with barrel shifting---see the "What do I still need to know?" section)

The trick is to add byte-by-byte using an inclusive or command:
```as
mov r1 #73
orr r1 #512
```

Another hard part about writing assembly is that 
it's kind of like a real time system.
Every instruction is mapped to one line of binary code
and that takes one clock cycle (I think).
So everything is driven by the clock cycle
and you can get precision on the order of milliseconds.

It was actually quite hard to do pulse-width modulation
with a constant delay.
Suppose you want to keep the LED on for 1 second.
That's some number of clock cycles.
However, when doing pulse-width modulation
you want to flicker it off and on with a short delay between.
The challenge is: how do you vary the brightness
(ergo change the time the bulb is off vs on)
while keeping the *total* time the LED on the same?
Remember you don't have any sort of timer:
you can only declare variables that tick down.
You need a nested loop with the invariant that
the nested loop must run for the same amount of time
regardless of how bright or dim the LED is 
(i.e. how long the LED stays off).
So that was pretty tricky.

## What did I do well?

I enjoyed writing assembly code in N2T and this time was
no different. 
The simplicity of assembly code is really quite nice.
I could feel the assembly that I did in N2T come back to me.
Even though the assembly language taught in N2T
was a toy language, a lot of the concepts were transferrable.
I found that I was able to write more simple/less convoluted
assembly code than Wei Neng, almost certainly
because of my previous practice.

## What could I have done better?

We worked till 2am/230am until we were super tired,
and we were already far from productive.
I should have called a break earlier
so that I wouldn't fuck my sleep schedule.

## What did I learn?

I learned (a small part of) ARM64 assembly.
I also learned about the concept of pulse-width modulation.

## What do I still need to know?

I'm still quite foggy on why some immediate values
are allowed and why others aren't. 
Read 
[how ARM encodes immediates](https://alisdair.mcdiarmid.org/arm-immediate-value-encoding/#play-with-it)

Browse through
[the ARM instruction set manual](https://cs107e.github.io/readings/armisa.pdf)

## Final thoughts

I really enjoyed this assignment,
and I hope I get to code more in assembly next time
(or C at least).
