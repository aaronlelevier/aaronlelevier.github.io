---
layout: post
title: How to calculate effective top tube length
tags: [Bike, Math, Erlang]
---

![Geometry Chart](https://i.imgur.com/D0T1w64.png "Geometry Chart")

## Summary

Don't just rely on mountain bike reach! Effective top tube(ETT) is also an important number for bike size fit. Recently, I was looking at [Airdrop Bikes](https://www.airdropbikes.com/) and became interested in the [Airdrop Filter](https://www.airdropbikes.com/en-us/pages/airdrop-filter), but sizes were limited. This blog is my research on figuring out ETT and if an in stock size would fit.

I have ridden a [Commencal Meta 29](https://geometrygeeks.bike/bike/commencal-meta-am-29-2019/) with a reach of 460 and seat tube angle(STA) of 76.5.

I have ridden a [Chromag Stylus](https://chromagbikes.com/products/stylus-2020) with a reach of 465 and STA of 76.0.

Question, will an [Airdrop Filter](https://www.airdropbikes.com/en-us/pages/airdrop-filter) with a reach of 475 and STA of 78.2 fit? (This is size large and medium is out of stock).

## Geometry Numbers

![Geometry Numbers](https://i.imgur.com/aNHDcfn.png "Geometry Numbers")

## How to calculate

```erlang
% Functions
DegreesToRadian = fun(Deg) -> math:pi()/180 * Deg end.
Hypotenuse = fun(B, Beta) -> B / math:sin(DegreesToRadian(Beta)) end.

% Parameters
Stack = 614.0.
HeightLow = 600.0.
STALow = 78.1.
HeightHigh = 700.0.
STAHigh = 78.7.
Reach = 475.0.

% seat tube able(STA) difference
STADiff = abs(STALow - STAHigh).
% percentage difference between high and low STA
PercentHeightDiff = abs(HeightLow - Stack) / abs(HeightLow - HeightHigh).
% Effective STA
ESTA = STADiff * PercentHeightDiff + STALow.

% Answer - effective top tube(ETT)
ETT = Hypotenuse(Stack, ESTA) * math:cos(DegreesToRadian(ESTA)) + Reach.
```

# Conclusion

The Airdrop Filter ETT is shorter than expected. Comparing to a reach of 460 or 465, the 475 reach Filter has the shortest ETT of 603. This is due to the steep STA.
