---
layout: post
title: PyTorch Developer Conference 2018 - PTDC - part 1
tags: [PyTorch, Machine Learning, AI, Python, C++]
---

This is my cliff notes style blog about my experience at PyTorch Developer Conference that happened on October 2, 2018. This is part 1 because as I was going through my notes, there was so much content and things to read and explain more, that it couldn't easily fit into one blog.

## Talks

The talks section is in loose chronological order of the [speaker schedule](https://pytorch.fbreg.com/schedule)

Here are the links to all videos from the conference:

- [PyTorch Developer Conference Part 1](https://youtu.be/JVT4XvixNvs)
- [PyTorch Developer Conference Part 2](https://youtu.be/8881p8p3Guk)
- [PyTorch Developer Conference Part 3](https://youtu.be/KJAnSyB6mME)


### Keynote Jerome Presenti

[DensePose](http://densepose.org/)

[PyTorch 1.0](https://hackernoon.com/pytorch-1-0-468332ba5163)

Current flow to get PyTorch into production is:

Pytorch -> [ONNX](https://pytorch.org/docs/stable/onnx.html) -> [Caffe2](https://caffe2.ai/)

PyTorch 1.0 is about making this a more seemless process with the [torch.jit](https://pytorch.org/docs/master/jit.html) module. 

We need testing and tooling for ML, like software development 20 years ago. A seamless process to get PyTorch into production should exist, so `torch.jit` was created.

Hardware breakthroughs like the [volta](https://www.nvidia.com/en-us/data-center/volta-gpu-architecture/) have accelerated ML research.

[Operator fusion](https://arxiv.org/pdf/1801.00829.pdf) now speeds up training times.

### Deep Dive on PyTorch 1.0

The goal of PyTorch 1.0 is to make putting PyTorch models into production as seamless as possible. For this, the PyTorch team is also considering:

- Research and flexibility is central to PyTorch.

- Production constraints are:

    - hardware efficiency
    - scalability
    - cross platform

Currently [ONNX](https://pytorch.org/docs/stable/onnx.html) is the way to put PyTorch models into production.

With PyTorch 1.0 comes the introduction of the [torch.jit](https://pytorch.org/docs/master/jit.html) module. This module allows the developer to write code once, and with the use of `torch.jit.trace` decorators and other helpers from the module, the Python PyTorch model will be output to run independently from Python, for instance in a C++ program, and be production ready.

PyTorch model development workflow that's possible as of 1.0:

- experiment with models in Python
- extract the model using a `torch.jit.script`
- optimize and deploy

Torch scripts do operator fusion for algebraic simplification.

#### `torch.jit` module

Functions are decorated with `torch.jit.script`, while subclasses of `torch.jit.ScriptModule` use a `torch.jit.script_method` decorator. Also:

- records control flow
- uses a subset of Python
- more info here: [https://pytorch.org/docs/master/jit.html#torch.jit.ScriptModule](https://pytorch.org/docs/master/jit.html#torch.jit.ScriptModule)

`torch.jit.trace` does the following:

- runs code straight through
- records what happens
- can run later without Python present
- more info here: [https://pytorch.org/docs/master/jit.html#torch.jit.trace](https://pytorch.org/docs/master/jit.html#torch.jit.trace)

Models can then be saved to disk.

[Tutorial for loading a PyTorch module to C++](https://pytorch.org/tutorials/advanced/cpp_export.html)

PyTorch library hierarchy described as:

```
Aten
 | 
Autograd
 |      \
 |    Python script
C++ extensions
```

[Custom C++ exetensions for PyTorch can be written](https://pytorch.org/tutorials/advanced/cpp_extension.html)

- Uses [PyBind](https://github.com/pybind/pybind11)
- `setup.py` can load the custom extension [can load](https://pytorch.org/tutorials/advanced/cpp_extension.html#building-with-setuptools) the custom extension

Deep learning C++ bare metal for ML

All links available at [pytorch.org/cppdocs](https://pytorch.org/cppdocs/)

[Distributed training](https://pytorch.org/tutorials/intermediate/dist_tuto.html) uses [C10D](https://github.com/pytorch/pytorch/tree/master/torch/csrc/distributed/c10d)

- performance driven C++ backend with Python frontend
- uses futures with `async_op=True`
- [distributed_c10d.py](https://github.com/pytorch/pytorch/blob/dfa03e94ebf24b12e889f749c481ed687441cf75/torch/distributed/distributed_c10d.py)
- communication overlap
- smart gradient sharing

`torch.distributed` is deprecated in favor of `C10D`

### Fairseq

[Fairseq](https://github.com/pytorch/fairseq) provides a sequence modeling toolkit

Seq2Seq library that has been instrumental at FB

Won the Global Machine Translation 2018 competition

Trains machine translations (MT) in both directions

### PyTorch Translate

[https://github.com/pytorch/translate](https://github.com/pytorch/translate)

- predict content language
- predict view language

Uses this flow

```
Alten -> decode
            \
            C++ Beam search
           /
Encoder -
```

[FBGEMM for quantization](https://code.fb.com/ai-research/rosetta-understanding-text-in-images-and-videos-with-machine-learning/)

[PyTorch Text](https://github.com/pytorch/text) has DataLoaders and abstractions for NLP

### AI at Facebook

2.2B Users

300+ trillion predictions made per day

FB AI Infrastructure runs many experiments per day

Things that FB needs to achieve it:

- AI as a service
- Data platform
- AI foundation

Current library relationship

```
PyTorch - research
 |
ONNX - transferring
 |
Caffe2 - production
```

Things that help scaling ML learning

- increased batch sizes
- increased learning rate
- overlap with training and balance

### More notes about the current ML environment

Models are needed for a highly fragmented hardware world. Mobile is highly fragmented and faces size constraints. Python isn't always present, so production models should run without needing Python.

[Quantization](https://arxiv.org/abs/1806.08342) has been proven to speed up training without hurting model accuracy.

[LibTorch](https://anaconda.org/anaconda/libtorch) C++ frontend for PyTorch is now available.  Or, for download here [https://download.pytorch.org/libtorch/nightly/cpu/libtorch-macos-latest.zip](https://download.pytorch.org/libtorch/nightly/cpu/libtorch-macos-latest.zip)


### People I met

The community was so friendly and welcoming. Coming from a software development background and not data science, with my knowledge of data science from online classes I was able to communicate, learn and understand everyone at the conference.

Some people I met were:

- Conor - ML Intern
- Tom - CTO at Paperspace
- Francisco - ML Intern at fast.ai
- Fedro - Data scientist working with Yann LeCun
- James - core PyTorch Dev

### Next

I'll be working on part 2 of this blog in the same style as this one. It will be a continuation of material presented in the conference with lots of links. More great PyTorch to come :)
