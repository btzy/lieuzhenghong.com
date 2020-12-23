---
title: Report on CS107E Lab and Assignment 2
layout: base
tags: ["public", "computer science", "programming"]
---


## Introduction

This was the second lab (of seven) of Stanford's CS107E course.
It may or may not be part of my plan to study a Stanford CS degree
in my spare time.
CS107E is a computer architecture course where you build 
a simple personal computer shell on the Raspberry Pi bare metal
(without an OS).

In this lab we disassembled a C program to understand how C programs
are translated by the compiler into assembly.
This also improved my understanding of assembly.
I learned a bit about the stack
We also learned a bit about Makefiles.

## Using gdb

Add a breakpoint by using `break`.
Use `info reg` to view the registers,
`disassemble` to view the assembly code of the current function,
and `next` and `step` to step through code execution.

## Understanding Makefiles

The symbols that begin with `$` and `%` in a pattern rule are handled by make using the following interpretations:

`%` is a wildcard symbol when used in a rule; `%.o` for example matches any file that ends with `.o`
`$@` refers to the left part of the rule, before the `:`
`$<` refers to the first element in the right part of the rule, after the `:`
            
One more special variable `$^` refers to all elements in the right part of the
rule, after the `:`, which is to say all of the dependencies.
