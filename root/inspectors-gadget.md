---
title: Inspector's Gadget
date: 2017-08-01
tags: project
layout: base
img: "/img/inspectors_gadget/inspectors_gadget_gif.gif"
blurb: "Custom Electron app that makes building inspections more efficient"
permalink: "/projects/{{page.fileSlug}}/"
---

## Inspector's Gadget

August 2017

<img src="/img/inspectors_gadget/inspectors_gadget_gif.gif" width="600px">

Inspector's Gadget is a bespoke desktop application written in ElectronJS
that was custom-built for a civil engineering consulting firm. It streamlines
the process of writing building inspection reports. Real-world usage reports
show that it decreases the time taken to write a report by up to 85%.

A building inspection report involves three things:

- Photos taken of the building
- Floor plan of the building
- PDF report of all building defects and recommended actions taken (if any)

A building inspection report is done as follows: An engineer walks around
the building and takes photos of all structural features and defects (if
any). The engineer will then "tag" the floor plan---put labels on the floor
plan to show where each photo was taken. Finally, the engineer will produce
a PDF report which includes all the photos taken, a description of each photo,
and a classification of the defect type.

Before I created this application for the firm, creating a report was a very
time-consuming process. First, every photo taken was renamed in File Explorer.
Then, the floor plan was tagged in Microsoft Word by manually creating Text
Boxes and moving them to the desired spot. Finally, to generate the report, the
engineers would paste the images one by one into the Word document. God forbid
the engineer missed out one photo in the middle, as to insert the new photo
_all_ subsequent photos had to be cut-and-pasted one box down. (You can see an
example in the image: the image A2-30 has been left out. That means all the
images and text from A2-31 onwards have to be cut and pasted one box down to
make space for the new image.)

This application streamlines every part of the process, from uploading images
to quick-tagging floor plans to the final report generation. Just click an area
of the floor plan to tag it. The report is generated automatically, and if you
missed out a photo, that's fine---the report will reflow seamlessly.

![Inspector Gadget's UI to create a report](/img/inspectors_gadget/report.png)

[GitHub](https://github.com/lieuzhenghong/inspectors-gadget/)
