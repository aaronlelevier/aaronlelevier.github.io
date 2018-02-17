---
layout: post
title: Reusable Test Database Pattern in Django!
image: /img/django-dj-icon.png
tags: [Django, Python, Testing]
---

### Summary

This is a short blog post about the resusabled database pattern that I use for working on Django projects.

### Use Case

You have a large Django project where running migrations takes in excess of 30 seconds, etc... Some undesireably long about of time. This is expensive time wise, if you are working on one test, and this is the overhead to re-run the single test each time.

### Inspiration

When chatting with my coworker, [@approaching236](https://github.com/approaching236), he recommended looking into how to do this in Django. He said that there's a 3rd party package in Ruby on Rails that does this and Django should be able to do the same thing. It's been a huge win as far as speeding up how fast we iterate when testing, needless to say!

### Solution

Use The Django `DATABASES` configuration for a [TEST MIRROR](https://docs.djangoproject.com/en/2.0/topics/testing/advanced/#testing-primary-replica-configurations) database.

This configuration lets you run tests against a database without having to create a test database, run all migrations, and drop the test database each time. Instead, it runs the tests on an existing database, and rolls back each transaction after each unit test method, or test class, so as not to mutate database state for unit testing, as you would expect.

To use this configuration, update the Django project like so:

```python
# myproject/settings/test.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_db',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
        'TEST': {
            'MIRROR': 'default',
        }
    }
}
```

To use this config, you will want to build an an empty database with the schema migrated one time. After that, migrations no longer have to be run, and unit tests can be re-run without the database migrations overhead.

### Helper Bash Functions

Here are some helper bash functions that I've found useful with the reusable database pattern. Once in a while there is leaked database state, so I usually make an initial backup after creating the initial empty database, in case that occurs, then a restore of the backup is quick.

```bash
# drop, create, migrate schema of a given database
migratedb () {
    export DJANGO_SETTINGS_MODULE=myproject.settings.test
    dropdb test_db
    createdb test_db
    ./manage.py migrate
}

# create a backup of a given database
backupdb () {
    if [ $# -eq 0 ]
    then
        echo "db_name not specified"
    else
        db_name=$1
        db_name_copy=${db_name}_copy
        psql -c "DROP DATABASE $db_name_copy;"
        psql -c "CREATE DATABASE $db_name_copy WITH TEMPLATE $db_name;"
    fi
}

# restore database from a given backup
restoredb () {
    if [ $# -eq 0 ]
    then
        echo "db_name not specified"
    else
        db_name=$1
        db_name_copy=${db_name}_copy
        psql -c "DROP DATABASE $db_name;"
        psql -c "CREATE DATABASE $db_name WITH TEMPLATE $db_name_copy;"
    fi
}
```

