---
layout: post
title: Code Elixir LDN 2019
tags: [elixir, erlang, europe, london, functional programming]
---

![Imgur](https://i.imgur.com/NgTGu8u.jpg)

Interesting thing. Do you know that if you go to the conference website, this blog uses the same slug? Here's the link. Or you can trust that the link is the same as the href text below. [https://codesync.global/conferences/code-elixir-ldn-2019/](https://codesync.global/conferences/code-elixir-ldn-2019/)

# Code Elixir London

This blog post is from my conference notes. I took 10 pages of notes. The notes however got soaked by rain inside my backpack because it was raining so hard the next day and I cycled to Richmond Park. They have since dried up pretty good though. Here are notes. They are not in exact cronological order of the speeches because when I dried out the pages the order was messed up. 

Annotated notes may be part 2. For now it was just a lot to copy 10 pages of notes, fixing spelling and typos errors and so on.

# Conference Notes

Here we go :)

## Keynote

understand the team level

review project - understand level

flash cards - improves recall

pair programming (for 3 hours) others can view but don't interupt

teaching - ask for understanding first, listen, then add, not the other way around

flashcards

why? options

positive reinforcement

pair programming - be writing code or code challenge, to understand how to help

mentor - focus on teaching concepts

## Performant String Processing in Elixir - work at Castle

Erlang Term Storage (ets) - like Redis for Erlang. read/writes in constant time. Replace `map` with `ets:table`

