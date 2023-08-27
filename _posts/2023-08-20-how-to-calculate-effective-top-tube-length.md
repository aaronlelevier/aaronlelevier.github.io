---
layout: post
title: How to calculate effective top tube length
tags: [Bike, Math, Erlang]
---

![Geometry Chart](https://i.imgur.com/D0T1w64.png "Geometry Chart")

The problem is that [Airdrop Bikes](https://www.airdropbikes.com/) is sold out of size medium Filter framesets, and the geometry chart doesn't show effective top tube, which is another important number, in addition to reach, when calculating bike fit.

# Geometry Chart legend

This is the legend for the red triangle overlayed on the Airdrop Filter geometry chart:

```
A - ?
B - stack
C - hypotenuse - effective seat tube length
a or Alpha - ? - can ignore
b or Beta - ? - effective seat tube angle
```

# Initial thoughts

I was going purely off of reach, and the medium is 455 vs. a large, which is 475. I've owned a [460](https://geometrygeeks.bike/bike/commencal-meta-am-29-2019/) and [465](https://chromagbikes.com/products/stylus-2020) reach bike, so 455 sounds good if I want to size down, but Airdrop is sold out. The chart doesn't list the effective top tube, which is the horizontal distance from the stack height to the saddle, so let's calculate it.

In order to calculate effective top tube length, we need to calcuate the effective seat tube angle, which is the angle of the seat tube at the stack height. Then, using the geometry of right triangles, we can calculate C, the hypotenuse, and then A, using C and one angle Alpha or Beta.

# Geometry numbers

![Geometry Numbers](https://i.imgur.com/aNHDcfn.png "Geometry Numbers")

# How to calculate the effective seat tube angle

With a stack height of 614.5, we can take the difference in distance from the measured seat angles in the geometry numbers at 600 and 700, and find the effective seat tube angle.

```erlang
% Returns the effective seat tube angle (STA) using:
% Low = {STA, Height}
% Height = {STA, Height}
% Stack
% ex: sta({78.7, 600.0}, {78.1, 700.0}, 614.5).
sta(Low, High, Stack) ->
    {SAL, SHL} = Low,
    {SAH, SHH} = High,
    SAL - ((Stack-SHL)/(SHH-SHL) * (abs(SAH - SAL))).

1> Beta = sta({78.7, 600.0}, {78.1, 700.0}, 614.5).
78.613
```

# How to calculate the effective seat tube length

This is the hypotenuse, which is the red `C` in the diagram.

```erlang
% Returns the radians using the degrees 'N'
radians(N) -> N * (math:pi()/180).

c(Beta, B) ->
    B / math:sin(radians(Beta)).

1>  c(78.613, 614.5).
78.613
```

# How to calculate a side given with an angle and the hypotenuse

We can now calculate the red `A`.

```erlang
a(C, Beta) ->
    C * math:cos(radians(Beta)).

1> a(c(78.613, 614.5), 78.613).
123.7598468837922
```

# Finally, calculate the effective top tube

This is the red `A` plus the black `A` for reach:

```erlang
ett(STA, Stack, Reach) ->
    a(c(STA, Stack), STA) + Reach.

1> a(c(78.613, 614.5), 78.613) + 475.
598.7598468837922
```

# Conclusion

The effective top tube (ETT) is actually shorter than I expected. The previous reach bikes of 460 and 465 have a comparable ETT of 619 and 614 . So, the size large Airdrop Filter ETT is shorter.

Another note is that the bike with an ETT of 619 has a stack height of 633.5 vs. the 614 ETT bike with a stack height of 597. The latter feels slightly longer, so stack height comes into play as well. The Airdrop bike has a stack height of 614.5, so it will feel in the middle of these two with how stack height affects position on the bike.

The large is said to fit a rider height of 175-188mm, and I'm 180mm, so I guess they are correct. But, I didn't just want to go by their recommendation. Anyways, it was fun to calcuate the geometry.
