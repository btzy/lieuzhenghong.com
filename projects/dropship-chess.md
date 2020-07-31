---
title: Dropship Chess
date: 2017-09-01
tags:
  - project
layout: base
img: "/img/chess/dropship-chess.jpg"
blurb: "A chess program on a custom OS/computer I built 
following the NAND 2 Tetris Course"
---

## Dropship Chess

September 2017

![screenshot of dropship chess](/img/chess/dropship-chess.jpg)

A game built for the the Jack computer, a computer we build ourselves from
scratch (NAND gates) as part of the (excellent) course [From NAND to
Tetris](https://www.nand2tetris.org/course).

It's chess played on a 6x6 board where captured enemy pieces can be
"airdropped" anywhere on the board in lieu of moving a piece, kind of like
Shogi/Bughouse. White starts with two knights and Black with two bishops—so you
have to capture the opponent's knights/bishops to get your own.

NAND To Tetris is an excellent overview of computer architecture. You start
with a NAND gate and build full adders and mutliplexers from it. You then build
basic processing and storage devices (ALU, RAM , CPU, display). Then you build an
assembler, then a VM, then an interpreter, then a full-fledged parser/lexer and
compiler for a high level language called Jack, and finally you write the OS
for the computer in Jack! At the end of the course you've built a computer
which supports a high-level language and can run a highly nontrivial
program (Tetris) starting only from NAND gates. Awesome!

[Dropship Chess](https://github.com/lieuzhenghong/nand2tetris-dropship-chess),
[NAND 2 Tetris](https://github.com/lieuzhenghong/nand2tetris/)
