---
layout: post
title: Training an ML model on the COCO Dataset
tags: [Machine Learning, Python, CUDA, Jupyter, Bash]
---

My current goal is to train an ML model on the COCO Dataset. Then be able to generate my own labeled training data to train on. So far, I have been using the [maskrcnn-benchmark](https://github.com/facebookresearch/maskrcnn-benchmark) model by Facebook and training on COCO Dataset 2014.

Here my [Jupyter Notebook](https://github.com/aaronlelevier/maskrcnn-benchmark/blob/plot-images/demo/Plot%20COCO%20Dataset%20ground%20truth%20images.ipynb) to go with this blog.

Okay here's an account of what steps I took.

## Getting the data

The COCO dataset can be download [here](http://cocodataset.org/#download)

I am only training on the 2014 dataset.

I'm working with this project:

[https://github.com/facebookresearch/maskrcnn-benchmark#perform-training-on-coco-dataset](https://github.com/facebookresearch/maskrcnn-benchmark)

And, it must be linked to the correct directories in order to use it with the Github project:

[https://github.com/facebookresearch/maskrcnn-benchmark#perform-training-on-coco-dataset](https://github.com/facebookresearch/maskrcnn-benchmark#perform-training-on-coco-dataset)

## Training

Here are some training commands. These worked.  Funny enough, the first command is for `720,000` iterations and it reported that it was going to take 3+ days to complete on my GTX 1080Ti. Also, I could only load 2 images at a time and it took up 10 out of 11GB of memory. This is a big model!

1-16-2019

```
python tools/train_net.py --config-file "configs/e2e_mask_rcnn_R_50_FPN_1x.yaml" SOLVER.IMS_PER_BATCH 2 SOLVER.BASE_LR 0.0025 SOLVER.MAX_ITER 720000 SOLVER.STEPS "(480000, 640000)" TEST.IMS_PER_BATCH 1
```

1-17-2019

```
python tools/train_net.py --config-file "configs/e2e_mask_rcnn_R_101_FPN_1x.yaml" SOLVER.IMS_PER_BATCH 2 SOLVER.BASE_LR 0.0025 SOLVER.MAX_ITER 10 SOLVER.STEPS "(480000, 640000)" TEST.IMS_PER_BATCH 1
```

## Some Things that maskrcnn does really well

everything's a hyper param

logging - for lots of feedback

single `tqdm` output for training

## COCO Dataset format notes

Things that I learned about the COCO dataset that will be important in the future for training my own datasets with this format are:

### Images

Image annotations have this format:

```
{'license': 3,
'file_name': 'COCO_val2014_000000391895.jpg',
'coco_url': 'http://images.cocodataset.org/val2014/COCO_val2014_000000391895.jpg',
'height': 360,
'width': 640,
'date_captured': '2013-11-14 11:18:45',
'flickr_url': 'http://farm9.staticflickr.com/8186/8119368305_4e622c8349_z.jpg',
'id': 391895}
```

### Annotations

Annotations have this format:

```
{'segmentation': [[239.97,
260.24,
222.04,
270.49,
199.84,
253.41,
213.5,
227.79,
259.62,
200.46,
274.13,
202.17,
277.55,
210.71,
249.37,
253.41,
237.41,
264.51,
242.54,
261.95,
228.87,
271.34]],
'area': 2765.1486500000005,
'iscrowd': 0,
'image_id': 558840,
'bbox': [199.84, 200.46, 77.71, 70.88],
'category_id': 58,
'id': 156}
```

**segmentation** explained:

I was confused how the `segmentation` above was converted to a mask. The `segmentation` is a list of `x,y` points. In this format: `[x1, y1, x2, y2, etc...]` In this code block, the `segmentation` list of points is reshaped to `[(x1,y1), (x2, y2), ...]` and is then usable by `matplotlib`

```
for seg in ann['segmentation']:
    poly = np.array(seg).reshape((int(len(seg)/2), 2))
```

`poly` becomes an `np.ndarray` of shape `(N, 2)` where `N` is the number of segmentation points.

**bbox** explained:

`bbox` is of format `[x1, y1, x2, y2]`. The bounding box points start at the top left of the image as point `(0,0)`. The `x1,y1` offset is from the `(0,0)` starting point, where the `y` size goes down, since it's starting from the top left. Then the `x2,y2` values are offsets from the `x1,y1` points.

## Conclusion

I've now learned 2 datasets. Pascal and COCO. Now I know a little more why most projects doing image tasks support both.

## What's Next

Next I want to label my own data and train on it. The last [section](https://render.githubusercontent.com/view/ipynb?commit=9d799b96f24ffd7d5f964165dcbf2d0037fd5dba&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6161726f6e6c656c65766965722f6d61736b72636e6e2d62656e63686d61726b2f396437393962393666323466666437643566393634313635646362663264303033376664356462612f64656d6f2f506c6f74253230434f434f2532304461746173657425323067726f756e642532307472757468253230696d616765732e6970796e62&nwo=aaronlelevier%2Fmaskrcnn-benchmark&path=demo%2FPlot+COCO+Dataset+ground+truth+images.ipynb&repository_id=165327326&repository_type=Repository#Plot-my-own-labeled-data) of the notebook is my attempt at this using **RectLabel**

I reviewed 3 different applications for labeling data:

- Labelbox
- RectLabel
- Labelme

My criteria for evaluating is that it should be free and I should be able to run the program locally and label my own data as I please. User friendly is better obviously.

If I can't find something, then maybe I have to create a simple app for labeling data. Definitely doable, but it'd be a detour.

**Labelbox** seems like it used to be open source, but they turned it into a SaaS, and I couldn't get it to run.

**RectLabel** is $5 which isn't bad, but it didn't generate the segmentation data in the format that I need.

[Labelme](https://github.com/wkentaro/labelme) seems exactly what I am looking for. Open source. There isn't a script for exporting to COCO Dataset 2014 format, so maybe this is an opportunity to contribute as well :)

So labeling my own data and training on it is the next step. Okay, until next time.


## Random... Extra

Some random notes about things learned when doing this.

### commands

count files in a dir - in order to check that the file count matches what was expected, or when the `zip` file didn't fully download, or to check the image file count vs. expected.

```
ls -1 | wc -l
```

`wget` in background with no timeout, so I can start the job from my laptop, but process runs as a daemon on the DL machine

```
wget -bqc --timeout=0 url
```

### fastjar

If a `zip` file didn't fully download, `fastjar` can be used to unzip it.

Trying to unzip the file will give you:

```
unzip error “End-of-central-directory signature not found”
```

Use `fastjar` if the whole zip file didn't download:

```
sudo apt-get install fastjar
jar xvf something.zip
```

[StackExchange reference](https://askubuntu.com/questions/54904/unzip-error-end-of-central-directory-signature-not-found)

### nvidia-smi

equivalent to "tail nvidia-smi"

```
# keeps passed traces
nvidia-smi -l 1

# doesn't keep past traces
watch -n0.1 nvidia-smi
```
