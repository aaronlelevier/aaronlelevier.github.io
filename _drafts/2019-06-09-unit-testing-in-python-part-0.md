# Unit testing in Python - Part 0

For this blog, I'm going to code up an example project in Python with unit tests. I'll discuss unit testing while building doing the project. This blog should have been a pre-cursor to [Unit Testing in Python - Part 1](https://aaronlelevier.github.io/unit-testing-in-python-part-1/), so I'm doing it now. Okay, I hope that you enjoy. Let's get started.

# Project Overview

For this project, let's create in Python objects AWS IAM Roles and Policies. Policies can be inline to a single Role, so only that Role can be related to that Policy, or a Policy can be attached to a Role, and then be shared used to configure 1 or more Roles. Let's start with these initial objects. We can add more detail later.

# Design first before writing code and tests

Okay, at this point, I thought that I was ready to start coding up an initial file and tests. Then, I looked up the AWS IAM documentation and some IAM Roles to see what properties they define to make sure that this blog is as accurate as possible uses the same naming.

I first thought that we will need a single parent class for the Policy and Role objects. Then I looked at the ARN of a single Role. A lot of data is present here. Here is an example ARN and a description of the data it contains:

Example:

```
arn:aws:iam::123456789:role/rds-monitoring-role
```

It contains this data:

- Service - `iam`
- AccountId - `123456789`
- ResourceType - `role`
- Role Name - `rds-monitoring-role`

At this point, a lot more objects have come forward. `Policy` and `Role` are both `ResourceType`'s. There is also an `Account` and a `Service`.

At this point, I have written 2 designs. We can use them in the future. But at first, let's make sure that our objects can satisfy a simple requirement. They should be able to generate an `ARN` from the composite data that we have identified.

# Our first test

Let's ignore the design, and write our first test. We don't know how the production (prod) code will be implemented. We do know what it should be able to do though. We want a `Role` to be able to tell us it's `ARN`.
