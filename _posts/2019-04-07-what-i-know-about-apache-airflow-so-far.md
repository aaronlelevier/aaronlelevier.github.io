---
layout: post
title: What I know about Apache Airflow so Far
tags: [Apache Airflow, Python, Learning]
---

This is a blog recording what I know about Apache Airflow so far, and a few lessons learned. This blog is in no means exhuastive on all Airflow can do. Maybe the main point of interest for the reader is the workflow section on how to iterate on adding tasks and testing them.

## Details

I started Apache Airflow with the [Quickstart](https://airflow.apache.org/start.html) and [Tutorial](https://airflow.apache.org/tutorial.html) and everything seemed pretty straight forward, but when I tried to do some of my own [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph) ideas and learn some other concepts in Airflow, I got stuck. My DAGs weren't registering, and I wasn't sure what was wrong. My DAGs were taking too long to run, too long of a feedback loop. Some of it was because they were in the wrong directory, or had Python Errors.

I learned to eventually follow this workflow. Okay, here's it is, but first some vocabulary.

### Airflow Vocabulary

Some Airflow vocabulary and concepts that will be used in this blog.

`DAG` - directed acyclic graph - in Airflow, a description of the work to take place

`Operator` - a class that acts as a template for a Task. This can be a `BashOperator`, `PythonOperator`, etc...

`Task` - an instance of an `Operator`

`Task instance` - a task instance is a Task in a DAG that was run at a certain point in time with a given configuration

Okay, *workflow* time!

### My Airflow Workflow

First, Airflow DAGS need to be registered in the `AIRFLOW_HOME` directory. This is set as an environment variable. By convention, `export AIRFLOW_HOME=~/airflow`. Other things in this `dir` are:

```
airflow.cfg   airflow.db    dags          logs          unittests.cfg
```

But, the DAGs that the developer works on are in a Project directory somewhere. To isolate my Project `dir` and where Airflow resources `live` and get my DAGs discovered, I symlinked them from the Project dir to the Airflow dir.

Next, to test a DAG, starting `airflow scheduler` and running the full DAG isn't ideal. The feedback loop is too long. It could take 5 minutes for a DAG to run, and it will run all steps. Here are the steps that I learned to use to iterate on developing a DAG in Airflow:

#### Iterate on developing a DAG in Airflow

First, call it as a Python script to see if there's any errors:

```
$ python my_dag.py
```

Second, try seeing if the DAG is registered:

```
$ airflow list_dags
```

Third, output the Tasks for a DAG. This lets you know what Tasks are configured for the DAG

```
$ airflow list_tasks my_dag
```

Then, a Task can be tested in isolation. A date param is required.

```
$ airflow test my_dag my_task 2019-04-07
```

Depending on the situation, and if we're ready to run the DAG, then the DAG can be run by starting these two processes:

```
# terminal 1 - DAGs are turned on an run here
airflow webserver

# terminal 2 - crawls the directory structure to discover and register DAGs
airflow scheduler
```

When running a full DAG, I was looking in the `$AIRFLOW_HOME/logs` to check output. Logs are by DAG name, task, and date. It's reachable, but it can be easier found in the Airflow webserver UI.

#### Python Debugging

I couldn't get `pdb` to work when running the full DAG. This is because the Tasks are run as subprocesses, so they won't hit the debugger, but when running `airflow test` though, `pdb` works!

#### PythonOperator.python_callable

Python functions can be tested outside of Airflow, and this is ideal. I unit tested a couple, and in a real application, I would do this extensively and outside of Airflow. This is also what Matt Davis recommends in the video and notes linked below.

#### Here's how to Hide example DAGs

This can be done in `$AIRFLOW_HOME/airflow.cfg` by setting: `load_examples = False`

## Some Airflow Features

`PythonOperator` - are used to call a Python function. They can be passed positional arguments with `op_args`, keyword arguments with `op_kwargs`, and Airflow context, such as the Task instance, and datetime info with `provide_context=True`

`BranchPythonOperator` - are used for doing conditional branching in a DAG

`SubDagOperator` - can be used for setting repeatable steps for `Tasks` at different points in a `DAG`. [Tensorflow Extended](https://github.com/tensorflow/tfx) uses these for common steps in each `Task` to first check the `cache`, and then decide to `execute` if needed.

[XCom](https://airflow.apache.org/concepts.html?highlight=xcom) - is for passing key/value primitive data from one Task to another. This can be:

- the return value of a `PythonOperator`
- any value using `xcom_push` and `xcom_pull`

As a note, this can be used for a Task to get a reference to the previouse Task instance that just run in it's context: `context['task_instance']`. 

In the example Github repo in the next section, I noticed that I only did `xcom_push` and `xcom_pull` for Tasks that ran sequentially.

## Github Repo for learning

I created this repo for learning Airflow and trying out the above features:

[https://github.com/aaronlelevier/apache_airflow_examples](https://github.com/aaronlelevier/apache_airflow_examples)

## Notes from YouTube video "[A Practical Intro to Airflow](https://youtu.be/cHATHSB_450)"

These are my notes from Matt Davis' talk at PyData SF 2016.

This video was super helpful in filling in the gaps in conceptually understanding Airflow in combination with the Airflow documentation.

### Airflow Concepts

**metadata db**

sqlite

mysql

postgres

**webserver**

flask

**scheduler**

nothing can run without this

crawls the configured dir's to find DAGs

**celery**

tasks are sent from the scheduler to run on Celery workers

would use *rabbitmq* or *redis* for Celery Queue

### Airflow objects

Tasks

Executors (workers)

### Code

**Useful DAG Arguments**

`start_date` - will say when to start, if in the past, Airflow will backfill the tasks to that date based on the `schedule_interval`

- can put the `start_date` for the future, if we don't want it to run yet

`schedule_interval` - cron config

- max interval to run should be at fractions of hour, not per minute, because Airflow kicks off tasks every 30 seconds

`default_args` - arguments supplied to the `DAG`, but get passed to the `Operators`

`max_active_runs` - can set globally or per Pipeline how may parallel pipelines to run at the same time

`concurrency` - max number of tasks run in a single Pipeline to run at a sinble time

can retry tasks

can put timeouts in Pipeline for when tasks start

**Useful Task Arguments**

`retries` -how many times to retry

`pool` - a worker pool - can limit slots here

`queue` - named Celery Queues - and assign certain Workers to a Queue based upon the type of Worker if biefy, lightweight, etc..

`execution_timeout` - set a max time for a Task to run

`trigger_rule` - default is "all upstream tasks are successful. Can change to things like

- "all upstream tasks failed"
- "all upstream tasks are done" - either success or fail

args for python

env vars

template vars

`provide_context` - supplies a dict of Task arguments, like "execution date", from Airflow context

`op_args` - positional arguments for the Task

`op_kwargs` - kwarg arguments supplied to the Task

**Executors**

`CeleryExecutor` - for prod, puts exec request on a queue and sends it to a Celery Worker

`SequentialExecutor` - good for debugging, will stop scheduling to run Tasks

`LocalExecutor` - uses Python's `multiprocess` module to run in a diff process, so Scheduler can continue scheduling things

- used in Prod for some companies - if don't want a distributed worker queue

`MesosExecutor`

**Local debugging**

To use `pdb`, use the `SequentialExecutor`, and run `airflow test` to hit `pdb` debugger

**Local Pipeline testing**

`start_date` - should be some date in the past

`schedule_interval='@once'`

can delete a DAG using the UI, in order to re-run this Local Pipeline for testing

**Separate Business Logic**

develop code first, then integrate with Airflow

**Deploying new code**

to get new Python code, we have to restart the process, so new code is imported. to do this with Airflow, we can do

`airflow scheduler --num_runs` - this will stop the scheduler after `num_runs` has occurred. You need a separate mechanism to restart the scheduler. Speaker uses a bash script

`CELERYD_MAX_TASKS_PER_CHILD` - will configure Celery workers to restart after the "max tasks"

speaker sets the above to 1 max, so each run, always gets new deployed code

## Conclusion

So far, so good. By no means is this all Airflow can do, and is the above blog exhaustive. Thanks for reading!
