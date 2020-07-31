---
title: Form Emailer and Form Letterer
date: 2016-04-01
tags: project
layout: base
img: "/img/form_suite/form_emailer.png"
blurb: "A collection of Python scripts that 
simplifies the process of sending mass personalised emails"
---

## Form Emailer and Form Letterer

![screenshot of form emailer](/img/form_suite/form_emailer.png)
![screenshot of form letterer](/img/form_suite/form_letterer.png)

April 2016

A mini "software suite" that makes sending mass, personalised emails very
simple. I created it because I was too lazy to send emails manually when I was
an intern. It was written in Python with the help of
[python-docx](https://python-docx.readthedocs.io/en/latest/).

Form Letterer allows you to quickly generate Word documents from a template,
(e.g. documents with different names/dates/amounts), while Form Emailer lets
you send personalised emails with different files attached. They synergise as
you can use Form Letterer to generate unique documents and then send those
documents in personalised emails with Form Emailer.

One of the "killer features" this software suite has is the ability to send
unique attachments (a different attachment to each recipient), which Outlook
Mail Merge lacked. Another cool feature is it supports arbitrary Python code in
substitutions, which allows for amazing substitutions Mail Merge just can't support
like conditional execution.

[Form Letterer GitHub](https://github.com/lieuzhenghong/form-letterer/)  
[Form Emailer GitHub](https://github.com/lieuzhenghong/form-emailer/)
