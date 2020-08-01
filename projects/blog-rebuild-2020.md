---
title: Rebuilding this website
layout: base
date: 2020-08-03
tags:
  - programming
  - public
  - project
blurb: "I move this website from Jekyll to Eleventy, 
and give it a makeover for good measure"
permalink: "/{{ page.date | date: '%Y/%m/%d' }}/{{page.fileSlug}}/"
---

## Table of Contents

[[toc]]

## Introduction

![The old front page](/img/blog_redesign_2020/old_blog.png)

![The redesigned front page](/img/blog_redesign_2020/new_blog.png)

## Restoring existing functionality

### Learning the templating language

### Writing custom filters

### Parsing Markdown snippets

### Maintaining backwards compatibility with old permalinks

["Cool URIs don't change"](https://www.w3.org/Provider/Style/URI.html)
consistently emphasises the need for URIs not to change,
mainly because someone may have bookmarked your post's old URL
and it would be terrible if they couldn't find it any more.
Eleventy's default paths when generating posts was different from Jekyll's,
so I made sure to point the URLs to the same place by putting

```
permalink: "/{{ page.date | date: '%Y/%m/%d' }}/{{page.fileSlug}}/"
```

in the YAML front matter.

The "Cool URIs don't change" post recommends
indexing by the creation date of the document,
as it is one thing that doesn't change.
"If a document is in any way dated, even though it will be of interest for generations,
then the date is a good starter."
It recommends a URI like `http://www.w3.org/1998/12/01/chairs`,
which is indeed what Jekyll uses by default.

The post further writes "the only exception is a page which is deliberately
a "latest" page for, for example, the whole organization or a large part of it",
for instance, `http://www.pathfinder.com/money/moneydaily/latest`
gives the latest version of the "Money daily" column in "Money" magazine.
If you want to link to the content, however, one would link to it where it appears
separately in the archives as

`http://www.pathfinder.com/money/moneydaily/1998/981212.moneyonline.html`.

In my case the "latest" pages are the index pages: home, about, projects, archive, etc,
and most of the rest of the blog posts are dated.

For some of my work, I am considering following Gwern's example to make URIs indexed by a topic sentence: for instance,

`https://www.gwern.net/Ethical-sperm-donation`

links to a page entitled "The Morality of Sperm Donation".
The pages are constantly updated:
while the page was first written in 2012,
the last major update to the page was in 2018.
This makes sense for Gwern's "long content": the date of document creation is
irrelevant because the pages are constantly updated.
I don't have much long content on the site yet,
but I hope to start writing some soon.
I think the explorations and explanations would be good candidates.

## Improving the website

### Adding a dark mode

### Revamping the projects page

### Supporting Markdown table of contents and footnotes

### Rendering LaTeX, and moving from MathJax to KaTeX

## Things I still need to do

### Fix broken post links

### Fix broken image links

## Sites and blogs I drew reference from

[Practical Typography](https://practicaltypography.com)

[gwern.net](https://gwern.net)

[Reasonable Deviations](https://reasonabledeviations.com)

[Iain Bean](https://iainbean.com/posts/2020/your-blog-doesnt-need-a-javascript-framework/)

### Conclusion
