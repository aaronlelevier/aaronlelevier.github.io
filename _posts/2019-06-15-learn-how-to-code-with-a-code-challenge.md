---
layout: post
title: Learn How to Code with a Code Challenge
tags: [Coding, Code Challenge]
---

The theme this week is to do a code challenge in a new language. For this week I will suggest a code challenge and solve it. I challenge you the reader to attempt the same challenge, or make another one up and solve it in a language that you are trying to get better at.

# Background

For me, I have had success by reading books on computer languages or frameworks, and then implementing them in a personal project. This has helped solidify the concepts, syntax of a language, standard library knowledge, and so on.

# Set the Scene

Code challenges are like code katas, or working out. You have to flex that muscle to stay fit. And push yourself to new limits in order to grow. That's the goal of the code challenge.

# Code Challenge

Here is the challenge to solve. This is an actual problem of mine that I wanted to solve in code. I have a book that I'm reading. I want to know what the date is when I will finish reading this book if I read N number of pages per day. There are a few things that go into this situation that I considered:

- how many pages are in the book
- what page am I on
- how many pages will I read per day
- what is the current date
- do I have any vacation days where I won't be reading
- how may days a week am I resting and not reading

## (Optional)

Optional challenge to test your code

Optional challenge to document your code

# My Code Challenge Attempt

Given the above details, I attempted this using [Erlang](http://erlang.org/doc/index.html). I hadn't done date arithmetic before, so I would be learning something new. The above code challenge is an actual real problem for me that I wanted to solve. I am reading [Programming Erlang 2nd Edition](https://gangrel.files.wordpress.com/2015/08/programming-erlang-2nd-edition.pdf). Here is my data for the above questions:

```
510 = "how many pages are in the book"
63 = "what page am I on"
5 = "how many pages will I read per day"
{2019, 6, 15} = "what is the current date"
17 = "how many vacation days when I won't be reading"
14 = "how may days a week am I resting and not reading"
```

Here is my code in Erlang:

<script src="https://gist.github.com/aaronlelevier/c2d192fa3e83d7e0cddd9f87282216bc.js"></script>

# Conclusion

I enjoyed the code challenge. It gave me a goal to test my current understanding where I wasn't purely copying book code with small tweaks. I now feel like I understand the language more and am ready to continue reading next week.

If you are an Erlang developer, I know that the code is really bad. It's part of the learning process. Don't worry if your code challenge isn't pretty. The goal is to solve the problem, and code can always be made prettier or more concise. 

# Code Challenge Solutions

If you solved the code challenge in another language, please send me a pull request for this blog with a `gist` of the code and I can see about adding it to the blog. Thanks.

Thank you for reading :)
