---
layout: post
title: How I came to read the first half of Distributed Algorithms by Nancy Lynch
tags: [Distributed, Algorithms, Programming]
---

This blog is my story of how I came to read half of Distributed Algorithms by Nancy Lynch.

## The beginning
I first found out about this book via the video [# Distributed Systems Theory for Practical Engineers](https://youtu.be/clYXrZtKhGs). In this video, the speaker references 4 books:

1. Distributed Algorithms by Nancy Lynch
1. Reliable and Secure Distributed Programming by Christian Cachin
1. Replication Theory and Practice by Bernadette Charon1.Bost
1. Guide to Reliable Distributed Systems by Kenneth Birman

Lets refer to these books by number 1-4. The speaker calls book 1 "the bible". Then says, "if you are going to read any book, read book 2. I went online and picked up the first two books.

## Getting stuck
I started reading book 1. I found the book to be abstract and scholarly. It uses math and formal proofs, and I was not used to the presentation style. I thought that book 1 might be too much on the theory side, and that I should read book 2 for practical applications.

I started reading book 2, but I wasn't getting it. The book seemed to be assuming knowledge that I didn't have.

## Taking a break to try Erlang
I next decided that was I really wanted to do was learn Erlang and write concurrent applications. I started reading [Programming Erlang](https://pragprog.com/titles/jaerlang2/programming-erlang-2nd-edition/) by Joe Armstrong.  I was able to read the whole book and do the exercises. This took about 9 months of hobby coding time.

It was time to build a concurrent application to solve a problem. I did build a simple project named [dta](https://github.com/aaronlelevier/dta) with a webscraper, where processes would fan out and scrape pages, then combine the results and email them to me. I liked this project, and the context was scraping mountain bike websites, so that was fun.

Next, I wanted to build something more interesting and more useful. I think at this time, I first saw the [gen_statem behavior](https://www.erlang.org/doc/design_principles/statem.html) documentation. I remember seeing this notation:

```
State(S) x Event(E) -> Actions(A), State(S')
```
Explained as:
> These relations are interpreted as follows: if we are in state S and event E occurs, we are to perform actions A, and make a transition to state S'. Notice that S' can be equal to S, and that A can be empty.

I was intrigued by this explanation. I like FSM.

What might I add to this explanation now? S is a system state. E is an external event and is input to the process. A is the set of internal tasks to be performed by the process. S' is the next system state returned as response. The system's state is S. The processes state is not noted here. The process must be input-enabled in order to accept the input event E.

But, I didn't know that at the time. I tried the [example](https://www.erlang.org/doc/man/gen_statem.html#example) `gen_statem` and coded up a couple concrete `gen_statem`.

Next, I had the idea to make drone software, and I wanted to write this in Erlang because I had recently learned it, and I wanted to take advantage of the fault tolerance semantics of the Erlang OTP. This did not go very far. I remember getting stuck on simple issues if you know Erlang. I hired the creator of Erlang [Cowboy](https://github.com/ninenines/cowboy) as a consultant for 1 hour. He is expensive for me, and that is all I could afford, but I wanted to get unstuck. When talking with him, he brought up things like "you didn't assign the return value, so you won't get a pattern matching error if the return value is wrong". Simple things like that, where I needed to do some more digging, and then I would find the error myself. I gladly thanked him.

## What next, I already took a break
I tried again to ready the first chapter of book 1. I still couldn't get it. I was starting to think that Erlang and concurrent programming wasn't for me.

I took a break. Tried Golang. Then went back to Erlang. Refreshed and got back almost to my same language level. I was still not sure what to build. I remembered this feeling after first learning Python. I had done the same thing, and wasn't sure after reading my first book and doing all of the exercises what to build until I found Django, and that made Python real for me.

## Discovering TLA+
Somehow about 1 year and 4 months ago from now, I was watching tech talks on YouTube and found the video [# TLA+ by Markus Kuppe](https://www.youtube.com/live/uPNFcTAgw3E?feature=share) with the subtitle "save weeks of debugging with TLA+". I didn't know know what TLA+ was, but I watched the video out of intrigue.

TLA, stands for Temporal Logic of Actions, and is a specification language for writing state machines.

I wanted to learn more, so I next found the TLA+ [website](https://lamport.azurewebsites.net/tla/tla.html) and did the video course.

## Still no luck
I felt ready after this, so I went back to book 1 and tried reading chapter 1 again and my goal was to convert the formal model in book 1 into a TLA+ specification. I still was not understanding the book. Maybe I got to chapter 2, but it didn't go anywhere.

I took another break.

## Six months ago
I am not sure what happened. I started reading the book.  I checked my journal, and I started September 4, 2022.  This time, I did change my mindset though. I told myself things like:

- just enjoy reading the book, don't put pressure on yourself to read X number of pages per day, etc...
- try to understand what the author is trying to tell you
- don't worry about doing less hobby coding

For a long time, I did not want to give up my hobby coding, or do less, but that was required to read the book and fully start to understand the concepts.

## Taking time to learn
There is a lot of math and concepts in the book that I didn't know. This took time and gradually as the concepts came up, I researched and learned more about graph theory and set theory.

I try to picture learning as pyramid. You can start at the top and try to do the hard thing, but maybe you don't know enough to do it, so you should go down the pyramid further and further until you have the foundation, then you can go back up the pyramid.

## Enjoying the vocabulary
For me, the vocabulary of distributed algorithms is quite fascinating. One of the first concepts is safety and liveness. If you search these terms you fill find things like:

- safety: a certain bad thing doesn't happen
- liveness: a certain good thing eventually happens

This is true, but this is not all that these mean. Safety is guarantees or invariants by the system state, actions, and transitions to new state. Safety can be expressed as trace properties. Traces are external observable actions of the system. Atomicity is a safety property.

Liveness is the ability of the system to make progress, which is the eventual good thing. Fairness is a liveness property. There is low-level fairness, which is the ability for processes of the system to take steps, and high-level fairness, which is the fair granting of processes to take steps.

## About a month ago
I watched the first two TLA+ videos, and the concepts where no longer foreign. Now, the videos have different meaning, and are more about how to express the concurrency and math concepts in the specification, not "what are the concepts and use the videos to learn the concepts."

## Now
It is now February 3, 2023, and I am on page 425 of 827 pages, so I am half way.

## Conclusion
I think the difference was enjoying what you are doing, and taking the time to learn.

## What Next
I plan to continue reading book 1. I may take a break to finally write a TLA spec from a model in the book, but I am going to wait and see. I don't want to lose momentum.

## Thank you to the authors
I am thankful to the authors for writing these books and sharing them with us. I have had two people in my career that I consider mentors. I learned a lot from them. When you read someone's book, if it is the right book, it is like having a senior mentor teaching you. You just have to take the time. The dollar amount, say $50 for a book is not high compared to the value that you may get from it. I am truly thankful for this.