---
layout: post
title: Python Unit Testing with MagicMock
tags: [Python, Mocking, Unit testing]
---

This blog post demostrates how to mock in Python given different scenarios using the [mock](https://docs.python.org/3/library/unittest.mock.html) and [pretend](https://github.com/alex/pretend) libraries.

This blog post is example driven.

## What is mocking

[Mocking](https://en.wikipedia.org/wiki/Mock_object) is the use of simulated objects, functions, return values, or mock errors for software testing. It is useful for creating specific application states to run automated tests against.

Mocking can be useful for simulating an API response, where the API response can be made a static return value, so the tests are deterministic vs. an ever changing live API call that takes longer to request, the API could be subject to [rate limiting](https://helpx.adobe.com/coldfusion/api-manager/throttling-and-rate-limiting.html), or maybe it's a live system that can't be live tested at will, such as a payment system.
  
Let's get started.

## Initial Setup

Assume these libraries are imported

```python
# python2
from mock import MagicMock, patch
# python3
from unittest.mock import MagicMock, patch

from pretend import stub

# common example of a library to mock against
import requests
```


## Some basics of the `mock` library

`@patch` can be used as a decorator for `unittest` methods. It can target a production test method and make it's return value a `MagicMock` instance.

`@patch` is the same thing as using the `MagicMock` class. It sets the mocked method as a `MagicMock` instance for the duration of the unit test method, then set's back the method to reference it's original definition when the unit test method completes.

A `MagicMock` instance can:

- capture the arguments that the method is called with
- count how many times it's called
- return values that we specify
- return the same or different values each time the mocked method is called
- be made to raise errors

## Mock at the call site

This is the first example, so a lot is going on here.

The prod method must be targeted based on the call site of where the method being mocked is called, not where the method is defined.

The below example shows that even though the method lives in `bar.py`, when we use `@patch` to mock the method, it's targeted using the Python path to `foo.Biz.baz`. This is the Python path to the call site.

When using `@patch`, the decorated unit test method will now require an additional argument. This is `mock_biz` in the example. `mock_biz` is a `MagicMock` instance.

```python
# bar.py
class Bar(object):

    def biz(self):
        pass

# foo.py
from bar import Bar

def foo():
    Bar().biz()

# test.py
import unittest
from mock import patch, MagicMock
from foo import foo

class MyTest(unittest.TestCase):

    @patch("foo.Bar.biz") # not -> @patch("bar.Bar.biz")
    def test_foo(self, mock_biz):
        self.assertFalse(mock_biz.called)

        foo()

        self.assertTrue(mock_biz.called)
        self.assertEqual(mock_biz.call_count, 1)
        self.assertIsInstance(mock_biz, MagicMock)
```

# Mock two things

When mocking two methods, the `MagicMock` arguments to the method should be passed in in the order that the decorators wrap the unit test method. So, in the below example, the `@patch` for `bar.requests.put` first wraps the unit test method, so it takes the place of the first argument, then the next is `bar.requests.get`, so it's the 2nd argument.

```python
# bar.py
import requests

class Bar(object):

    def sync(self, id, query_first):
        if query_first:
            requests.get('/remote/api/{id}'.format(id=id))

        requests.put('/remote/other/api/{id}'.format(id=id),
                                                     data=current_data())

# test.py
import unittest
from mock import patch
from bar import Bar

class MyTest(unittest.TestCase):

    @patch("bar.requests.get")
    @patch("bar.requests.put")
    def test_foo(self, mock_put, mock_get):
        Bar.sync(id=42, query_first=False)

        self.assertFalse(mock_get.called)
        self.assertTrue(mock_put.called)
```

# Mock as an Argument Captor

Here is an example of the `MagicMock` instance capturing different arguments. It can capture positional and keyword arguments. In the below example, `url` and `method` are positional arguments to `Bar.biz`, and are stored in `mock_biz.call_args[0]`

`data` and `headers` are keyword arguments, and are stored in `mock_biz.call_args[1]`


```python
# bar.py
class Bar(object):
    def biz(self, url, method, data, headers):
        pass

# foo.py
from bar import Bar

def foo(url, method='GET', data=None, headers=None):
    Bar().biz(url, method, data=data, headers=headers)

# test.py
class MyTest(unittest.TestCase):

    @patch("foo.Bar.biz")
    def test_foo(self, mock_biz):
        url = '/api/users/{id}'.format(id=1)
        data = {'phone_number': '+17025551000'}
        method = 'PUT'
        headers = {"Authorization": "JWT <your_token>"}

        foo(url, method, data=data, headers=headers)

        self.assertFalse(mock_biz.called)
        self.assertEqual(mock_biz.call_count, 1)
        self.assertEqual(mock_biz.call_args[0][0], url)
        self.assertEqual(mock_biz.call_args[0][1], method)
        self.assertEqual(mock_biz.call_args[1]['data'], data)
        self.assertEqual(mock_biz.call_args[1]['headers'], headers)
```

# Mock a return value

The `MagicMock` instance `return_value` attribute's value can be set to mock a return value. 

This is a common use case for how to mock an API response.

```python
# bar.py
class Bar(object):

    def biz(self):
        return 1

# foo.py
from bar import Bar

def foo():
    return Bar().biz()

# test.py
class MyTest(unittest.TestCase):

    @patch("foo.Bar.biz")
    def test_foo(self, mock_biz):
        expected_value = 2
        mock_biz.return_value = expected_value
        
        ret = foo()
        
        self.assertEqual(ret, expected_value)
```

# Mock multiple return values

If the mocked method is called multiple times, and `MagicMock.return_value` has been set, the same value will be returned each time the mocked method is called.

In order to return different values each time, the value of `MagicMock.side_effect` can be set as in the below example.

`MagicMock.call_args_list` can be used to check what the different arguments each time the mocked method is called.

```python
# bar.py
class Bar(object):
    def biz(self, i):
        return expensive_computation(i)
    
    def expensive_computation(self, i):
        pass

# foo.py
def foo():
    bar = Bar()
    for i in range(2):
        value = bar.biz(i)
        process_expensive_value(value)
    
# test.py
class MyTest(unittest.TestCase):
    @patch("bar.Bar.expensive_computation")
    @patch("foo.process_expensive_value")
    def test_foo(self, mock_process_exp_val, mock_exp_comp):
        value1 = 1
        value2 = 2
        mock_exp_comp.side_effect = [value1, value2]
        
        foo()
        
        self.assertTrue(mock_exp_comp.called)
        self.assertEqual(mock_exp_comp.call_count, 2)
        self.assertEqual(mock_process_exp_val.call_args_list[0][0][0], value1)
        self.assertEqual(mock_process_exp_val.call_args_list[1][0][0], value2)
```

# Mock an Exception

`MagicMock.side_effect` is more commonly used to mock throwing an `Exception`.

This is very useful because maybe the application hit a particular error state that is seen in the logs that needs to be guarded against. Instead of having to get the application back in that exact state to cause the error, the method that threw the error can be mocked to do throw the error, and then code can be written and tested to react accordingly.

Here is an example:

```python
# bar.py
class Bar(object):
    def biz(self):
        if some_condition():
            raise CustomException()

class CustomException(Exception):
    pass
            
# foo.py
from bar import Bar

def foo():
    Bar().biz()

# test.py
class MyTest(unittest.TestCase):

    @patch("foo.Bar.biz")
    def test_foo(self, mock_biz):
        mock_biz.side_effect = CustomException()
        
        with self.assertRaises(CustomException):
            foo()
```

## Using mock objects

Here is an example of creating a mock object using the [stub](https://github.com/alex/pretend) library in order to create the exact response structure that you want to simulate and react to.

```python
# bar.py
import requests

class Bar(object):
    def biz(self):
        return requests.get('/api/users/')

# foo.py
from bar import Bar

def foo():
    response = Bar().biz()
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf8'))
        process_users_data(data)

def process_users_data(data):
    pass

# test.py
from pretend import stub

class MyTest(unittest.TestCase):
    @patch("bar.requests.get")
    @patch("foo.process_users_data")
    def test_foo(self, mock_process_users_data, mock_get):
        fake_reponse = stub(
            status_code=200,
            content=json.dumps({'users': 'data'}).encode('utf8'))
        mock_get.return_value = fake_reponse

        foo()

        self.assertTrue(mock_process_users_data.called)
        self.assertEqual(
            mock_process_users_data.call_args[0][0],
            json.loads(fake_reponse.content.decode('utf8')))
```

## Other info about mocking

Parent methods can be mocked, so if your code calls `super()`, the `@patch` should target the parent class's method.

Constructors can be mocked. A `return_value = None` must be set because a Python constructor can't have  a return value.

## Conclusion

Mocking has been super useful for me in my professional software developer career. Code gets more and more complicated as applications scale, so being able to isolate inputs and outputs to a function within a system is priceless for unit testing.

Integration testing, the degree of mocking, and overall test strategy has to be thought of a lot. It can't just be "mock all the things" and then you have 100% test coverage, and an application that is bullet proof. Maybe the mocks are wrong, there's too many, etc.. Maybe things that don't need to be tested are tested. Over testing is a thing.

If you have any feedback, drop me a [line](mailto:aaron.lelevier@gmail.com) or comment below.

Thanks