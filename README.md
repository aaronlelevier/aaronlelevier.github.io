# About

This is the code for [my blog](http://motivatedcoder.com). It's a customization of the [Kasper](https://github.com/rosario/kasper) theme for [Jekyll](http://jekyllrb.com/). Feel free to fork, change and use it.

## How to use it

Clone this repository, and then run `rake` to run the server.
There is a rake task to create new posts:

```bash
rake post title="my new post"
```

## local setup

Jekyll docs [here](https://jekyllrb.com/)

Also need to use `rvm`

```
# get rvm
curl -L https://get.rvm.io | bash -s stable

# install Ruby version of project
rvm install ruby-2.4.2
```

```
# set Ruby version of project
rvm use 2.4.2

# install dependencies
bundle install

# serve locally
rake default
```
