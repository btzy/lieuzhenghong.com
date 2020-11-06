---
title: MOOCs I've taken (WIP)
layout: base
permalink: "/{{page.fileSlug}}/"
tags:
	- draft
---

This page lists the massively open online courses (MOOCs) I've taken.
I will try to review the MOOCs, outlining why I liked/didn't like them,
what I learned, and whether I finished them.

<div class="toc">

[[toc]]

</div>

## Algorithms: Design and Analysis

Taught by Tim Roughgarden from Stanford University

An excellent course, but unfortunately I don't have access to my work anymore
as Stanford retired their Lagunita platform.

From the [Lagunita website](https://online.stanford.edu/lagunita-learning-platform):

> Looking for your Lagunita course? Stanford Online retired the Lagunita online learning platform on March 31, 2020 and moved most of the courses that were offered on Lagunita to edx.org.
>
> Learners who were actively engaged with the platform, as well as anyone who had been issued a Statement of Accomplishment, were notified throughout the beginning of 2020 that the Lagunita platform was closing. These learners were invited to download any course content and Statements of Accomplishments by March 31, 2020.

They've moved to edX.org now and you have to pay \$149 USD for a verified certificate,
but previously they were giving certificates for free.

![](/img/mooc_certs/algos_1.png)

## From NAND To Tetris (N2T)

Taught by Noam Nisan and Shimon Shocken from Hebrew University of Jerusalem.

**Best course ever**: more on this in the future. Briefly, this is
a project-based course that starts from the microscopic (NAND gates) and builds everything
from there.

From NAND gates you first construct elementary logic gates.
From those you build multiplexers and adders, which combine together to form
ALU, CPU, RAM, ROM, and you have a computer.

So now you have a computer: the next step is to write software for it.
You start off by writing machine code, but that's very unwieldy: Nisan and Shocken
thus give you an assembly language spec and you write an assembler that converts
assembly code to machine code. Obviously assembly code is not ideal either, so
you again climb the ladder of abstraction and build a stack-based _virtual
machine_
(and yes, that means writing VM code, then writing code that parses
VM code into assembler).

You climb _again_ and build a parser and lexer to compile a high-level (something like C)
language called Jack into that VM code. Now that you've built that high-level language
you can then write OS functions (drawing images on the screen, arithmetic, etc.)
and use those functions to write games on it --- games that include Tetris!
(Hence the title).

The beautiful, genius, sublime part is that you've
built every single rung of the ladder (from electrical circuits to high-level
language) and you just get such a great understanding (and appreciation) for
all those previous layers.
It's a bit like those videos which start from a grain of sand and zoom out to
an image of the Earth.

### N2T I

First part of the course deals with the hardware:
using the NAND gate to build multiplexers, half/full adders, then ALU/CPU/RAM/ROM. Then you write machine code
and an assembler. It was quite easy for me, and I made it a bit harder
by forcing myself to write the assembler/parser in C++.

Here's what the assembler looks like. Assembly code looks like this:

```
// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

  @i
  M=0
  @R2
  M=0

(LOOP)
  @R1
  D=M
  @i
  D=D-M
  @END
  D; JEQ

  @R0
  D=M
  @R2
  M=D+M
  @i
  M=M+1

  @LOOP
  0; JMP

(END)
  @END
  0; JMP
```

You have to write code that converts that assembly code to the following machine code:

```
0000000000010000
1110101010001000
0000000000000010
1110101010001000
0000000000000001
1111110000010000
0000000000010000
1111010011010000
0000000000010010
1110001100000010
0000000000000000
1111110000010000
0000000000000010
1111000010001000
0000000000010000
1111110111001000
0000000000000100
1110101010000111
0000000000010010
1110101010000111
```

![](/img/mooc_certs/n2t_I.png)

### N2T II

The difficulty ramps up a lot in the second course
and will really test your software engineering chops.
First you will need to understand how a stack-based virtual machine works,
and how it maps to assembly language.

A simple function in VM looks like this:

```
// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/08/ProgramFlow/BasicLoop/BasicLoop.vm

// Computes the sum 1 + 2 + ... + argument[0] and pushes the
// result onto the stack. Argument[0] is initialized by the test
// script before this code starts running.
push constant 0
pop local 0         // initializes sum = 0
label LOOP_START
push argument 0
push local 0
add
pop local 0	        // sum = sum + counter
push argument 0
push constant 1
sub
pop argument 0      // counter--
push argument 0
if-goto LOOP_START  // If counter > 0, goto LOOP_START
push local 0
```

And you have to write code to convert that VM code to assembly code:

```
// push constant 0
  @0
  D=A
  @R0
  A=M
  M=D
  @R0
  M=M+1
// pop local 0
  @R0
  A=M-1
  D=M
  @R0
  M=M-1
  @R13
  M=D
  @0
  D=A
  @LCL
  A=D+M
  ...
```

Then you will need to understand how high level code
compiles down to the stack-based VM code. Which is even harder.
You will need to write a parser/lexer according to a
language grammar.

Once you've done that, you can use the high-level language to implement
basic OS functions. With those we can then build a non-trivial program.
I decided---in keeping with the namesake of the course---to build a game,
and I wanted to build a game that had never been done before. I eventually
settled on Bughouse Chess played on a 6x6 board.

That was pretty hard too. Jack is a "high level language" in the same way that
C is a high level language, so lots of things were quite painful.
Among other things, images are represented by arrays of 8-bit integers
(0000 0000 = all white, 1111 1111 all black),
and so to draw the sprites of [my chess game](https://github.com/lieuzhenghong/nand2tetris-dropship-chess)
I had to figure out the pixel calculations manually. You can see it in
[SpriteSheet.jack](https://github.com/lieuzhenghong/nand2tetris-dropship-chess/blob/master/source/SpriteSheet.jack)
but it sort of looks like this:

```cpp
    let WPW[0]  = 0;
    let WPW[1]  = 0;
    let WPW[2]  = 0;
    let WPW[3]  = -16384;
    let WPW[4]  = 12288;
    let WPW[5]  = 4096;
    ...
    let WPW[61] = 1023;
    let WPW[62] = 0;
    let WPW[63] = 0;
```

Really really rewarding though.

![](/img/mooc_certs/n2t_II.png)

## Functional Programming in Scala Specialisation

The link to the Specialisation is [here](https://www.coursera.org/specializations/scala#courses). The description:

> This Specialization provides a hands-on introduction to functional
> programming using the widespread programming language, Scala. It begins from
> the basic building blocks of the functional paradigm, first showing how to
> use these blocks to solve small problems, before building up to combining
> these concepts to architect larger functional programs. You'll see how the
> functional paradigm facilitates parallel and distributed programming, and
> through a series of hands on examples and programming assignments, you'll
> learn how to analyze data sets small to large; from parallel programming on
> multicore architectures, to distributed programming on a cluster using Apache
> Spark. A final capstone project will allow you to apply the skills you
> learned by building a large data-intensive application using real-world data.

> Learners will build small to medium size Scala applications by applying
> knowledge and skills including: functional programming, parallel programming,
> manipulation of large data sets, higher-order functions, property-based
> testing, functional reactive programming.

I found the first and fourth courses excellent (and I completed them),
the third course good (completed all but the last assignment),
and the second one incredibly bad. The second course seemed to be missing
more than half of the lecture videos and was impossible to follow.

### Functional Programming Principles in Scala

Taught by Martin Odersky from EPFL

[Verification link for Functional Programming Principles in Scala](https://www.coursera.org/account/accomplishments/verify/M9QXY6C62MKX)

![](/img/mooc_certs/fp_scala.jpg)

### Big Data Analysis for Scala and Spark

[Verification link for Big Data Analysis with Scala and Spark]
(https://www.coursera.org/account/accomplishments/records/CSFJQZEQFBHD)

![](/img/mooc_certs/big_data_scala.jpg)

## Machine Learning

Taught by Andrew Ng from Stanford University

![](/img/mooc_certs/ml.png)

## Mathematics for Machine Learning Specialisation

This was largely a box-ticking exercise because I needed to demonstrate that
I had done linear algebra and multivariate calculus
for the purposes of my Master's admission.

I didn't like these courses because they were too easy and not rigorous enough.

### Linear Algebra

[Verification link for
Mathematics for Machine Learning: Linear Algebra](https://www.coursera.org/account/accomplishments/records/R5MYEWD9MU2J)

![](/img/mooc_certs/ml_linalg.jpg)

### Multivariate Calculus

[Verification link for Mathematics
for Machine Learning: Multivariate Calculus](https://www.coursera.org/account/accomplishments/verify/MDBQLZJDE4JR)

![](/img/mooc_certs/ml_calculus.jpg)

## Databases

This entire series---taught by Jennifer Widom
and hosted on the now-defunct Stanford Lagunita platform---
is excellent. Rigorous and compsci look at the theory of databases
(relational algebra, 3NF/4NF/BNF), with many brain-bending query/SQL exercises.

I took this during the 2019 summer internship with Inzura to learn just enough to
start building my own PostgreSQL database for the
[Bayesian SMS sender pipeloop](2019/09/16/using-thompson-sampling-to-optimise-SMS-effectiveness/).
I completed DB1, DB4 (Relational Algebra), and DB5 (SQL)

### DB1 Introduction to Databases

An excellent introduction for those with no prior knowledge (ergo me).
Easy course by design.

### DB4 Relational Algebra

![](/img/mooc_certs/db4.png)

### DB5 SQL

The certificate is unfortunately lost to time.

## Competitive Programmer's Core Skills

Competitive programming course taught by Russians. I took it mainly as a forcing function
to get more CP practice in when preparing for job interviews back in 2019.

![](/img/mooc_certs/cpsk.png)
