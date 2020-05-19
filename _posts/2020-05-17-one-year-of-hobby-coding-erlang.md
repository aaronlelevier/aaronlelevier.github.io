---
layout: post
title: One Year of Hobby Coding Erlang
tags: [Erlang]
---

I am Celebrating 1 year of hobby coding Erlang as of May 15, 2020. I was talking with my wife and a couple of things stood out about reaching this milestone. There's some important things that I learned, and some of these have been outside of programming. There are also some bridges that I have yet to cross and next steps that I'd like to list.

## How Erlang compares to other languages that I've surveyed

The language that I code in every day is Python, but I try to make a point to learn other languages. Besides SQL, which is the first language that I learned, and used at work for 3 years before getting into Python, I have used a few other languages, but I have never crossed the 1 year mark.

### Java

I used for 10 months with Android, and eventually quit when I realized that I'd have to do UI design if I wanted to build an app. I quit around the time that Android announced support for Kotlin. I think what first got me into Java was reading *Test Driven Development* by Kent Beck, which is in Java, and then coding up the examples, and I wanted to then learn the language.

### Swift

Prior to learning Java, I spent 8 months using Swift. I mostly did online courses, and never really made anything other than the demo apps, and one simple [SpriteKit](https://developer.apple.com/spritekit/) game that my daughter was the only one that played. It was about a bunny that hopped to collect coins, and I purchased the images from [GraphicRiver](https://graphicriver.net/).

### C++

My wife laughed when I told her about this one. I spent 2 weeks learning C++. I bought the book *Accelerated C++*, and was driven to learn C++ because machine learning frameworks use C++ under the hood, and the developer API is in Python, so I thought that I should learn it, but, it only lasted 2 weeks.

### Objective-C

This predates all the above languages, and was after I learned Python. I think  that I spent 2 months with Objective-C, and did one book, but forgot all of it.

### Erlang

Now Erlang. I had bought Joe Armstrong's book, *Programming Erlang 2nd ed*. because I wanted to learn Erlang for a while, but then held onto the book for 6 months and didn't read it. Then in May of 2019, I learned about Joe Armstrong's unexpected passing, and felt compelled to read his book.

The book is really good. It covers the whole language and Erlang OTP. One of my favorite parts of the book is in the chapter on Maps. I tried to code up the examples, and the code wouldn't compile. I started googling to see what I did wrong, and I guess Joe had included experimental syntax in the book, that didn't  get accepted by the Erlang language board. I could feel Joe's personality when I read the book.

So then what happened?

## More than just one Erlang book

In July of 2019, I had the pleasure of attending Code Elixir LDN 2019. This was the first time that I had been exposed to the Erlang/Elixir community.

Some of the ideas were very different. At the conference, I listened to some of the best talks that I have ever heard, fresh with ideas that were new to me.

I attended the happy hour after and got to hang out with the speakers. Then the founder of [Erlang Solutions](https://www.erlang-solutions.com/home.html), Francesco Cesarini, approached me and asked me how I liked the conference. I told him about my Erlang journey, and how I was half way through the *Programming Erlang* book. Francesco said:

>  That's good. You're reading Joe's book. After your done with his book, you should read my book.

I listened to what he said, but let me get to that in a minute.

So in November/December 2019, I finished the *Programming Erlang* book and thought that I was ready to build software using Erlang. I started a project using [Erlang Cowboy](https://github.com/ninenines/cowboy), a "Small, fast, modern HTTP server for Erlang/OTP", and got stuck, so I contacted the creator of Cowboy, Loïc Hoguin, for consulting. I booked 1 hour, and thought that it would be worth it if I could make this software idea that I had. We ended up working together for 30 minutes, and it was pretty obvious to me that I wasn't ready. We exchanged a few emails after that, and I told Loïc that I wasn't sure if I needed the other 30 minutes of consulting because I needed to learn Erlang first. He told me:

> Glad you're still enjoying Erlang! It is indeed pretty pretty big.

After that, I quit the software project and started reading Francesco's book *Erlang Programming*. This time taking my time to let the language and concepts soak in, and not force myself to learn it with the goal of building something, as I did with the first book.

## Where am I at today

As of today, I'm on pg. 290, ch-12 of *Erlang Programming*, and have gotten back to Erlang OTP. I am taking my time to learn more about Erlang, distributed programming and functional programming.

I have mostly been coding `gen_server`'s at this point, and some one or two `gen_statem`. I am about to add `supervisor`'s to the mix.

I started reading the book *Distributed Algorithms* by Nancy Lynch in conjunction with *Erlang Programming* by Francesco Cesarini. Today, I finished coding the Leader Election LCR algorithm in Erlang. [Here](https://github.com/aaronlelevier/syncnet/tree/lcr) is the commit tag, so I know what happened later!

I am also reading *The Litter Typer*. This book is about dependent types. It was recommended by one of the speakers at Code Elixir LDN 2019. I'm enjoying it so far, and it should be valuable to go along with the other learning.

I am learning more about functional programming (FP). After using Erlang OTP more, and some of the behaviors, I plan to spend more time on FP.

## What has been really cool

Erlang and FP in general makes you think differently.

I was explaining Erlang to a friend and relating it to Python and Object Oriented Programming (OOP), and I said:

> In Erlang each process is like an object instance, but those objects are all running processes, and they communicate concurrently.

If that's not cool, I don't know what is.

When coding in Erlang, you have to think about concurrency, and if something is timing related. I have written code with tests, where the test needs to wait for a "done" message from a certain process before proceeding. What you end up with is a partially synchronous system, which makes up most systems.

Erlang has all of the primitives for a highly concurrent fault tolerant system, and being able to build stuff with these primitives is a lot of fun.

## What's next

Finish Francesco Cesarini's book, *Erlang Programming*.

Fully learn Erlang OTP and all the behaviors.

Write a simple Erlang App using OTP.

I want to learn how to use the Erlang debugger, and not just log statements.

Ourside of Erlang, I want to continue to read the *Distributed Algorithms*'s book. I first put "finish", but this is a big book!

For FP, I want to learn more [concepts](https://degoes.net/articles/fp-glossary) and about [functional design patterns](https://www.ibm.com/developerworks/library/j-ft10/index.html).

## Conclusion

I am definitely not where I thought that I would be. I thought that I would be building full fledged Erlang applications by now, but I am okay with that. I am still having fun, and don't plan to on changing hobby languages quite yet. For a minute, the thought entered my mind, "how about trying Haskell." But, then I thought about all of the time that I've spent with Erlang learning the primitives, and it's better to stick with it.
