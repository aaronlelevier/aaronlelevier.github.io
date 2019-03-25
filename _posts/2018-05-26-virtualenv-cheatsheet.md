---
layout: post
title: virtualenv Cheatsheet
tags: [Python, virtualenv, cron]
---

A `virtualenv` is one of the first things a Python programmer learns about. This blog post describes what it is, how to set it up, and examples of some concrete use cases.

## What is a `virtualenv`?

A `virtualenv` is a way of having separate Python environments. It allows you to have different environments for Python 2 and Python 3 and the 3rd party package dependencies to go along with that environment.

## Quickstart

Run the following commands to create and activate your first `virtualenv`

### virtualenv for Python3

```
# installs PIP globally
curl https://bootstrap.pypa.io/get-pip.py | python

# creates a virtualenv
python3 -m venv venv

# activates the virtualenv
source venv/bin/activate
```

### virtualenv for Python2

```
# installs PIP globally
curl https://bootstrap.pypa.io/get-pip.py | python

# installs virtualenv globally
pip install virtualenv

# creates a virtualenv
virtualenv venv

# activates the virtualenv
source venv/bin/activate
```

### Verify it's working

You should see the command line now starting with `(venv)`. This means that the virtualenv is active. 

Run `which python` and it should point to a Python executable inside the virtualenv at `venv/bin/python`

## Quickstart Explanation

First get [pip](https://pypi.org/project/pip/). `pip`, which stands for "Pip Installs Packages", is the Python ecosystem's package installer. If it is not already installed. This can be done using the linked instructions, or with this command.

```
curl https://bootstrap.pypa.io/get-pip.py | python
```

If you already have `pip` or just want to check, run this command to check and output all installed 3rd party packages:

```
pip freeze
```

If you currently have other 3rd party packages, and want to clean up the gloal dependencies, then run this command to remove all 3rd party packages:

```
pip freeze | xargs pip uninstall -y
```

This is my prefered configuration. To only have `virtualenv` as the single global 3rd party package. Other packages are local to the `virtualenv`.

Now, install `virtualenv` globally.

```
pip install virtualenv
```

Check what version of Python is the default version.

```
python -V
```

On my machine, the previous command returned `Python 2.7.14`. So, when I create a `virtualenv` this will be the default Python version, unless another version is specified.

Create a new `virtualenv`

```
virtualenv venv
```

**Why is it named `venv`?**

By convention, the name `venv` is used as the name of the `virtualenv`, but any name can be used.

Now, activate the `virtualenv`

```
source venv/bin/activate
```

`venv`, the name of the `virtualenv` should show at the start of the command line prompt.

```
# before
~/Documents/github/jira (master) $

# after
(venv) ~/Documents/github/jira (master) $
```

If you run `pip freeze` at this point, there should be no output because this is a new Python environment. The global `virtualenv` that was just installed should not appear in the output.

At this point, any 3rd party Python package can be installed, just like `virtualenv` was installed globally, and as long as the `virtualenv` is active, it will be private to that `virtualenv`.

To deactivate the `virtualenv`, run:

```
deactivate
```

## CheatSheet

Here are some use cases and common commands.

### Create a `virtualenv` in Python3

The [venv](https://docs.python.org/3/library/venv.html) standard library package is available as of Python 3.3 and can be used to create a `virtualenv`

```
python3 -m venv venv
```

### `virtualenv` with a specific version of Python

This will create a `virtualenv` in Python 3.5

```
virtualenv -p /usr/local/bin/python3.5 venv
```

### Access the `virtualenv` without it being active

By using the path to the Python executable inside of the `venv`, the `virtualenv` and all of it's 3rd party packages will be loaded:

```
~/Documents/github/jira (master) $ python
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
~/Documents/github/jira (master) $ venv/bin/python
Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```

### `virtualenv` with [cron](https://en.wikipedia.org/wiki/Cron)

```
crontab -e
* * * * * /path/to/venv/bin/python /path/to/code.py
```

### Include global Python packages when creating a `virtualenv`

```
virtualenv --system-site-packages venv
```

### Delete a `virtualenv`

```
rm -rf venv
```

### Store copy of Python package versions

This is done by convention in a file called `requirements.txt`

```
pip freeze > requirements.txt
```

### Install all packages from `requirements.txt`

This command would be used when running another projects code, to install all dependencies of the project.

```
pip install -r requirements.txt
```

## Conclusion

[virtualenv](https://virtualenv.pypa.io/en/stable/) has been very useful. Now days, with Docker, and containers, they're not always necessary, but if you're developing locally and have multiple Python projects, they're a must. You won't get package conflicts, and can maintain different Python version and environments.

### Any questions?

Thank you for reading. If you have any questions or anything that I can add, please let me know. Thanks.
