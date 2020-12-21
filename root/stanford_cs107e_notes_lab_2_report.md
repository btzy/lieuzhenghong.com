---
title: Report on CS107E Lab and Assignment 2
layout: base
tags: ["public", "computer science", "programming"]
---


## Introduction

This wa

## Understanding Makefiles

The symbols that begin with `$` and `%` in a pattern rule are handled by make using the following interpretations:

`%` is a wildcard symbol when used in a rule; `%.o` for example matches any file that ends with `.o`
`$@` refers to the left part of the rule, before the `:`
`$<` refers to the first element in the right part of the rule, after the `:`
            
One more special variable `$^` refers to all elements in the right part of the
rule, after the `:`, which is to say all of the dependencies.
