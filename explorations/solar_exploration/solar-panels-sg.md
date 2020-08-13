---
title: How many solar panels would be needed to 100% solar-power Singapore?
layout: base
tags:
  - exploration
---

[toc]

**Principal investigators: Michael and Celine**

## Summary

We use horizontal irradiance data, Singapore's half-hourly power demand
statistics and solar panel schematics to calculate the area of solar panels
(and battery storage) needed to meet Singapore's energy demands. We
calculate that an area of **16,800 hectares** would be needed.

I am very uncertain in this calculation and I am certain that I have missed
something.

Thanks very much to Michael and Celine for researching this problem with me:
whatever errors remain are mine.

## Background and motivation

I saw this infographic,

## Strategy

We'll tackle this question in two main parts: on the supply and on the demand side.

1. How much energy does Singapore demand?
2. How much energy can be produced per unit area?
   - How much energy falls onto the ground per unit area?
   - How much of that energy can we soak up per unit area?

## Demand-side: how much energy does Singapore demand?

How much power does Singapore demand? The answer depends of course on "over what period"? Because solar power varies greatly throughout the day, we should take the highest-resolution snapshot of the data.

The best I could get was half-hourly power demand figures obtained from
Singapore's [Data.gov.sg](https://data.gov.sg/dataset/half-hourly-system-demand).
The dataset starts in 2012 and ends in 2017 but I extrapolated it to 2020
(taking the geometric mean).

The chart below plots half-hourly power demand in Watts.
Pick any date from 22 Feb 2020 to 20 June 2020 to see how
power demand varied during that day.
Surprisingly, power usage tends to dip during working hours and
go up during the wee hours of the night

This chart gives the daily fluctuation

We can see a periodicity in the data,
and a general upward trend in power demand over the months.

## Supply-side

### How much energy hits the ground? Global Horizontal Illumination (GHI)

Data from...

The following graph

Check out 9 March 2020:
that day seems to have been a particularly overcast day,

To calculate the

## Putting it all together

### The duck curve

Move the slider and the date picker to

We have enough solar panels to fulfill Singapore's peak power demands
when the area under the red curve
(total solar energy that is collected for a given area)
exceeds the area under the blue curve
(total power demand of Singapore).

This is a

### How does that look like on a map of Australia?

In the image below, I've marked in red the (approximate)
square area of both Singapore and the area of solar panels
needed to fully power Singapore (~30,000 hectares).

The image has dimensions 1382 x 1005 pixels.
In the image, a length of 100 pixels corresponds to 500km distance.
1 pixel therefore represents 5km, and a 1x1 pixel square
represents an area of 25 sq km.

The area of Singapore is (very generously) 900 sq km, so this
corresponds to about a 6x6 pixel square.

And 30,000 hectares is 300 sq km, which is a 3x4 rectangle.

Here's what that looks like on the map:

![Full size image of Australia](/img/solar_exploration/australia_area_full_size.png)

You might need to squint a bit to see it, because Australia is very (very!!)
big. I'll save you the trouble and zoom in into Australia:

![Zoomed in version of Australia](/img/solar_exploration/australia_area_crop.png)

And here's zoomed in even more on just the northernmost tip of
the Northern Territories:

![Zoomed in version of Australia](/img/solar_exploration/australia_area_crop_2.png)

<div id="observablehq-744a5081">
  <div class="observablehq-area_multi"></div>
  <div class="observablehq-date_picker_1"></div>
  <div class="observablehq-demand_chart"></div>
  <div class="observablehq-date_picker_2"></div>
  <div class="observablehq-supply_chart"></div>
  <div class="observablehq-total_net_supply"></div>
  <div class="observablehq-area_needed_hectares"></div>
  <div class="observablehq-area_input_1"></div>
  <div class="observablehq-duck_chart"></div>
  <div class="observablehq-area_input_2"></div>
  <div class="observablehq-area_each_day_chart"></div>
</div>
<script type="module">
  import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@4/dist/runtime.js";
  import define from "https://api.observablehq.com/@lieuzhenghong/solar-power-observable-take-2.js?v=3";
  (new Runtime).module(define, name => {
    if (name === "area_multi") return Inspector.into("#observablehq-744a5081 .observablehq-area_multi")();
    if (name === "date_picker_1") return Inspector.into("#observablehq-744a5081 .observablehq-date_picker_1")();
    if (name === "demand_chart") return Inspector.into("#observablehq-744a5081 .observablehq-demand_chart")();
    if (name === "date_picker_2") return Inspector.into("#observablehq-744a5081 .observablehq-date_picker_2")();
    if (name === "supply_chart") return Inspector.into("#observablehq-744a5081 .observablehq-supply_chart")();
    if (name === "total_net_supply") return Inspector.into("#observablehq-744a5081 .observablehq-total_net_supply")();
    if (name === "area_needed_hectares") return Inspector.into("#observablehq-744a5081 .observablehq-area_needed_hectares")();
    if (name === "area_input_1") return Inspector.into("#observablehq-744a5081 .observablehq-area_input_1")();
    if (name === "duck_chart") return Inspector.into("#observablehq-744a5081 .observablehq-duck_chart")();
    if (name === "area_input_2") return Inspector.into("#observablehq-744a5081 .observablehq-area_input_2")();
    if (name === "area_each_day_chart") return Inspector.into("#observablehq-744a5081 .observablehq-area_each_day_chart")();
  });
</script>
