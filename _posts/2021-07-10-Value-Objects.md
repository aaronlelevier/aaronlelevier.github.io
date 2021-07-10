---
layout: post
title: Value Objects
tags: [DesignPattern]
---

Hello! This blog discusses the pattern of value objects as I use them, why they are useful, and some real world use cases.

Hello, my name is Aaron Lelevier, and I hope that you enjoy the blog and come away with a new tool (design pattern) in your tool chest.

## What is a Value Object

Let's start with a definition. A value object (VO) is an object that stores some data that is logically grouped together.

The VO can then represent an object in the business domain, concept, or rule(s). 

The VO should be properly constructed, so it recieves all arguments when it is initialized and does not call separate methods at a later time to mutate itself.

The VO should be read only. It can potentially make API reads to load data, possibly lazy load, and this should be idempotent.

The VO can read by other objects that understand its type (interface).

The VO should not have methods for API write calls or writing to a database. After all, it is a value.

## Proper Construction

The Proper Construction concept is powerful because it allows an object to be immediately useful upon initialization. I have worked in codebases where objects have to call 2 or 3 methods before they have all of their data. Proper Construction removes that.

Some programming languages, use immutable objects, for example [Erlang](https://erlang.org/doc/apps/erts/users_guide.html). In these languages the new object needs to be assigned to a different variable. Immutability removes the mental overhead of needing to confirm if an object has been mutated, or worse reassigned.

## Value Objects are for Reading

The VO can be a business object, a concept, rule, etc... but it should be a noun. The VO can then be read by other objects in the system, like those that do API writes.

## Program to an interface not an implementation

The VO should have a Type (Interface). This will allow creation of an object with the same interface in different circumstances that are then understood by other objects in the system.

## Value Objects and Eliminators

An Eliminator, from the book [The Little Typer](https://thelittletyper.com/), is a function that takes a value as an argument. An Eliminator then must understand the value's type. This pattern scales well if the VO's complies to an interface, and then the Eliminator can be programmed to work with that interface.

## CQRS

VO's and Eliminators also natrually reinforce [CQRS](https://martinfowler.com/bliki/CQRS.html) or Command Query Resource Separation, which is the pattern of separating code for reading and writing. The VO's should only read data and the Eliminators, not all but some, are then used for API writes.

## Real World use case for Value Objects

Here is a real world example. Let's say we have a HR system that is responsible for storing employee information.

The first time an employee is hired, the VO in the system requires all their information to be properly constructed. The VO's type is Employee. The Empolyee VO is then passed to an Eliminator that handles database writes, and the new employee is added to the HR system. We have followed CQRS.

Then, the employee is granted access [AWS](https://aws.amazon.com/). We will need their info to grant them access in AWS. Since all of their information is in the HR system, we only need a unique identifier, like their work email, and we can construct an Employee VO of the same type by querying the database. The Employee VO is then used to create as a User in AWS and is provisioned via [Cloudformation](https://aws.amazon.com/cloudformation/), which handles writing and updating resources in AWS. We have followed CQRS again, and this time the API writes were done by Cloudformation.

## Conclusion

Thank you for reading. I hope that you can find the value object pattern as useful as I have. Cheers!
