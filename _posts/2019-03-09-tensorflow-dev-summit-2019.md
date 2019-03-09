---
layout: post
title: Tensorflow Dev Summit 2019
tags: [tensorflow, python]
---

![Imgur](https://i.imgur.com/Y2avwJV.png)

This is my blog post summary of the [Tensorflow Dev Summit 2019](https://www.tensorflow.org/dev-summit). I applied to go to the conference, but wasn't accepted. Google sent me an email saying that I could still attend via the live stream, so I took off to watch the live stream and learn.

I attended the last Pytorch Dev Con in Octoboer 2018. I've been pretty active in following machine learning and learning more about it and experimenting in my free time for about 1.5 years. My full time job is as a Python Developer working on internal tools.

Okay, to the conference.

## The conference

The conference started out with an overview of the current Machine Learning landscape. Recent advances [BERT](https://github.com/google-research/bert) for NLP, and Open AI's [GPT-2](https://blog.openai.com/better-language-models/) model for NLP were discussed.

Models have been built like [Aircognizer](https://medium.com/tensorflow/air-cognizer-predicting-air-quality-with-tensorflow-lite-942466b3d02e) that predicts air quality based on computer vision. There's a [Google Play app](https://play.google.com/store/apps/details?id=com.bvpiee.com.airmirror&hl=en_US) for this.

There's break throughs all the time in open datasets such as the [open images dataset](https://storage.googleapis.com/openimages/web/index.html).

I'm going to include a library section below. So may libraries were released or now have new versions and features. The big release is Tensorflow 2.0.

## Tensorflow 2.0

[Tensorflow 2.0](https://www.tensorflow.org/alpha) was released.

Keras API is now the recommended way to express TF models.

Eager execution is the default.

Functions with dynamic control flows can now be decorated with `@tf.function` and be used in TF, just like [PyTorch](https://pytorch.org/docs/stable/jit.html) with `@torch.jit.script`

Saved models use the same format in development and prod, so the same exported model can be used in both places, and doesn't have to be converted.

Tensorboard can be used in Google Colab. Here is a [link](https://colab.research.google.com/github/google/dopamine/blob/master/dopamine/colab/tensorboard.ipynb#scrollTo=KS3rXKgsjiiY) to an example. I just ran the example and it uses [ngrok](https://ngrok.com/). Way to ngrok, that's awesome!

### Orchestration

TF has chose to standardize on Orchestration for what everyone is already using instead of providing their own solution. Supported Orchestration frameworks are [Apache Airflow](https://airflow.apache.org/) and [Kubeflow](https://www.kubeflow.org/)

### Online courses

Both Udacity and Deeplearning.ai are going to have online courses

### Hackathons

There's a [Devpost](https://tensorflow.devpost.com/) Hackathon with $150k in prizes. Wow!

### Interface programming

`tf.raw_ops` exists for using the same ops that TF uses

There's a set of base components for checkpoints, layers, etc... and these base components can be extended to write your own components.

`tf_upgrade_v2` to upgrade TF 1.x code to TF 2.0

## Tensorflow.js

Now supports Electron apps

There are off the shelf models for use

## Tensorflow Swift

There's going to be a new [fast.ai tensorflow swift](https://www.fast.ai/2019/03/06/fastai-swift/) class. Jeremy Howard, I a little bit couldn't believe it, if you are reading this! I'm excited to take a look at the class though. I love Jeremy Howards teaching style and the way he explains things. If I can get time and the class aligns with other goals, etc... I am pretty interested.

## Tensorflow Special Interest Groups (SIGs)

There are special interest groups within Tensorflow for different parts of the community. There's a SIG for Rust.

## Tensorflow Extended (TFX)

Tensorflow Extended is an end-to-end ML solution. As of now, all components have been open sourced by Google. This and TF 2.0 were the #1 things that blew me away.

Here's a couple of screen shots from the talks that overview what goes into a production ML workflow and the components involved.

![Imgur](https://i.imgur.com/XzpYIF5.png)

![Imgur](https://i.imgur.com/hnWCK6x.png)

I went through the [Tensorflow Extended](https://www.tensorflow.org/tfx) tutorial for example Chicago Taxi Cab model. Everything worked amazing. It uses Apache Airflow, all parts of TFX, gRPC to send requests to TF Serving.

## Libraries

[Tensorflow Hub](https://www.tensorflow.org/hub) - TensorFlow Hub is a library for reusable machine learning modules.

[Tensorboard](https://github.com/tensorflow/tensorboard) - TensorFlow's Visualization Toolkit

- has a ton new features, and is also now natively supported in Jupyter Notebook and Google Colab

[Tensorflow Model Analysis](https://github.com/tensorflow/model-analysis) - Model analysis tools for TensorFlow

[Tensorflow Probability](https://github.com/tensorflow/probability) - Probabilistic reasoning and statistical analysis in TensorFlow

[Tensorflow Agents](https://github.com/tensorflow/agents) - TF-Agents is a library for Reinforcement Learning in TensorFlow

[Tensorflow Tensor2Tensor](https://github.com/tensorflow/tensor2tensor) - Library of deep learning models and datasets designed to make deep learning more accessible and accelerate ML research.

[Tensorflow Federated](https://www.tensorflow.org/federated) - TensorFlow Federated: Machine Learning on Decentralized Data

[Tensorflow Privacy](https://github.com/tensorflow/privacy) - Library for training machine learning models with privacy for training data

[Tensorflow Extended](https://www.tensorflow.org/tfx) - TensorFlow Extended (TFX) is an end-to-end platform for deploying production ML pipelines

[Tensorflow Lite](https://www.tensorflow.org/lite) - TensorFlow Lite is a lightweight solution for mobile and embedded devices

[Tensorflow.js](https://www.tensorflow.org/js) - A WebGL accelerated, browser based JavaScript library for training and deploying ML models.

### Talks Reference

[All talks from Tensorflow Dev Summit 2019](https://www.youtube.com/playlist?list=PLQY2H8rRoyvzoUYI26kHmKSJBedn3SQuB)

## Conclusion

I'm running out of time for the day. This isn't everything, but it covers a lot. I hope you enjoyed readying and found some useful references. Thanks.
