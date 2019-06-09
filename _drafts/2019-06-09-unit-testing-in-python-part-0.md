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

Next, for the first test setup error, we did what is known as **method stubbing**.

## Method Stubbing

Method stubbing is important, so we can call our prod code correctly, and know that everything is conected, just not returning the value that we want. For compiled languages like Java, this has to be done, or else the code won't compile. Methods must be stubbed in order to run initial tests before implementing the method body. Python is more forgiving because of dynamic typing, but it is just as important to stub methods when testing.

After our two test setup errors were fixed, we got what is known as a **graceful test failure**.

## Graceful Test Failure

A graceful test failure is when the test finally fails on an assertion. We have setup the test and called our prod code correctly, and now the only thing wrong is the value that we are supposed to get back is wrong. Now we can implement the method.

Let's now define an initial implementation of or prod method.

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

*Commit!* Our tests have now passed. We don't have to `git commit`, that's just a joke. Or test have passed though for the first time. We succeeded here in a couple of ways.

- we used the `self.name` attribute defined on the class
- the change was quick, and we got to see the test pass

There's still a lot to be desired though. Thinking about our initial design and the objects that we identified, and the method body of the `arn` property, here are some thoughts:

- AccountId shouldn't be hardcoded in a single method body for `Role.arn`. What about `Policy.arn` when we implement that.
- same for `role`. This is hardcoded. We know that this is the `ResourceType`
- same for `iam`. This is hardcoded and this is the `Service`

Before going on to the next section, I did `git commit` and `git tag` the example code repo at this point. You can check out to the git tag at this point by running:

```
git checkout first-test-pass
```