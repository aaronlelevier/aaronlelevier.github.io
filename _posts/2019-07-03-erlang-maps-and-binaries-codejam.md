---
layout: post
title: Erlang Maps and Binaries Codejam
tags: [Erlang, Codejam]
---

If you can read this Erlang code jam, the syntax is kind of insane. Just think about it. This is how to manipulate primitive types in Erlang. But not just that. After that is a Python codejam. Python is my main language. It will be fun to compare. 

Here are list, tuple, and zip two lists in both languages. But, first, a short background.

# My Story

I'm new to Erlang. I'm on page 110 of [Joe Armstrong](Joe Armstrong (programmer) - Wikipedia
https://en.wikipedia.org/wiki/Joe_Armstrong_(programmer))'s book, [Programming in Erlang, 2nd](https://gangrel.files.wordpress.com/2015/08/programming-erlang-2nd-edition.pdf). 

Erlang is an interesting language. The first time that I tried to learn Erlang, about 1 year ago, a good friend said, "wait until you see pattern matching." I was reading this exact same book, and was to about page 70, and I still hadn't seen pattern matching. 

My interests changed, and I gave up reading the book. I had gotten so stuck on [Tensorflow Extended (TFX)](https://www.tensorflow.org/tfx/serving/serving_basic) and had paused any project coding because I was so frustrated. 2 months ago, I started reading the book after hearing in May 2019 of Joe Armstrong's untimely death.

TFX had promised me an end-to-end pipeline. There are about 9 steps. When I got two thirds of the way through to the `transform` step, I got so frustrated with the objects involed and their api. Whatever I was trying to do wasn't working. I gave up.

In May, I stated reading "Erlang Programming 2nd Ed." by Joe Armstrong. So, if I do the math, in 60 days I have read 110 pages, so 2 pages a day. Ouch. Okay, that's kind of bad. Either way, here is my progress. Maybe I only got serious in the last month, and I'm being hard on myself. Enjoy.

# Python and Erlang

Let's do Erlang first. I'll build myself up for Python. Python is my main language, so I'll show that last.

## Erlang

Map, List, Tuple, Zip Code Example

```
^Caaron@ ~/Documents/erlang/src (master) $ erl
Erlang/OTP 20 [erts-9.2.1] [source] [64-bit] [smp:4:4] [ds:4:4:10] [async-threads:10] [hipe] [kernel-poll:false] [dtrace]

Eshell V9.2.1  (abort with ^G)
1> bob.
bob
2> % ok let's go.
2> ab.
ab
3> bob.
bob
4> Map  = #{first_name := "aaron"}.
* 1: only association operators '=>' are allowed in map construction
5> Map  = #{first_name => "aaron"}.
#{first_name => "aaron"}
6> FullNameMap = Map#{last_name => "lelevier"}.
#{first_name => "aaron",last_name => "lelevier"}
7> Attrs = maps:keys(FullNameMap).
[first_name,last_name]
8> Values = maps:values(FullNameMap).
["aaron","lelevier"]
9> tuple_to_list({Attrs, Values}).
[[first_name,last_name],["aaron","lelevier"]]
10> lists:flat(Attrs, Values).
** exception error: undefined function lists:flat/2
11> lists:flat(Attrs).
** exception error: undefined function lists:flat/1
12> lists:flatten(Attrs).
[first_name,last_name]
13> lists:flatten(Attrs, Values).
[first_name,last_name,"aaron","lelevier"]
14> P = fun(X) -> X * 2 end.
#Fun<erl_eval.6.99386804>
15> lists:fold
foldl/3  foldr/3
15> lists:foldl(P, void, [1,2,3]).
** exception error: interpreted function with arity 1 called with two arguments
     in function  lists:foldl/3 (lists.erl, line 1263)
16> P1 = fun(X, y) -> {X,Y} end.
* 1: variable 'Y' is unbound
17> P1 = fun(X, Y) -> {X,Y} end.
#Fun<erl_eval.12.99386804>
18> lists:foldl(P1, void, [1,2,3]).
{3,{2,{1,void}}}
19> lists:foldl(P1, 9, [1,2,3]).
{3,{2,{1,9}}}
20> P2 = fun(X, Y) -> {X*7,Y*2} end.
#Fun<erl_eval.12.99386804>
21> lists:foldl(P2, 1, [1,2,3]).
** exception error: an error occurred when evaluating an arithmetic expression
     in operator  */2
        called as {7,2} * 2
     in call from erl_eval:do_apply/6 (erl_eval.erl, line 674)
     in call from erl_eval:expr_list/6 (erl_eval.erl, line 878)
     in call from erl_eval:expr/5 (erl_eval.erl, line 236)
     in call from lists:foldl/3 (lists.erl, line 1263)
22> P2 = fun(X, Y) -> X*Y end.
** exception error: no match of right hand side value #Fun<erl_eval.12.99386804>
23> P3 = fun(X, Y) -> X*Y end.
#Fun<erl_eval.12.99386804>
24> lists:foldl(P3, 1, [1,2,3]).
6
25> list_to_tuple([1,2]).
{1,2}
26> list_to_tuple([1,2, "three", four]).
{1,2,"three",four}
27> Tup = list_to_tuple([1,2, "three", four]).
{1,2,"three",four}
28> Bin = term_to_binary(Tup).
<<131,104,4,97,1,97,2,107,0,5,116,104,114,101,101,100,0,4,
  102,111,117,114>>
29> StatusCode = 200.
200
30> Packet = <<StatusCode:4, Bin/binary>>.
<<136,54,128,70,16,22,16,38,176,0,87,70,135,38,86,86,64,0,
  70,102,247,87,2:4>>
31> <<RecHeader:4, RecBin/binary>> = Packet.
<<136,54,128,70,16,22,16,38,176,0,87,70,135,38,86,86,64,0,
  70,102,247,87,2:4>>
32>
32> RecHeader.
8
33> c(utils).
{ok,utils}
34> utils:type(RecHeader).
integer
35> Packet2 = <<StatusCode:32, Bin/binary>>.
<<0,0,0,200,131,104,4,97,1,97,2,107,0,5,116,104,114,101,
  101,100,0,4,102,111,117,114>>
36> <<RecHeader2:32, RecBin2/binary>> = Packet2.
<<0,0,0,200,131,104,4,97,1,97,2,107,0,5,116,104,114,101,
  101,100,0,4,102,111,117,114>>
37>
37> RecHeader2.
200
38> RecBin2.
<<131,104,4,97,1,97,2,107,0,5,116,104,114,101,101,100,0,4,
  102,111,117,114>>
39> binary_to_term(RecBin2).
{1,2,"three",four}
40> Values.
["aaron","lelevier"]
41> lists:zip(Attrs, Values).
[{first_name,"aaron"},{last_name,"lelevier"}]
```

And from there, I could get back to where I eventually was.

## Python 

Map, List, Tuple, Zip Code Example. Here is the Python codejam. Enjoy.

```python
(venv) aaron@ ~/Documents/github/tfx (statistics_gen) $ python
Python 2.7.16 (v2.7.16:413a49145e, Mar  2 2019, 14:32:10) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> # let's do this the same way. It has to be command line. If it were in Jupyter notebook, then that just wouldn't be fair. Right?!
... 
>>> d = {'foo': 1, 'bar': 2}
>>> # what are they keys
... 
>>> d.keys()
['foo', 'bar']
>>> # what are the values
... 
>>> d.values()
[1, 2]
>>> # single line split
... 
>>> keys, values = zip(d)
>>> keys
('foo',)
>>> values
('bar',)
>>> keys, values = zip(d.items())
>>> keys
(('foo', 1),)
>>> values
(('bar', 2),)
>>> zip(d.items())
[(('foo', 1),), (('bar', 2),)]
>>> zip(*d.items())
[('foo', 'bar'), (1, 2)]
>>> a, b = zip(*d.items())
>>> a
('foo', 'bar')
>>> b
(1, 2)
>>> d
{'foo': 1, 'bar': 2}
>>> d.items()
[('foo', 1), ('bar', 2)]
>>> c,d = d.items()
>>> c
('foo', 1)
>>> d
('bar', 2)
>>> d.keys()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'keys'
>>> d
('bar', 2)
>>> d = {'foo': 1, 'bar': 2}
>>> d
{'foo': 1, 'bar': 2}
>>> d.values()
[1, 2]
>>> zip(d.keys(), d.values())
[('foo', 1), ('bar', 2)]
>>> a, b = zip(d.keys(), d.values())
>>> a
('foo', 1)
>>> b
('bar', 2)
>>> {chr(x}:x for x in range(100, 100)}
  File "<stdin>", line 1
    {chr(x}:x for x in range(100, 100)}
          ^
SyntaxError: invalid syntax
>>> {chr(x):x for x in range(100, 100)}
{}
>>> {chr(x):x for x in range(100, 110)}
{'e': 101, 'd': 100, 'g': 103, 'f': 102, 'i': 105, 'h': 104, 'k': 107, 'j': 106, 'm': 109, 'l': 108}
>>> chars = {chr(x):x for x in range(100, 110)}
>>> next(iter(chars))
'e'
>>> chars.keys()
['e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm', 'l']
>>> chars.values()
[101, 100, 103, 102, 105, 104, 107, 106, 109, 108]
>>> chags.items()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'chags' is not defined
>>> chars.items()
[('e', 101), ('d', 100), ('g', 103), ('f', 102), ('i', 105), ('h', 104), ('k', 107), ('j', 106), ('m', 109), ('l', 108)]
>>> sup(chars.values())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sup' is not defined
>>> sum(chars.values())
1045
>>> values = chars.values()
>>> min(values)
100
>>> values[:2]
[101, 100]
>>> values
[101, 100, 103, 102, 105, 104, 107, 106, 109, 108]
>>> sorted(values) == values
False
>>> values[-3:]
[106, 109, 108]
>>> values[:-3]
[101, 100, 103, 102, 105, 104, 107]
>>> # that was the last three, or up to the last three
... 
>>> # that was the last three, or up to the last three
```

Wow, that was a world tour of Python. The slicing here involved lists, where the Erlang slicing used Binaries. Both were slicing of data structures.

# Verdict

Okay, hands on the keyboard verdict. Both were amazing! Okay, until next time. Thanks for reading.