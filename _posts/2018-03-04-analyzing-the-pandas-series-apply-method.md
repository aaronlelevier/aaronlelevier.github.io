---
layout: post
title: Analyzing the Pandas Series Apply Method
tags: [Pandas, Python]
---

I saw the [Pandas.apply](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html) method and started thinking about this pattern and if it'd be useful to implement on other objects. Here's a brief blog about the pattern.

The general pattern outside of framework or language specifics is:
> Apply an anonymous function to a value or an iterable

### Pandas Example

In the case of `Pandas.apply` it let's you apply a function to each item in a iterable, which, in the case of Pandas, is each item of a single [Series](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html) in a [DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html). `Series` implements the `apply` method.

```python
import pandas as pd

df = pd.DataFrame({'number': [1, 2, 3, 4]})

series = df['number']

print(type(series), '\n')

is_even = series.apply(lambda n: n % 2 == 0)

print(is_even)

### OUTPUT ###
# <class 'pandas.core.series.Series'>

# 0    False
# 1     True
# 2    False
# 3     True
# Name: number, dtype: bool
```

### Python object instance example

Can this pattern then be used with Python base class instances inheriting from `object`? Yes, here's what that would look like.

```python
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def apply(self, func):
        return func(self)
    
person = Person('Bob', 60)

person.apply(lambda p: "{p.name} is {p.age}".format(p=p))

### OUTPUT ###
# 'Bob is 60'
```

Defining the `apply` method allows the [lambda](https://docs.python.org/3/reference/expressions.html#lambda) to be immediately returned, instead of having to assign it to a reference, then invoke it.

```python
f = lambda p: "{p.name} is {p.age}".format(p=p)
f(person)

### OUTPUT ###
# 'Bob is 60'
```

### Python iterable example

Okay, so let's use the `apply` pattern with a Python iterable and see what it looks like.

This code snippet subclasses the Python `list` standard *type*, which may or may not be kosher. The point is that the `type` being subclassed just has to implement the iterable interface. This could be anything, a Django [QuerySet](https://docs.djangoproject.com/en/2.0/ref/models/querysets/) for example.

```python
class PersonList(list):
    def apply(self, func):
        return [func(x) for x in self.__iter__()]

person_list = PersonList()

person = Person('Bob', 60)
person2 = Person('Jerry', 55)

person_list.append(person)
person_list.append(person2)

person_list.apply(lambda p: "{p.name} is {p.age}".format(p=p))

### OUTPUT ###
# ['Bob is 60', 'Jerry is 55']
```

Let's do the same using Python's [map](https://docs.python.org/3/library/functions.html#map) builtin function.

```python
[x for x in map(lambda p: "{p.name} is {p.age}".format(p=p),
                [person, person2])]

### OUTPUT ###
# ['Bob is 60', 'Jerry is 55']
```

Python `dict` example for `iter` and `items`

### Python iterable example #2 - dict

```python
class EmployeeDict(dict):
    def apply(self, func):
        return [func(x) for x in self.__iter__()]
    
    def apply_items(self, func):
        return [func(k,v) for k,v in self.items()]

employee_dict = EmployeeDict({'manager': person, 'clerk': person2})

employee_dict.apply(lambda x: x)

### OUTPUT ###
# ['manager', 'clerk']
```

Use `apply` pattern with `dict` items

```python
employee_dict.apply_items(lambda k,v: "The {}'s name is {}".format(k, v.name))

### OUTPUT ###
# ["The manager's name is Bob", "The clerk's name is Jerry"]
```

### Summary and Note on `Pandas.apply`

The `Pandas.apply` method does a lot more than apply a lambda function. Here is the full method signature and link to the [source](https://github.com/pandas-dev/pandas/blob/master/pandas/core/series.py#L2407).

It makes sense to do a lot more, because if your class has to defined an extra method `apply` when you could just be calling the builtin Python `map` function, then it should be worth it.