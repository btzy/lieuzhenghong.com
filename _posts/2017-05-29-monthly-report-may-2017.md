---
layout: base
date: 2017-05-29
title: "May 2017 report"
tags:
  - progress report
  - monthly review
  - private
  - diary
  - post-ord
permalink: "/{{ page.date | date: '%Y/%m/%d' }}/{{page.fileSlug}}/"
---

Since my
[last post]({{'/_posts/2017-03-25-quarterly-report-2017/'}}) I have done the following:

- Finished my internship at iGlobe (ended May 12, 2017)
- Been rejected by MAS and GIC in the penultimate round
- Went to Japan for the first time in my life
- Finished building the Raspberry Pi console
- Finished my first substantial MOOC, Andrew Ng's Machine Learning
- Built my first executable file (.exe rather than .py) and wrote _software_ rather than a _program_

Some of these deserve a separate post so I'll dedicate the whole of today to writing them.

## Finished my internship at iGlobe

I started interning at iGlobe on 23rd January 2017 and ended 12th May 2017. My
main responsibility was to help the investment team (Jeff) in his sourcing for
new deals. That means that I accompanied him to meetings with promising
startups and wrote minutes for the meetings.

At a later stage, this evolved into due diligence whereby I had to research on
the company to see if i) they could deliver on their promised claim; ii) they
did not misrepresent the uniqueness or impact of their technology; iii) there
were any other competitors in this market and so on.

At the final stage, I was tasked to help write **investment papers** for the
company. Investment papers are papers written by the investment team for the
Board. They introduce the company and explain why the company is worth
investing in. I helped Jeff do in-depth research in the technology of the
company and wrote those sections of the investment paper. Over the course of my
internship I helped write investment papers for V-key, an online crpyto company
and SourceSage, an app for oleochemical traders.

I was also tasked to do market research on industries iGlobe was interested in
(e.g. insurtech, fintech, blockchain). I produced three research reports on
insurtech, medtech and payment data monetisation.

On the investor side, I helped the investor team conduct research on the
possibility of getting family offices to invest in iGlobe.

I also learned miscellaneous administrative stuff like how to use a courier
service, how to post a letter and so on.

### Programming at iGlobe

I wrote two programs during my stint at iGlobe,
[form-letterer](https://github.com/lieuzhenghong/form-letterer) and
[form-emailer](https://github.com/lieuzhenghong/form-emailer).

These programs make it easy to send multiple similar emails (form emails) to
different recipients. As an intern, I was given drudgery like this to do and I
didn't like it (I am a very lazy person). Therefore, I wrote these programs to
help me.

Form Letterer takes in a specially-formatted Word document and a `.csv` data
file, and returns multiple personalised Word documents. This is useful if you
want to be printing contracts for example.

Form Emailer automatically sends personalised emails to receipients, and
supports attachments as well. It can be used in conjuction with Form Letterer
to send each recipient a different Word document.

These programs are actually quite trivial (form-letterer was actually harder
because of how difficult it is to manipulate Word documents programmatically!).
It was yet another example of, as Mark puts it, "library whacking". However, I
still learned a lot from these projects.

First of all, I learned how to write code that is meant for the end-user. This
means catching exceptiosn and throwing 'friendly' error messages; being
permissive and clever when handling imperfect user input; building an
executable instead of leaving it as a `program.py` file (may write a separate
post on this); writing comprehensive and easy-to-read documentation.

Second of all, I learned how to use Python's `argparse` to write a command-line
program! I've never done this before and I'm very happy with it.

I'm also happy with the fact that my code is clean and follows PEP-8.

I'm slightly regretful that I didn't manage to write a nice TUI/GUI. Instead I
used Python's `input` to prompt users to fill in their details instead.

Of course, the real test of any piece of software is: is it being used? And I
am happy to report that it is (for now...). I met Kim and her nephew at a calligraphy
competition yesterday and she told me that they successfully used it to send
their quarterly review without any help on my part!

All in all, I am very pleased to have written a piece of software that is
successfully being used by end-users. I'm also happy that I was able to
contribute to iGlobe above and beyond the help normally expected from an
intern.

## Rejected from scholarships

I was rejected from both GIC and MAS in the penultimate round, the 'group
discussion' round... perhaps my personality was too abrasive. Unfortunately the
scholarship agencies don't give feedback on unsuccessful applications.
Nevertheless, it was a good learning experience; I don't regret the application
process.

The last scholarship I am waiting for is IMDA. As of this moment, IMDA is
trying to schedule an interview slot with the directors. I told them that I
would be willing to cancel my trip to Yunnan if need be; nothing to do now but
wait.

## Future plans

The path ahead of me is bifurcated. All depends on my decision to go to Ox or
NTU.

There are things that I will be doing no matter my eventual choice, however.

### Some very clear goals:

1. Get a Class 3 driving license by September 31 2017
2. Do at least one machine learning project by August 2 2017

### Some more nebulous ones:

1. Think about a new niche for the Codellective: see [this Saturday kids
   class](http://saturdaykids.com/creative-coder/pykids-level-1/) also doing
   Python Turtle idea but they have a lot of traction and are charging 700-900
   per workshop?? I think the real question is : what is Codellective, what are
   we doing different from the rest, what kind of volunteers do we want?

### Pipe dreams:

I am pretty sure that these won't happen

1. Learn to play one of Faye Wong's songs on the piano by 2nd Aug 2017—no point
   asking Prof Chiu for the scores if I never use them
2. Think of a way to earn some money during university
