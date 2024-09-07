---
layout: post
title: What reading Distributed Algorithms by Nancy Lynch cover-to-cover meant to me
tags: [Distributed, Algorithms, Programming]

---

Concurrency has always been of great personal interest to me. I purchased Java Concurrency in Practice by Goetz, the book with the trains on it, and would just look at the cover and think of when to start reading it...

## Background

I remember reading the Erlang finite state machine (FSM) [statem module docs](https://www.erlang.org/doc/design_principles/statem.html) and seeing notation that looked like [TLA+](https://lamport.azurewebsites.net/tla/tla.html). I owned Distributed Algorithms (DA) by Nancy Lynch for 3 years, and I read the first two chapters, and could understand the concept of an FSM for leader election in a ring, but I couldn't understand the model notation or explanations of theorems, lemma, and so on. I use some concurrency in Python programming with threads, but mostly for fan-out-and-back.

## Recently

It is now June 2023. I was driving my kids to school, and the school year was ending, and I told my kids.

> "I read Distributed Algorithms by Nancy Lynch and it took me from September (2022) to May (2023). The same as the school year for you guys. It took me a while, but I read the whole book."

## The difference

I later asked myself, what was the difference? How was I able to understand the book and also read it in its entirety? I think that the difference was learning to think on my own at a new level, and loooking up each concept whether it was math with set theory or graph theory, and being able to connect the concepts. It required doing this because the author assumes that you know these concepts. Also, trying to think in the shoes of the author, and what she was trying to tell me.

I have been fortunate to have had a mentor for software engineering early in my career for about a year, but only one. After this time it has been largely through books and reading the learnings and thoughts of smart people that have helped me grow. It takes time to mentor somebody, so it is a special thing when it happens. Anyone can pick up a book though. The cost is relatively small, and it just takes time, and it is like listening to a senior engineer tell you everything they know. A truly special experience.

Here are some of the concepts that the author assumed knowledge of. These lead to leisurly journeys on Google just looking up the concepts from multiple sources, re-reading them, writing them down in my own words, and trying to connect the dots.

- infimum, supremum, irreflexive partial ordering
- agreement, k-agreement, approximate agreement, 1-valent, bi-valent, uni-valent
- tree, spanning tree, forest, spanning forest, minimum spanning tree, strongly and weakly connected graphs
- singleton set, multiset, superset, poweset
- set union, difference, disjunction, symmetric difference
- function domain, codomain, image, range, injective, surjective

## Impressions

The DA book is an academic book with so many concepts. If you are in the field of computer science or math, I highly recommend this book to you. I can say that I understood what safety and liveness were, but this book adds so many rich concepts to their understanding. For example, it explains low-level and high-level fairness in the context of mutual exclusion, where low-level is concerned with the user steps, and high-level is concerned with granting of the resource. High-level fairness can be guaranteed in some cases and not low-level fairness.

Other important concepts are:

- atomic objects and serialization points
- composition of models, where each model is a component
- simulation relation of a model A to B where a high-level model can be made to show low-level model properties using successive refinement
- impossiblity results - e.g. asynchronous agreement with fault tolerance
- upper and lower complexity for both time and messages

## After

After reading DA, I re-read [Lamport Time Clocks](https://lamport.azurewebsites.net/pubs/time-clocks.pdf) and the meaning was different. The LamportTime algorithm is covered in DA.

I tried learning TLA+ before reading DA, and I couldn't get to the point of writing my own TLA+ models. After reading DA, I now get it and can write models from DA in TLA+, which was one of my dreams. Here is the mutual exclusion Bakery algorithm for example: [Bakery.tla](https://github.com/aaronlelevier/tlaplus-aaron/blob/develop/specs/Bakery.tla). I wanted to write this model spec in particular because we run a bakery at my work, and I just liked the name of the algorithm, but the bakery at work is for AWS AMI's so a little different :)

## Next

I am going to continue learning distributed systems. Whatever I learn can be distilled down and used for concrete cases in my AWS programming work.

I found this [MIT course schedule](https://pdos.csail.mit.edu/6.824/schedule.html) for distributed systems with a lot of links to research papers. This may be a good next step. I may also read Reliable and Secure Distributed Programming by Cachin.

I have been careful to not tell myself that "I finished the DA book". I plan to keep referring back to it. Instead I tell myself, "I read the DA book".
