---
layout: post
title: Converting Labelme annotations to COCO dataset annotations
tags: [Machine Learning, Python, COCO dataset, labelme]
---

This is a short blog about how I converted Labelme annotations to COCO dataset annotations.

## mlearning

I created the repo [mlearning](https://github.com/aaronlelevier/mlearning) for storing Machine Learning utilities, helper code, etc...

The first main addition to this repo is the converter that I wrote. I takes [labelme](https://github.com/wkentaro/labelme) annotated images, and converts them to the COCO dataset 2014 annotations format.

## Why?

I'm training a model on the COCO dataset, so I need a way to generate my own labeled data that can be used by this model. I tried out a few data labeling softwares, like [RectLabel](https://rectlabel.com/) and [LabelBox](https://labelbox.com/), but they were freemium's and didn't give me the output, or weren't that great to use. `labelme` is open source. I plan to contribute back my COCO dataset converter once I use it more, and it becomes more stable.

Let's see the converter in action.

## Example Output

Here's example output from the `mlearning` Github repo.


```python
%matplotlib inline

import os

from matplotlib import pyplot as plt
import matplotlib.pylab as pylab

from mlearning import util
from mlearning.coco import Annotation
from mlearning.plotting import plot_bboxes_and_masks

pylab.rcParams['figure.figsize'] = 12, 12

# must set file paths for one's own data!!!
ann = Annotation(path=os.path.join(os.path.expanduser('~'), 'Desktop/license_plate_detection'))

# this is the function that displays a random example
plot_bboxes_and_masks(ann)
```

![Imgur](https://i.imgur.com/g6l2A3u.png)

## Future plans

I plan to label more images and then train them on the model. I am still doing a proof of concept that I can train on my own hardware, and that the *labelme-to-COCO dataset* converter that I wrote works.
