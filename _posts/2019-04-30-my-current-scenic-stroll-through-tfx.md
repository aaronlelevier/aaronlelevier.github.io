---
layout: post
title: My Current Scenic Stroll Through TFX
tags: [TFX, Tensorflow, Python, Apache Airflow, Apache Beam, Learning]
---

This is a blog is about my current an ongoing stroll through the [TFX](https://github.com/tensorflow/tfx) library.

## Why TFX?

The opening line of the TFX [README](https://github.com/tensorflow/tfx/blob/master/README.md) says it all. It says:

> TensorFlow Extended (TFX) is a Google-production-scale machine learning platform based on TensorFlow. It provides a configuration framework to express ML pipelines consisting of TFX components.

This is so compelling. The README also says, it's a:

> framework for building end-to-end ML Pipelines

So, I plan to discuss and document what I've seen with TFX so far.

Ok, let's go.

## My Goal

My goal and strategy when doing this scenic stroll is to build my own TFX Pipeline for the [MNIST](https://en.wikipedia.org/wiki/MNIST_database) dataset and ML models.  The example TFX Pipeline uses the Chicaco Taxi Cab dataset and CSV flat files. By building a slightly more complicated Pipeline, it is forcing me to learn the TFX Framework.

## The Start

When I first started, I though, I'll just plug in MNIST data at the correct file path, and everything will just work. But, it didn't...

I next thought, okay, let me tweak a little bit of code. I started to read the source code, and try to do this, but I didn't understand the source code.

[Apache Airflow](https://airflow.apache.org/), then [Apache Beam](https://beam.apache.org/), what are these things? These are the first 3rd party libraries that you run into when reading the TFX source.

### Apache Airflow

Airflow is for creating workflow pipelines as [directed acyclic graphs](https://en.wikipedia.org/wiki/Directed_acyclic_graph).

I did a separate blog post of Airflow [here](https://aaronlelevier.github.io/what-i-know-about-apache-airflow-so-far/) detailing learnings.

### Apache Beam

Beam is for implementing batch or streaming jobs with a single programming model that uses [MapReduce](https://en.wikipedia.org/wiki/MapReduce) with windows and triggers.

For Beam, the [core-overview](https://beam.apache.org/documentation/programming-guide/#core-beam-transforms) in the official documentation was really good.

This YouTube video, [A Whirlwind Overview of Apache Beam](https://youtu.be/buXqe0YQjMY) was also really good for helping to understand Beam.

Then coding along and doing the core transforms helped make them real before trying to do Beam transforms in TFX. Repo link here: [aaronlelevier/apache_beam_examples](https://github.com/aaronlelevier/apache_beam_examples)

Okay, here's the steps that I've gone through of TFX so far.

## Details on TFX Pipeline Steps 1-4

I have been tweaking my work flow for trying to run each Pipeline Airflow Operator.

The first thing that helped me was to symlink the Airflow pipeline file [mnist_pipeline_simple.py](https://github.com/aaronlelevier/tfx/blob/statistics_gen/tfx/examples/mnist/mnist_pipeline_simple.py) to `~/airflow/dags/mnist/mnist_pipeline_simple.py` where Airflow expects to find it.

For debugging Airflow, the steps in a blog post that I did, for *"What I know about Apache Airflow so Far"*, in this section have worked well:
 [Iterate on developing a DAG in Airflow](https://aaronlelevier.github.io/what-i-know-about-apache-airflow-so-far/)

For refreshing the local DBs, I created a helper script: [refresh_mnist_pipeline.sh](https://github.com/aaronlelevier/apache_beam_examples/blob/master/scripts/refresh_mnist_pipeline.sh) This way any changes to the Pipeline wont cause a fail due to stale Database schema, data, etc..

### ExamplesGen

Here, going through the Apache Beam [core-transforms](https://beam.apache.org/documentation/programming-guide/#core-beam-transforms) was important to know what's possible.

[CoGroupByKey](https://beam.apache.org/documentation/programming-guide/#cogroupbykey) is needed here to combine 2 files in the case of MNIST, where the image data and labels are in separage Gzip files. `CoGroupByKey` is used to combine 2 or more Beam `PCollection`'s, then the single `PCollection` can be output to a TFRecord with `beam.io.WriteToTFRecord`.

### StatisticsGen

This step is for running [Tensorflow Data Validation](https://www.tensorflow.org/tfx/data_validation/get_started) (TFDV) on the dataset to generate statistics.

In order to do this and visualize the statistics, [Bazel](https://docs.bazel.build/versions/master/install.html) must be installed. On Mac OSX, I first installed Bazel using Homebrew, but that didn't work, so I installed from source, and it worked. I had created an issue with [tensorflow/data-validation](https://github.com/tensorflow/data-validation/issues/59) but I then closed it once I realized the issue.

[This](https://github.com/tensorflow/tfx/blob/master/docs/tutorials/data_validation/chicago_taxi.ipynb) TFDV example Jupyter Notebook was super helpful for figuring out how to call TFDV.

### SchemaGen

This step uses TFDV to generate a Schema, which is the features, labels, and their types for a given dataset.

### ExampleValidator

This step then uses TFDV to then compare the statistics generated by `StatisticsGen` and the `Schema` generated by `SchemaGen`. TFDV will look for any anomalies between the **train** and **eval** dataset splits, and write them to a file. 

TFDV can also be used to fix these anomalies.

## Next

There's 4 more steps, then [Tensorflow Serving](https://www.tensorflow.org/tfx/guide/serving) can be used to serve the model.

I will report back soon!

Thanks for reading :)
