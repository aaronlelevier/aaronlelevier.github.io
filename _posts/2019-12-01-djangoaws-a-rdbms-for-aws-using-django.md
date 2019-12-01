---
layout: post
title: A RDBMS for AWS using Django and Erlang
tags: [Python Django AWS Erlang]
---

I have a dream for a tech stack where Python and Erlang live together. I feel like I took the first step towards that today. Here is an overview of a code spike for creating a Postgres DB with data from AWS and reading from the same Postgres DB using Erlang.

# The Stack

The stack consists of technologies that I currently use or have used in the past. It's familiar. So far, the stack consists of:

- Python3
- Django
- PostgerSQL
- Erlang

# Let's see it

This is best demostrated by examples, so I'm going to refer to the Github Repo's and READMEs. 

### Django/Python

Here is the Django/Python README: [https://github.com/aaronlelevier/djangoaws](https://github.com/aaronlelevier/djangoaws). 

This code can be used to create a PostgreSQL database, migrate the schema, and populate it with data from AWS EC2.

### Erlang

Then here is example code for connecting to the same database setup and populated by Django, but reading from it using Erlang: [https://github.com/aaronlelevier/motivatedcoder](https://github.com/aaronlelevier/motivatedcoder)

# Conclusion

This is a code spike. The code could be extend for more AWS resources, or connected to other parts of tech stack.