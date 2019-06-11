---
layout: post
title: Test Driven Development with Python
tags: [Python, Unit Testing]
---

For this blog, I'm going to code up an example project in Python with unit tests. I'll discuss unit testing while building doing the project. This blog could have been a precursor to [Unit Testing Concepts with Python](https://aaronlelevier.github.io/unit-testing-concepts-with-python/), which discusses more concepts then application. Okay, I hope that you enjoy. Let's get started.

# Project Overview

For this project, let's create in Python objects AWS IAM Roles and Policies. Policies can be inline to a single Role, so only that Role can be use that Policy, or a Policy can be attached to a Role, and then the Policy can be also used with other Roles. Let's start with these initial objects. We can add more detail later.

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

At this point, I have written 2 designs. Here are the 2 designs. The first is in blue pen, the second in pencil. I forgot my rule, always diagram in pencil!

![Imgur](https://i.imgur.com/b4ZvE73.jpg)

We can use them in the future. But first, let's make sure that our objects can satisfy a simple requirement. They should be able to generate an `ARN` from the composite data that we have identified.


# Our first test

Let's ignore the design for now and write our first test. We don't know how the production (prod) code will be implemented. We do know what it should be able to do though. We want a `Role` to be able to tell us its `ARN`.

All of this code lives in [python-unit-testing-examples](https://github.com/aaronlelevier/python-unit-testing-examples). Follow the [Project Setup](https://github.com/aaronlelevier/python-unit-testing-examples#project-setup) instructions in the README to install the project and code along with this blog.

Here's the test:

```python
import unittest
from iam import Role

class RoleTests(unittest.TestCase):

    def test_arn(self):
        name = 'rds-monitoring-role'
        role = Role(name=name)

        ret = role.arn

        assert ret == 'arn:aws:iam::123456789:role/rds-monitoring-role'
```

Then run `py.test` from the project home directory to run the test suite.

There's no prod code written at this point. Running the above test only with no prod code, will result in this error:

```
Traceback:
tests/test_iam.py:3: in <module>
    from iam import Role
E   ImportError: cannot import name 'Role' from 'iam' (/Users/aaron/Documents/github/testing_example/iam/__init__.py)
=================================== 1 error in 0.15 seconds ===================================
```

Let's add some initial prod code and see what happens. Let's add this code:

```python
class Role:
    @property
    def arn(self):
        pass
```

And re-run `py.test`. This results in the error:

```
    def test_arn(self):
        name = 'rds-monitoring-role'
>       role = Role(name=name)
E       TypeError: Role() takes no arguments

tests/test_iam.py:10: TypeError
================================== 1 failed in 0.16 seconds ===================================
```

This is because we did correctly add a `Role` class in the `iam/__init__.py` file. But, classes have a default empty constructor of: `def __init__(self):pass` that accepts no arguments, but our test passed in a `name` argument. Let's add a constructor to accept the `name`. Our goal of the test here is to test the `ARN`. Let's update our code to:

```python
class Role:
    def __init__(self, name):
        self.name = name

    @property
    def arn(self):
        pass
```

Re-run `py.test` and we now get the error:

```
self = <test_iam.RoleTests testMethod=test_arn>

    def test_arn(self):
        name = 'rds-monitoring-role'
        role = Role(name=name)

        ret = role.arn

>       assert ret == 'arn:aws:iam::123456789:role/rds-monitoring-role'
E       AssertionError: assert None == 'arn:aws:iam::123456789:role/rds-monitoring-role'

tests/test_iam.py:14: AssertionError
================================== 1 failed in 0.09 seconds ===================================
```

This is good! All of our previous test fails were due to **test setup errors**. This is an important concept.

## Test Setup Errors

A test setup error is different then a prod code error. This is an error like we just saw. Maybe it's a missing import or an undefined variable in the test code. Either way, it's a problem with the test code and can be solved by setting up the test correctly and only changing test code.

To fix the first test setup error, we did what is known as **method stubbing**.

## Method Stubbing

Method stubbing is important. We do this so we can call our prod code correctly and know that everything is connected, but not returning the value that we want to test for. For compiled languages like Java, this has to be done, or else the code won't compile. Methods must be stubbed in order to run initial tests before implementing the method body.

Python is more forgiving because of dynamic typing, but it is just as important to stub methods when testing. This tells us that we correctly called or prod code from the test.

After our two test setup errors were fixed, we got what is known as a **graceful test failure**.

## Graceful Test Failure

A graceful test failure is when the test finally fails on an assertion. We have set up the test and called our prod code correctly, and now the only thing wrong is that the value that we are supposed to get back. Now we can implement the prod method.

Let's now define an initial implementation for the prod method.

## Initial Implementation

There are a lot of things wrong with this implementation, but let's ignore that for a second and see if this allows our test to pass. Here's the updated method:

```python
class Role:
    def __init__(self, name):
        self.name = name

    @property
    def arn(self):
        return f'arn:aws:iam::123456789:role/{self.name}'
```

Run `py.test` and now we get:

```
tests/test_iam.py .                                                                     [100%]

================================== 1 passed in 0.05 seconds ===================================
```

*Commit!* Our tests have now passed. We don't have to `git commit`, that's just a joke. Or test have passed though for the first time. We succeeded here in a couple of ways:

- we used the `self.name` attribute defined on the class
- we *failed first*. By failing first, when the test passed later, we know it's the code that we added that caused it to pass
- we *failed fast*, a favorite tech cliche! The change was quick, and we got to see the test pass

There's still a lot to be desired though. Thinking about our initial design and the objects that we identified, and the method body of the `arn` property, here are some thoughts:

- `AccountId` shouldn't be hardcoded in a single method body for `Role.arn`. What about `Policy.arn` when we implement that.
- same for `role`. This is hardcoded. We know that this is the `ResourceType`
- same for `iam`. This is hardcoded and this is the `Service`

Before going on to the next section, I did `git commit` and `git tag` at this point for the example code repo. You can check out to the git tag to this point by running:

```
git checkout first-test-pass
```

# Improving the Implementation

Our test is already defined at this point. We can make prod code changes to improve the implementation. This will make the prod code better.

From our design, we might consider our class as a `Resource`, and it should have a required `resource_type` attribute, equal to `'role'` in this case. We can use the Python [abc](https://docs.python.org/3/library/abc.html) module to require a property on a class. Let's update the code:

```python
import abc

class AbstractResource(abc.ABC):

    @abc.abstractproperty
    def resource_type(self):
        pass


class Role(AbstractResource):
    def __init__(self, name):
        self.name = name

    @property
    def arn(self):
        return f'arn:aws:iam::123456789:role/{self.name}'
```

We run `py.test` and get this error:

```
self = <test_iam.RoleTests testMethod=test_arn>

    def test_arn(self):
        name = 'rds-monitoring-role'
>       role = Role(name=name)
E       TypeError: Can't instantiate abstract class Role with abstract methods resource_type

tests/test_iam.py:10: TypeError
================================== 1 failed in 0.07 seconds ===================================
```

This is the error that we want. We are using the **test feedback loop** here.

## Test Feedback Loop

![Imgur](https://i.imgur.com/sms9k2H.png)

The test feedback loop means using the development workflow of changing code, run tests, make changes, test, write new test, prod code change, etc... It is:

> the feedback in between writing test and prod code that let's us know that the code is doing what we want

The test feedback loop *exists in manual testing!*. It is more time consuming to do manual testing though, so if this can be done as much as possible through automated testing, and unit testing because these are the cheapest tests to run, then this is the goal.

Let's update the prod code:

```python
import abc

class AbstractResource(abc.ABC):
    @abc.abstractproperty
    def resource_type(self):
        pass


class Role(AbstractResource):
    def __init__(self, name):
        self.name = name

    @property
    def resource_type(self):
        return 'role'

    @property
    def arn(self):
        return f'arn:aws:iam::123456789:{self.resource_type}/{self.name}'
```

The test should now pass again.

# Move out the rest of the data

Let's move out the rest of the data in the method that probably doesn't belong there. We have lots of choices on how to add configuration to our project. It will vary in complexity. Here's a way to keep it hardcoded in code, but improve the variable scoping:

```python
import abc

ACCOUNT_ID = '123456789'


class AbstractResource(abc.ABC):
    @abc.abstractproperty
    def resource_type(self):
        pass


class IamResourceMixin:
    service = 'iam'


class Role(IamResourceMixin, AbstractResource):
    def __init__(self, name):
        self.name = name

    @property
    def resource_type(self):
        return 'role'

    @property
    def arn(self):
        return f'arn:aws:{self.service}::{ACCOUNT_ID}:{self.resource_type}/{self.name}'
```

Here we have made `ACCOUNT_ID` a global. This could also be loaded as an environment variable or dynamically, but the point is that it's scope is larger than the initial method.

We created a mixin class `IamResourceMixin`. The `service` is defined here. This pattern is the **composition pattern**.

## Composition Pattern

The composition pattern combines pieces of functionality in order to make a fully functional class. The classes used to build the concete class may not have all of the functionality to exist on their own, and this is okay. Piecies of functionality can be defined separately, then shared by the classes that need them.

This pattern is used a lot in [django-rest-framework](https://github.com/encode/django-rest-framework/blob/master/rest_framework/viewsets.py) to define API endpoints as classes that support different HTTP request types, where a single HTTP request type is a `Mixin`.

# Maybe change the implementation to this

We could further change our working code example to:

```python
import abc

ACCOUNT_ID = '123456789'


class AbstractResource(abc.ABC):
    @abc.abstractproperty
    def resource_type(self):
        pass


class IamResourceMixin:
    service = 'iam'


class AbstractIamResource(IamResourceMixin, AbstractResource):
    pass


class Role(AbstractIamResource):
    def __init__(self, name):
        self.name = name

    @property
    def resource_type(self):
        return 'role'

    @property
    def arn(self):
        return f'arn:aws:{self.service}::{ACCOUNT_ID}:{self.resource_type}/{self.name}'
```

Here, we put the `Mixin` and `Abstract` class in a single class, and `Role` inherits from that class. This might be a nice change, so when `Policy` is added, it can inherit from a single class, instead of the `IamResourceMixin` and `AbstractResource` class, which Policy will need both, since it also defines an `'iam'` service with a `resource_type`.

I did a code commit here. To git checkout to this point, run:

```
git checkout first-mixin-added
```

# Challenge

Okay, now, here's the *challenge!* Implement a `Policy` class with a test for it's `arn` attribute. The `arn` should equal:

```
'arn:aws:iam::123456789:policy/DenyIAMAccess'
```

How did that go?

## Policy class with tests and refactored

I implemented the `Policy` class and also refactored. To see the new code, run:

```
git checkout add-policy-class
```

There's been lots of code blocks, so at this point, I did a few changes at once. First, the test code:

```python
class PolicyTests(unittest.TestCase):

    def test_arn(self):
        name = 'DenyIAMAccess'
        role = Policy(name=name)

        ret = role.arn

        assert ret == 'arn:aws:iam::123456789:policy/DenyIAMAccess'
```

Very similar to the `RoleTests.test_arn` method.

For the prod code:

```python
import abc

ACCOUNT_ID = '123456789'


class AbstractResource(abc.ABC):
    @abc.abstractproperty
    def service(self):
        pass

    @abc.abstractproperty
    def resource_type(self):
        pass

    @property
    def arn(self):
        return f'arn:aws:{self.service}::{ACCOUNT_ID}:{self.resource_type}/{self.name}'


class AbstractIamResource(AbstractResource):
    def __init__(self, name):
        self.name = name

    @property
    def service(self):
        return 'iam'


class Role(AbstractIamResource):
    @property
    def resource_type(self):
        return 'role'


class Policy(AbstractIamResource):
    @property
    def resource_type(self):
        return 'policy'
```

So, I had the `PolicyTests` code in place. I got it to pass by basically copying the `Role` class and renaming the `resource_type`. There was a fair amount of duplication though. I started moving things around, and came up with the above code. I think this is better for a few reasons:

- the `arn` property exists on the `AbstractResource` class. This is better. All AWS Resources have ARNs, so it makes sense for this to be defined on `AbstractResource `
- `service` is now an abstract property. This is better because Services should have to define what kind of Service that they are.

**Abstract** is an important concept here.

## Abstract and Concrete Classes

Abstract classes can't be instantiated from. They are meant to be inherited from. In the above example, the `arn` property is being accessed, and this property references a `resource_type` and `name` attribute. These are defined on the concrete classes, Role and Policy.

If we were to instantiate a `AbstractIamResource` and access it's `arn` we would get an error.

# Conclusion

This blog may have been better named:

> scenic stroll through testing and code design

I kind of took some side trips away from just testing, but I hope that you enjoyed it and they made sense in the context of testing and added value.

In this blog we learned how to:

- write test code first
- test setup error
- test stub
- graceful test fail
- test feedback loop
- composition pattern
- code challenge
- abstract class
- concrete class

# Next

We didn't quite get to inline vs. attach Policies. There are more testing concepts to cover next as well. I will extend upon this example and cover more concepts in the next blog.