[streams](https://hexdocs.pm/elixir/Stream.html) - read data as a stream and only split 1x

iolists - can call print 1x instead of per line. List of strings vs. list of references

Thought Process

- confirm problem
- set goal
- create benchmark
- iterate on changes
- consider tradeoffs

can't pass a `ets:table` between processes

can pass a `map` between processes

binary compile pattern - for pattern matching strings

Unix Interface Design Patterns - book

dtrace - to fully trace system calls

nible csv - csv paring library

## Elixir for IoT by James

everything that is a physical IoT thing is a process

have a durable message store

John Hughes - Lambda Days talk Feb 2019 - also IoT related

communication is all using binary

Gattling - load testing for Users

Mocks - testing devices - use mocks for send / receive to IoT device

Basher

Akka - other async language

The Little Typer - book

Nerves - for embedded devices

IoT <---> Cloud <---> Demand Response Predictor

1984 - by George Orwell - book

## Type Classes and Programming Vocabulary - Erlang Solutions, Michael

productive / inspiring - did a venn diagram of the two potentially overlapping but said lets think of then not overlapping

Vocabulary

- Semigroupoid
- Contravarient
- Monad
- Comonad
- Traversible
- Monoid
- endofactors
- functor
- Applicative

Type Class - is the interface

Functor - an iterable that a func can be applied to. Should return the same number of items. Traversible

Brookly Zelentak @ espede Elixir

Words

- GenServer
- Supervisor
- Process
- Actor
- Enum
- Stream
- Task
- GenStage

design patterns

put all impure functions in a module called `effects`

learn the concepts and words then apply them

## Resisting object Oriented Programming - works at MailChimp

hegemony - vocab word - means someone dominating - can be physical or by concept

Gang of Four - design patterns

LU Cache - least recently used Cache

Factories - there are faults

## Hold My State

always initialize with a default state

Calling

- process calculates and returns a value each time before accepting another message
- provides psuedo back pressure - if process has to answer back before accepting more work

Casting

- send messages + don't wait for reply
- request values whenever
- kill process + clan up if don't respond after 10 sec for example

Workers

- (I missed this part of the talk)

## Event Sourcing in Elixir

Everything that occurs is recorded as a Domain Event and saved in Event Store

Process can subscribe to the Event Store

Read Stores - can be created to organize data for use by API, UI, etc...

Language for Producing Types

- [Coq](https://en.wikipedia.org/wiki/Coq)
- [Agda](https://en.wikipedia.org/wiki/Agda_(programming_language))

## Design

Pure Func - maintainable, can run in parallel

Keyword List - Elixir type, Erlang record type?

Types

umbrella application - allow for plug + play, dependency injection, ubiquitous language, releases, delete ability

Why not umbrella? - if project is small, start with monolith, avoid circular dependencies until business domain is known

Interface programming

Struct for create - structs give compile time guarantee, type checking

| Interface        | Business Logic |
|------------------|----------------|
| impure functions | pure functions |
| create ->        |                |
|                  | <- struct      |
| struct ->        | -0             |

GenServer

Phoenix

Ecto

Debuggging

## UI Testing with Hound - by Vanessa Lee from Interactive Vacations

to do Selenium tests using Elixir

target elements, xpath

use execute scripts - to call Javascript to input text in to a form

take screenshot, move mouse, keystroke

Property Based Testing - book

Can do this testing for checking various different inputs to the same form, func etc...

## The Alchemists Code

3-7 years to become a senior engineer

Painting Analogy

- work in teams
- use templates - frameworks

Phoenix

Absinthe

Separate a Project by Context

Contexts are like a microservice, have their own domain and should be isolated from other Context

Can draw a dependency graph between models

model is aware of another module by importing, sharing a struct, then that's a dependency

context - could also be though by directory

Should be NO cross context communication

Service -> Model

Service -> IO -> Model

Pyramid, from top down could be thought of:

- Service
- IO
- Model

Example path pattern to use:

`mylib/*/(model|io|service)/*`

Model - Actors, pure functions

IO - for impure functions, calling anything external

Service - all business logic

Domain Modeling Made Functional - book

Restart GenServer w/ new State

state -> perform -> new state

move impure functions to boundry. This is the:

- interface
- most public functions
- 1st function called that calls other functions

purity

types

organization

architecture - event based architecture - all requests sent to broker and distributed from there

aka Brokered approach

confident code

- unit test
- integration test (don't mock db)

libs

- credo
- formatter
- dialyzer

smoke tests - selenium

test coverage

property test

debug

tracing

discuss concepts

- what - question
- why 
- how

## Error Free Elixir

design code w/ error handling in minde

source of errors

- users
- other services
- infrastructure
- developers

let it crash

error tuples

Heuristics

- reasonable defaults
- declarative operations
- don't fight the real word

think idempotent - if get cancel command 2x let the 2nd one pass because the goal to cancel has been achieved so it's not an error

handle the error correctly for what it is

understand if it is an error, why did it happen

can we recover from the error

A Philosophy of Software Design - John Ousterhout - book

The Art of Destroying Software - Greg Young - talk 

Understand real use cases of the application in order to reduce error handling + understand what reall is an error or not

## Build a CLI in Elixir

Why CLI

- light weight
- can utilize OS
- infrastructure level features
- reproduceability

run app, output data to JSON, can then run JSON as an event command, etc...

Developer Experience - robust, speedy, visually intuitive

Option Parser - Elixir argument parsing module

use colored text in terminal

whne debugging - can reference same script + call with arguments reference secrets for environment variables in prod

don't reinvent language - use standard commands

stdout / stderror - be able to easily customize logging

Exit Codes - don't use 0/1 - have an error code per failure type

fail fast

## lightening talks

exercism.io - structured series of programming exercises

community - social platform for sharing thinking

stackshare.io - share software stack

portmidi - Elixir midi music player that uses LiveView for SVG UI

umbrella application with a single port

- don't do it in test
- initialize at compile time

PubSub in Postres

```
LISTEN channel;
NOTIFY chanel;
```

Can have an Elixir process listening for Postgres Notifications

Ecto-sandbox - use to proxy to the database when locally testing a frontend app 

- creates a separate DB for testing
- data API requests can be sent form App to DB

ex_machina

- natterbox
- red matter

kubernetes

- Telemetry
- Prometheus

## closing keynote

The River by Bruce Tate from grox.io

author

- programming phoenix
- dsesigning elixir otp systems

organization

lifecycle - get failover for free; turn off + on again

concurrency - modeling real life objects

Platformatec, Bleacher Report, Dockyard - Chris, Le Tote, Erlang Solutions

Erlang Ecosystem Foundation - way to get involved

Garden Bot - IoT Elixir bot for watering garden

Texas Whitewater - by Steve Daniel - book

Stewardship Made Practical - by Stewart ? - talk

Outside Magazine - has a contest for the best places to live Outdoors

Regents Canal - places to go

> "Elixir is done" - Jose Valim

Syntax is stable

libs

- LiveView
- Scene
- Nerves

vote with your values, dollars, time, companionship

# Speaking with the people

I am kind of bad with names. I started talking to someone about cycling. He recommended that I go to Richmond Park the following day. That's what I ended up doing, and it was amazing. There's deer with giant antlers, 2 lakes. It was great.

Everyone was so nice. Herb, it was great to talk with you, your friend, James, and the others. 

We talked about the how the infix operator isn't efficient for appending to the tail of a list. It is also the case for removing items from the tail of a list and the complexity is N square.

Everyone was so kind and welcoming. 

## Advice I got

Francesco, it was great to meet you. Thank you for some road map advice to consider after I'm done with Programming Erlang 2nd Ed., Joe Arstrong's book.

- Erlang Programming: A Concurrent Approach to Software Development
- Defining Scalability for OTP

First learn concurrency, a process can only change it's own state

Next, processes are an event handler, finite state machine. Client server, supervisor, worker, and so on

Glamorous Toolkit - editor

Purely functional data structures

# Conclusion

The conference was a very unique oppurtunity and I appreciate it a lot. I hope to go to Code Mesh SF in March 2020. Or maybe the RabbitMQ conference.