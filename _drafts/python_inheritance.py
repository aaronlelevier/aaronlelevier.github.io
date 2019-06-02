#!/usr/bin/env python
# coding: utf-8

# This blog is a tour through Inheritance in Python.
# 
# This blog assumes no prior knowledge, and teaches the Reader from the ground up what Inheritance and how to use it in Python.
# 
# For the Reader who already knows inheritance and is reading this blog in order to audit it (you know who you are!). Please comment if there's anything you question. Any feedback is welcome.
# 
# Let's Go.

# What is inheritance?
# 
# That's a big question, right?! If we could say in a sentence or paragraph, what it is, then, well, it obviously wouldn't be complete. Instead, let's describe Inheritance as we go.
# 
# The first point, Inheritance means exaclty that, you inherit. Let's look at code that does this.
# 
# In this inheritance example, we'll see what this means to have one's own method and inherit some method

# In Python, the `__init__` is the constructor. This method is called when an object is created.
# 
# It contains the arguments passed to the class.

# In[25]:


# __init__ constructor example
# class with no inheritance

class MyClass:
    def __init__(self, a):
        print(f"we're in: {self.__class__.__name__}")
        self.a = a
        
my_class = MyClass('foo')
        
vars(my_class), my_class.a


# Let's inherit from a parent

# In[33]:


class ParentMyClass:
    def __init__(self, a):
        cls_name = self.__class__.__name__
        print(f"parents: {cls_name}", a)
    
class Child(ParentMyClass):
    def __init__(self, a):
        super().__init__(a)
        print(f"child: {self.__class__.__name__}", a)
        self.a = a
        
Child('bob')


# Call the Parent class when they have a different implementation

# In[42]:


class ParentMyClass:
    def __init__(self, a):
        cls_name = self.__class__.__name__
        self.a = a
        print("foo", a)
    
class Child(ParentMyClass):
    def __init__(self, b):
        super().__init__(b)
        print(f"bar", b)
        self.b = b
        
child = Child('bob')


# Why should I call a parent class?
# 
# Maybe the parent class sets some functionality that I want to happen for free. 

# In[ ]:





# In[40]:


child.a


# In[41]:


child.b


# In[ ]:


class A:
    def __init__(self):
        print("I'm A")
        
class B:
    def __init__(self):
        print("I'm B")


# In[ ]:





# In[ ]:




class A:
    def __init__(self):
        print("I'm A")
        
class B:
    def __init__(self):
        print("I'm B")
        
class C:
    def __init__(self):
        print("I'm C")
        
        
class D(A):
    def __init__(self):
        super().__init__()
        print("I'm D")
        
class E(A, B):
    def __init__(self):
        print("I'm E")
    

d = D()


# In[9]:


E()


# In[ ]:




