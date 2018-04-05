---
layout: post
title: Multithreading in Python
meta: Processes, Threads, and the GIL in Python
tags: [Python, Threads, Processes, Multithreading, GIL]
---

This blog post is about Processes, Threads, and the GIL in Python.  Because of the way that the Python GIL operates, it may be different than one initially expects, so this blog post is an attempt to discuss this in more detail.

### Some background

A [Process](https://en.wikipedia.org/wiki/Process_(computing)) is a instance of a computer program in execution. It has it's own address space, data stack, memory, and auxiliary data to keep track of it's execution.

[Threads](https://en.wikipedia.org/wiki/Thread_(computing)) exist within a process. They can run in parallel to the main thread of a process and share the same data space.

The [GIL](https://wiki.python.org/moin/GlobalInterpreterLock), Global Interpreter Lock, in Python says that when in effect only one thread can run at a time per Python process.

### How the GIL behaves

If the GIL is in effect, it is a [Lock](https://en.wikipedia.org/wiki/Lock_(computer_science)), and only one thread can run at a time.

With CPU tasks, the GIL will be in effect. If multiple CPU tasks are being run on the same Python process, the GIL will block the additional tasks if they are non yielding until one completes and the GIL is released.

Yielding means non-blocking, so the use of `Threads` or the `yield` statement in Python for example are non-blocking if the task itself doesn't block. 

The GIL is released when doing I/O. I/O invokes built-in operating system C code, so the GIL is released and then reacquired when the I/O completes. This means that threads can be used in Python to improve I/O program performance.

The GIL is also often released in extension code. [Here](https://docs.python.org/3/c-api/init.html#releasing-the-gil-from-extension-code) is more detail.

### Separate Python processes

Each Python process has it's own GIL managing access to it's main thread of execution. Python processes can run in parallel and there are primitives for sharing data between processes.

### Some Python modules for multiple threads or processes

The [threading](https://docs.python.org/3/library/threading.html) module is a higher-level interface built on top of the Python's [thread](https://docs.python.org/3/library/_thread.html) module. This is shown in the example below.

The [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) module has the `ThreadPoolExecutor` and `ProcessPoolExecutor` class. With these classes, jobs are submitted to a worker pool of a given size and then executed.

The [subprocess](https://docs.python.org/3/library/subprocess.html) module allows for the spawning of new processes. This is commonly used in testing for running independent test code in parallel.

### Sharing data between Threads or Processes

The Python [queue](https://docs.python.org/3/library/queue.html) module adds this functionality. An example of using a `Queue` to share data between threads is shown below.

### Example of improved Python performance with multithreaded I/O

Here is an example of a single vs. multithreaded I/O program using the Github API to demonstrate the difference in performance.

<script src="https://gist.github.com/aaronlelevier/cbf7d38a571ae72a0339aa0f12f88df2.js"></script>

Example output

```
$ python github_followers.py --username aaronlelevier
single_threaded time(sec): 4.647056104964577
multi_threaded time(sec): 1.0500583100365475
both single_threaded and multi_threaded count: 127
```

### Summary

If you are doing Python I/O, whether it be HTTP data syncing or other I/O tasks, multithreading can be used to improve program performance.

Extension code may also be used for running Python code in parallel on a single process.

### More info

[Core Python Applications Programming - Multithreading](http://www.informit.com/articles/article.aspx?p=1850445) by Wesley Chun

[Python Concurrency From the Ground Up: LIVE!](http://pyvideo.org/pycon-us-2015/python-concurrency-from-the-ground-up-live.html) by David Beazley

