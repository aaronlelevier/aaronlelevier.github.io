---
layout: post
title: Training the maskrcnn-benchmark on my own hardware
tags: [Machine Learning, Python, COCO dataset, maskrcnn-benchmark, PyTorch]
---

My goal is to train a Machine Learning model on my own hardware and my own labeled dataset. In order to do this, I've been ramping up on the tools and software necessary to do this. This blog post is about **Training the [maskrcnn-benchmark](https://github.com/facebookresearch/maskrcnn-benchmark) on my own hardware**

## Initial detour

I'll start where I left off from my last [post](https://aaronlelevier.github.io/training-an-ml-model-on-the-coco-dataset/), which was titled *"Training an ML model on the COCO Dataset"*, but I hadn't fully trained a model, I had run a model over a couple of mini-batches of the COCO dataset.

After my last post, I decided to upgrade my Linux kernal headers unknowningly. Well, come to find out Ubuntu 18.04 with linux-headers `4.15.0-45-generic` doesn't currently work with Cuda 10.0 drivers. I tried fixing it a variety of ways, and wasn't sure why it was working, but in the end, I downgraded back to `4.15.0-29-generic` and it is now working.

If you run into a similar issue and want to downgrade, how I did it was, check the linux-headers here:

```
$ ls /lib/modules/
4.15.0-29-generic  4.15.0-45-generic
```

Then in `grub`, you can set the preference for choosing what linux-headers you want to use at start up like so:

```
# /etc/default/grub

#GRUB_DEFAULT=0
GRUB_TIMEOUT_STYLE=hidden
GRUB_TIMEOUT=-1
GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
GRUB_CMDLINE_LINUX=""
```

Then run `sudo update-grub` and `reboot` for the config to take effect.

## Let's train the model

Now that Cuda drivers are working, I trained the [model](https://github.com/facebookresearch/maskrcnn-benchmark) using this command

```
nohup python tools/train_net.py --config-file "configs/e2e_mask_rcnn_R_50_FPN_1x.yaml" SOLVER.IMS_PER_BATCH 2 SOLVER.BASE_LR 0.0025 SOLVER.MAX_ITER 720000 SOLVER.STEPS "(480000, 640000)" TEST.IMS_PER_BATCH 1 &
```

`nohup` will run the process in the background.

This is a large model. My hardware is a Nvidia 1080Ti with 11GB of GPU memory. The model is usually run on a cluster of 8 GPUs with a mini-batch of 16. On a single GPU, they recommend a mini-batch of 2. This takes up 6-10GB of memory depending on the image size.

The run time is also long. At 720,000 iterations above on the 1080Ti, it will run for 3.5 days.

After 2 days, I got excited and wanted to see how the model is doing. Below is my trained model, and the original model.

### My model

![Imgur](https://i.imgur.com/ldcvI4o.png)

### Original model

![Imgur](https://i.imgur.com/fZUh70j.png)

## Okay, continue training

I started the model again. It will load the previous checkpoint, and continue training.

I first change the iterations to 300,000 thinking that I should lower to about how many I had left, but the model must know the total expected iterations, because when I did this, the model thought that it was done, and ran the validation set.

I changed the command back to the original 720,000 iterations, and the model loaded it's last checkpoint, started training again, and calculated 1.5 days left.

## The Nvidia 1080Ti GPU

So far, the GPU has been running like a champ. I got it used off eBay, so you never know, but so far so good. It's been at 72c degrees max. The process hasn't failed, and ran continuously for the first 2days.

## What's next

I'm going to let the GPU finish training, run validations for the original vs. my trained model and compare. This comparison will be for spot checking individual images, but also with the validation set. The model returns these statistics for overall model performance. The below are after two days of training, so my plan is to evaluate after the full 3.5 days of training and also the original model to see if I can produce the same results.

```python
OrderedDict([('bbox',
              OrderedDict([('AP', 0.2995932418350566),
                           ('AP50', 0.5048334612699799),
                           ('AP75', 0.3199970069827478),
                           ('APs', 0.17024760135017813),
                           ('APm', 0.33163478543717106),
                           ('APl', 0.38858065511848544)])),
             ('segm',
              OrderedDict([('AP', 0.28114866256991533),
                           ('AP50', 0.47389863964406576),
                           ('AP75', 0.2971631326535043),
                           ('APs', 0.12308321652841664),
                           ('APm', 0.30504965888965696),
                           ('APl', 0.41763089921672736)]))])
```
