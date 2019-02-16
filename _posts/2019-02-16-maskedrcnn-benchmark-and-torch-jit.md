---
layout: post
title: Convert a PyTorch model to C++ - using maskedrcnn-benchmark and torch.jit - Part 1
tags: [Python, PyTorch, C++, Machine Learning, maskedrcnn-benchmark, production]
---

The next step in my project for putting a machine learning model in production is to put an initial model in production! So..., I'm somewhere towards the first full iteration. Obviously, a production machine learning model will need to be accessed, a data pipeline, etc..., and I haven't done that yet, but first let's convert a [PyTorch](https://pytorch.org) model into `C++`.

## Goal

Convert the `maskedrcnn-benchmark` PyTorch Python model to a C++ model using `torch.jit`

## Story

I'm using the [maskedrcnn-benchmark](https://github.com/facebookresearch/maskrcnn-benchmark) Github library. 

There's an [open PR](https://github.com/facebookresearch/maskrcnn-benchmark/pull/138) for `torch.jit` support.

I pulled down the PR branch, and tried building to see if I can assist.

I first synced up with the *master* branch. (maybe I should have built and run the PR branch first, not sure....)

Ok, now I'm trying to install the additional dependencies of the PR branch. So far, it looks like it requires OpenCV and Pytorch in C++ as dependencies.

When I run `demo/Mask_R-CNN_demo.ipynb` because getting error:

```
error: could not create 'maskrcnn_benchmark/lib/custom_ops.cpython-36m-x86_64-linux-gnu.so': No such file or directory
```

So, I think I need to compile and correctly link `custom_ops.cpp`

When I run `cmake CMakeLists.txt`, like below, here's the output.

command line:

```
(venv) aaron@ubuntu-desktop:~/github/maskedrcnn-benchmark/maskrcnn_benchmark/csrc/custom_ops$ cmake CMakeLists.txt 
```

With error:

```
CMake Error at CMakeLists.txt:11 (find_package):
  Could not find a package configuration file provided by "Torch" with any of
  the following names:

    TorchConfig.cmake
    torch-config.cmake

  Add the installation prefix of "Torch" to CMAKE_PREFIX_PATH or set
  "Torch_DIR" to a directory containing one of the above files.  If "Torch"
  provides a separate development package or SDK, be sure it has been
  installed.


-- Configuring incomplete, errors occurred!
See also "/home/aaron/github/maskedrcnn-benchmark/maskrcnn_benchmark/csrc/custom_ops/CMakeFiles/CMakeOutput.log".
```

Okay, I will try to install LibTorch C++ version

```
cd ~/Downloads
wget -bqc https://download.pytorch.org/libtorch/nightly/cu100/libtorch-shared-with-deps-latest.zip
```

I'm going to wait for this to download and then build. It's a big downlaod, so did it in the background using `wget -bqc`

**Part 1** done. To be continued.