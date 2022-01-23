---
layout: post
title: One Month of TLA+ Learning Adventure
tags: [TLA+, Learning]
---

In this blog, I share my experience from learning TLA+ for one month. This blog does not teach TLA+. Instead, I link to resources for those who are interested in learning TLA+. All resources are free as of this blog.

## What is TLA+

TLA+ is a specification language, where you write a specification(spec) of a finite state machine(FSM). You denfine the inputs(CONSTANTS), mutable state(VARIABLES), and transitions from one state to another(action expressions). The TLC model checker is then used to run the spec and will investigate all possible actions for all states. One key point is that you write "what can happen", not "how it happens". This is why TLA+ is a specification language and not a programming language.

TLA+ is created by [Leslie Lamport](https://en.wikipedia.org/wiki/Leslie_Lamport).

## How did I find out about TLA+

I discussed this in my previous blog [2021 EOY Blog - The adventure of learning TLA+](2022-01-08-2021-EOY-Blog.md##The-adventure-of-learning-TLA+).

## Where I started

I started learning TLA+ by watching [The TLA+ Video Course](https://lamport.azurewebsites.net/video/videos.html). Here are 3 highlights that really grabbed me.

1. The [Introduction to TLA+ video](https://lamport.azurewebsites.net/video/intro.html). Here Leslie Lamport says, "now is not the time to be modest", and he goes on to say what he has achieved and why you should listen to him and learn TLA+. He also states how AWS has used TLA+ since 2013 to prove their internal services, and how AWS senior management believes in TLA+.
1. The [Paxos Commit](https://lamport.azurewebsites.net/video/video7.html) video at `12:30` in the video, Leslie Lamport shows [slide 126](https://lamport.azurewebsites.net/video/video7-script.pdf), and he says, "I don’t know how to write a clearer precise description of this step of the algorithm." At first, I could not understand this code, but then going back and rereading it later, I understood it, and thought, "wow this is the most concise and elegant way to state the behaivor of this algorithm in TLA+."
1. The [final video](https://lamport.azurewebsites.net/video/video10b.html) of The TLA+ Video Course. Leslie Lamport closes the video with this quote, "As you go forward, remember to take the time to stop and think. I
hope what you’ve learned here will help you do that."

## Where am I at now

I am currently reading the [Specifying Systems](https://lamport.azurewebsites.net/tla/book.html) TLA+ book, and am on page 80. I think that watching the videos first has made the book easier to understand.

I have written my 2nd TLA+ spec [RTOP.tla](https://gist.github.com/aaronlelevier/75ec48f7de1878fb55d7604e3bcdacc3).

<script src="https://gist.github.com/aaronlelevier/75ec48f7de1878fb55d7604e3bcdacc3.js"></script>

### RTOP explained

RTOP stands for R-to-P and is a spec that shows a mapping of many-to-many `P` to `R` and the inverse.

`CONSTANT` defines a set of P and a set of R. Everything in TLA+ is a set. These are inputs to the spec.

`VARIABLE` declares the mutable state of the spec. `ptor` and `rtop` are mappings from "P to R" and "R to P", which is the inverse.

`TypeOK` declares our type invariants, which states what are the allowed types of our mutable state. Here we define `ptor` to be a mapping for the domain `P`, where the value always a subset of `R`. The inverse is true for `rtop`.

`Init` initializes the spec. Here we initialize the `ptor` mapping for all `p` in the set of `P` to a value in the subset of `R`. `rtop` is initialized to the inverse.

`PAddR(p, r)` defines a single Action where `r` is added to the mapping for a given `p`.

`Next` declares that in each transition(step) of the FSM that there should exist some `p` and some `r` such that `r` can be added to `p`'s mapping.

`Spec` declares what is run by the TLC model checker. We first initialize our state with `Init` and then we run the `Next` Action where all state variables `vars` are subject to change. The `[]Next` means that `Next` runs continuously until all states are reached.

`THEOREM` states that our `Spec` requires `[]TypeOK` to always be true, so in all states, `Init` and `Next`.

### How can I run this code

`RTOP.tla` can be run using the [TLA+ Toolbox](https://lamport.azurewebsites.net/tla/toolbox.html).

## What I learned

Leslie Lamport is 100% correct in the fact that TLA+ will help you think about problems differently. He talks about how creating abstractions is difficult, and you have to learn it over time. TLA+ forces you to think about the abstraction and at what level you want to create it. There are tradeoffs to coarse of fine grained abstractions. 

When going back to a programming language, thinking about the design separately from the implementation has helped. The design must be correct, or the implementation has to try and make up for it and will struggle. Getting the design right is a must, which then simplifies the implementation. TLA+ is the design, and that is why already I can tell that TLA+ is super valuable.

## What's Next

I plan to keep reading [Specifying Systems](https://lamport.azurewebsites.net/tla/book.html). I also want to continue reading [Distributed Algorithms](https://dl.acm.org/doi/book/10.5555/2821576) by Nancy Lynch at the same time and implement the algorithms from the book in TLA+ to get more practice.
 
## TLA+ References

[TLA+ Website](https://lamport.azurewebsites.net/tla/tla.html)

[TLA+ Cheatsheet](https://lamport.azurewebsites.net/tla/summary-standalone.pdf) 

[TLA+ syntax](http://lamport.azurewebsites.net/tla/newmodule.html)

[Unofficial Learn TLA+ website](https://learntla.com/introduction/)
