---
layout: post
title: Unit Testing in Python - Part 1
tags: [Python, Unit Testing]
---

# Overview

This is going to be a multi-part blog. Testing is too big of a subject to cover in one blog. These blog(s) will cover what unit testing is and some thoughts and concepts on unit testing in order to best apply it. I will also show code examples and discuss them.

# Introduction

Let me start out by introducing myself and the person that got me started on testing.  Hi, my name is Aaron Lelevier. I’ve been using Python for 6 years, 5 years professionally. Prior to that and with some overlap, I did MsSQL for 3 years. 

The person that got me started on unit testing was [Toran Billups](https://twitter.com/toranb). This was 4 years ago. I was hired on at Big Sky Technologies as a backend Python Django Developer on a team of 3, myself, [Scott Newcomer](https://twitter.com/puekey), who did frontend EmberJs, and Toran Billups, who’s background is in Javascript and Test Driven Development (TDD), as Tech Lead. I didn’t know this at the time, but Toran had only agreed to come on the team as Tech Lead if the team embraced testing. 

Toran made a big impact on me. I’d like to share some of his quotes, and give examples with how they apply.

# Quotes from Toran

Let me start off with a funnier quote. We had been into our project for about 3 months. I was asking Toran about his thoughts on testing for some concept or topic. Then, Toran says to me:

> “You know, discussing testing is like discussing religion.”

This is pretty interesting. I have come across this thought a lot. Some people are against testing and they will fight it. Other people are on the reverse side, and are testing pedantics, and brutally enforce every little thing be tested. Our team was growing while I was at Big Sky, and we wanted to keep our culture of TDD, and people that we discussed this with said “good luck”. It is hard to keep testing a first priority.

Another quote from Toran was:

> “Test first or test last. I don’t know about you, but once I’m done writing my code, I don’t want to write tests. I want to go and do the next thing, that’s why I write my tests first.”

This is true, but also for other reasons. After a feature is considered working, writing tests for it seems laborious. The other reason to test first though, and the real reason I would argue, is to see if the functionality currently exists. If you can write a test that something should occur, and it doesn’t, then when you write the production (prod) code for this, and the test passes. Then you know that it was the code you added that made it work, whereas before it didn’t. The testing cycle proves that.

# Is this a TDD blog?

No, it is not. I bring it up as part of the previous quotes, and from some of what Toran taught me. Test First has its place. It is not the only way to test though. 

Sometimes what you are doing is too unknown, so writing tests for something you’ve never done before is too slow, or simply doesn’t work. An example of this is learning a new programming language or framework. It’s much easier to learn by writing code to do the thing then to write tests. For machine learning, this is also true. Some parts of machine learning like data transformations are good places for heavy testing and even TDD. Making a model with layers and iterating on that model may not be. 

There is the concept of Defect Driven Testing (DDT). This is when a defect is discovered, then a test can be written to capture that defect (or bug), so it won’t resurface. Here, the testing scenario isn’t known ahead of time, or else the bug wouldn’t have existed, so TDD doesn’t apply.

Okay, so what is the goal of testing?

# Goal of Testing

This is best said by this quote from Toran:

> “You don’t know if something works unless you have a test that says it does.”

This could be an automated test, whether it’s a unit or integration test. It could be a manual test by someone on the QA team or it could be your customers testing in Prod by using your product. Ideally, it’s some sort of automated test though because these are the cheapest test to run, and we don’t want our customers to be the first to test and discover bugs, then have to report them and wait for them to be fixed!

Let’s start with an overview of unit testing and see a simple application of it in Python for this first blog. 

# Unit testing overview

What is a unit test?

A unit test is a test for a single piece of functionality in your code. It would be a test for a single function that tests a single code path. If this function, for example, has an if/else block, you would want a unit test for the “if” code path in the function, and a separate unit test for the “else” code path in the function. 

Unit tests are cheap. They are the quickest tests to write and fastests tests to run. They won’t prove that your whole application works. They prove that pieces of the application work in isolation with certain inputs and then verify the outputs.

Here is the famous Test Pyramid.

![Imgur](https://i.imgur.com/RhOhPqg.png)


## Unit Tests

Unit tests are at the bottom. This should make up the bulk of your test suite. At Google, they use this ratio, and unit tests make up 70% of their total tests. I heard about this from a Google I/O talk.

## Integration Tests

These tests start to connect functions and bodies of code together. They don’t stand up the whole application and test though. They are above unit tests for individual pieces and below whole application automated testing.

## UI Tests (Functional Tests)

UI Tests, or Functional Tests if there is no UI, are automated tests of the whole application. This would be [Selenium](https://www.seleniumhq.org/projects/webdriver/) for automated UI testing of a web site, [Appium](http://appium.io/) for mobile apps, and so on.

## Level of Tests as a Concept Vary by Situation

This is a very good talk on how to test infrastructure.

[![Imgur](https://i.imgur.com/OKmmbZ2.jpg)](https://www.youtube.com/watch?v=jiWRTuF4yXk)

In this talk, the speaker discusses how infrastructure can only be fully tested by deploying it. In this testing paradigm, Unit Tests are then single pieces of infrastructure deployed in isolation with the minimal number of dependencies. Integration Tests starts to connect infrastructure, and Functional Tests test the infrastructure as a whole.

# Unit test in Python

Here is the prod and unit test code from one of my Python projects. Let’s take a look at this code and discuss it.

<script src="https://gist.github.com/aaronlelevier/e53fceeaed8323b76212dbcc8c7079ec.js"></script>


There are two unit tests for the example class and it’s single method. One tests the scenario that all image files in a directory are ordered by name. The other tests the scenario that they aren’t ordered by name and what the outputs of the method would then be.

I’m going to discuss a couple of concepts and mechanics from this example code.

## Concepts

Unit tests are calling prod code to make assertions about the inputs and outputs. A simple example would be if a function multiplies an input value by two, then the unit test would assert if 1 goes in, 2 comes out, if 3 goes in, 6 is returned, etc… 

Inputs may vary. Sometimes functions have defaults or varying number of arguments. In this case, you would want multiple tests to assert the behavior of that function. The above code is an example of this. The prod code only has a single argument, but two situations are being tested.

## Mechanics of Unit Testing in Python

If you go to the Github repo linked in the description of the gist, or you may be able to derive most of this information from the gist. Here are a few things going on.

### The Test Runner

To run unit tests, Python’s unittest test runner needs to be able to discover them. 

I like to put my tests in a directory called “tests” at the project directory level. This is a known pattern. [django-rest-framework](https://github.com/encode/django-rest-framework/tree/master) uses this pattern. Another pattern is to put the tests in the same directory as the prod code file and append “_test” to the name. [TensorFlow Extended](https://github.com/tensorflow/tfx) uses this pattern. I prefer the former because it separates test code from prod code.

The test runner will find each Python file that starts with “test_”. I like to name the test file names with the “test_” prefix, so they are discovered by the test runner, and then use the same name as the prod test file. This makes them easier to keep track of.

The test class should subclass unittest.TestCase. This is because there are setUp and tearDown hooks in the class that can be used.

Each test method in the class should start with “test_”. The test runner will call these test methods and report success or failure. Test classes are just Python classes. They can have other methods for test helpers, etc… and then these would not start with “test_” because they are a helper, not a test method.

### Pytest

The example code is using [pytest](https://docs.pytest.org/en/latest/). I prefer the test syntax of pytest to the standard library unittest methods. Also, pytest gives nice red/green colored highlighting on test output. There is a table in the unittest [documentation](https://docs.python.org/3/library/unittest.html) for the different assertion methods. The testing semantics are the same, just with different syntax.

In the example code, the Python assert keyword can be used to assert if something is truthy or falsy. Assert if equal or not equal, etc…

### Test Class Names

I like to name the test class the same as the prod class, and then add “Tests” to the end. This makes the test method class easy to search for and identify which prod code the test class relates to.

### Test Method Names

Test methods have to start with “test_”. For their actual name, I like to have the name of the prod method that I’m testing in the test method name. This makes it easier when searching for tests for a given method. 

A co-worker of mine, [Vince Grato](https://www.linkedin.com/in/vgrato/), said to me once, I use rspec for naming tests. He was calling me out because I had named my test methods based on the prod methods and then with a suffix like “true” or “false”, which would be the output that they test for, but the test method name didn’t say anything about what the test actually did. Over time, and now currently, this is how I name my tests. I still like to have the prod method name in the test method name, and then append a description of what the test is doing.

Another co-worker of mine, [Bill Heaton](https://twitter.com/pixelhandler?lang=en), said something similar. He said that when he wants to know how some code or library works, he first runs the test suite, and then reads the method names output by the test run to see what the code is doing. This follows along with what Vince said.

### Format of the Test Method Body

For the test method body, I like to follow the format of:

Test setup - linespace - code being tested - linespace - assertions

This is the format of the test method bodies of the example test code above. This makes it easier to follow and separate initial setup that the prod code needs before being called. Then actual code being called, and finally the assertions for that code.

I believe that I got this from Kent Beck’s book, [TDD by Example](https://www.eecs.yorku.ca/course_archive/2003-04/W/3311/sectionM/case_studies/money/KentBeck_TDD_byexample.pdf), but I am not sure. Either way linespaces can be used to denote meaning in code, and this is a good place for them.

### Test Method Ordering

I prefer to put the test methods in the same order as the prod methods. This makes it easier to relate the prod code to the test code if they follow the same method declaration ordering. 

The above code example is only for a single prod method, but if there were a second method, then the test method would be ordered below the current test methods.

### Test Code Doesn’t Look Like Prod Code

When I worked with Toran, he said this to me one time:

> “Where are all the assertions here. There’s all kinds of missing assertions.”

Toran is really nice. I asked him for constructive feedback one time when we were having reviews, and he only told me positive things, but I could also glean some things that I could improve on even though he was so positive.

That said, the above quote means that I had missed a lot in the test coverage. This stemmed from me thinking that code looks like code and test code looks like prod code. It’s object oriented, has arguments, etc… 

The test in question was asserting return values of an API endpoint. The API endpoint was returning 10-15 fields with data, but my test was only testing that 2-3 came back. The prod code could have half of it’s fields removed for example. Maybe it’s a cut/paste error, and it’s not seen in code review. If so, the test would never catch this because it doesn’t assert the full behavior of the API endpoint. This leads to another quote:

> “Test the things that you care about.”

We can’t test everything. There is a limit. But, we should do our best to test the things that we care about. And, if this API endpoint is something that we care about, we should fully test it’s behavior.

# Conclusion

I wrote out 1 ½ pages of bullet points on testing over the last few weeks as I thought about different aspects of testing and things that I’d like to discuss. The above is ⅕ of those bullet points. This is a really good start though I think. Thank you for reading. I hope that you enjoyed and this blog added value for you.

# Next

Next blog I will discuss more mechanics for testing, and I will show code examples for different testing concepts and build upon what I discussed in this blog.

Any feedback is more than welcome. Drop me an email or comment below.

Thank you.
