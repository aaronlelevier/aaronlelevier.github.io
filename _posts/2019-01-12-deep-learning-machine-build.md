---
layout: post
title: Deep Learning Machine Build
tags: [Hardware, Linux, Wifi adapter, CUDA, Jupyter, Bash]
---

This blog is about my experience building my first Deep Learning machine. There are plenty of great blogs and videos on how to do this. If you're interested in how to do this only, skip to the **References** section, and I put links to all of the blogs / videos that I used.

# Acknowledgements

This blog is dedicated to my wife. Without her support, none of this would be possible. My wife told me 6 months ago that I had put a lot of time into machine learning, and I should stick with it. She wouldn't let change my direction!

# Preface

One thing that is ringing true for me lately and with this whole project is:

> People can do anything. You might not know how to do it yet but just go for it!

Nobody helped me do this as in writing any actual code or physically assembling things. One person gave me advice on Wifi drivers, thanks Evangelos!, but other than that I figured it out :)

# My Story

Okay, so the story...

I got into [PyTorch](https://pytorch.org/). I had tried Keras and Tensorflow as well, but for some reason PyTorch stuck and I really liked the API. It has pretty much the same API as `numpy` but with GPU  support and for machine learning.

I went to the [Pytorch Developer Conference](https://aaronlelevier.github.io/PyTorch-Developer-Conference-2018-part-1/) October 2, 2018, and had just been excited since.

I had been using [Paperspace](https://www.paperspace.com/) for running models on a GPU that I rented hourly at `$0.50` an hour plus `$8` per month for persistent storage. This worked okay, but my monthly costs were going up as I was getting more into PyTorch, so it started to feel like it was the right time to invest in my own machine. I started at `$15` a month, and the last month was `$34`. The astute will notice this is `$360` a year. So, if I can make a `$1800` DL machine build last 5 years, then I break even at my current usage, with only power as an additional cost, plus I can use the machine any amount on top of that.

I decided to build the machine myself instead of paying someone to assemble it. I followed a great [YouTube]((https://youtu.be/OZaFqY8UF6I)) video. It's also in the References section.

Installing the USB Wifi Adapter was probably the hardest part. I did a separate [blog](https://aaronlelevier.github.io/install-usb-wifi-dongle-on-ubuntu-18.04/) on it.

Installing the CUDA drivers was pretty easy, following Nvidia's very thorough documentation. There's a link in the **References**.

## Some things I learned

Assempling the DL machine scared me. In the YouTube video they say to be careful at every point or you coulld bend a pin or break something. I was super careful, and didn't break anything, it just took longer.

Coming from a software background and doing unit testing, it scared me that the feedback loop for assembling the DL machine and to know if it was successful was super long. Once assembled though, small teaks and confirming that things were powered on worked. Things that I had to test and tweak were:

- the hdmi input - if you have a GPU the hdmi has to be plugged in to the GPU hdmi port, not the motherboard hdmi port
- what usb ports are available. The command `lsusb` will tell you this

The whole build was a learning experience. I didn't know anything about setting up a Wifi adapter. I learned a lot and did a separate blog about it [here](https://aaronlelevier.github.io/install-usb-wifi-dongle-on-ubuntu-18.04/)

I learned to follow the directions that come with the Motherboard. I was Googling for what goes where and a diagram, but there was instructions in the box that I didn't look at until I thought to check the box!!

Same for the power supply, there's instructions in the box.

RAM is CPU specific. There's a list of supported RAM sticks that work with the specific CPU. I first ordered RAM, and it said Intel on it, but my CPU is AMD. I didn't install it, did some research, and had to return it and get the right RAM. Lucky for me, Newegg has a great return policy.

"You will need a monitor, keyboard, and maybe mouse". I first thought, no I just plug my Macbook into the DL machine. This was maybe me not thinking it through. It might be possible, but for the simplist install, use these things.

An ethernet cable is needed to set up the USB Wifi Adapter. Most motherboards don't come with Wifi. I had to purchase this separately later once I realized that I needed it.

## Parts list

Here is my parts list for the build:

- Case - [Anidees AI-Crystal-AR Mid Tower](https://www.amazon.com/gp/product/B07D4MN8R7/ref=ppx_yo_dt_b_asin_title_o03__o00_s00?ie=UTF8&psc=1)
- CPU -  [AMD Ryzen 7 2700X](https://www.amazon.com/gp/product/B07B428M7F/ref=ppx_yo_dt_b_asin_title_o04__o00_s00?ie=UTF8&psc=1)
- GPU - [GIGABYTE GeForce GTX 1080Ti](https://www.ebay.com/itm/GIGABYTE-GeForce-GTX-1080-Ti-Gaming-OC-11GB-GDDR5X-Video-Card-White-/283301035112?_trksid=p2047675.l2557&ssPageName=STRK%3AMEBIDX%3AIT&nma=true&si=1%252FBZEwhqjFA%252FZehikkOSe58oRkY%253D&orig_cvip=true&nordt=true&rt=nc)
- RAM - [G.SKILL TridentZ RGB Series 16GB (2 x 8GB)](https://www.amazon.com/gp/product/B06WP4L3D7/ref=ppx_yo_dt_b_asin_title_o01__o00_s00?ie=UTF8&psc=1)
- SSD - [SAMSUNG 970 EVO M.2 2280 500GB NVME SSD](https://www.newegg.com/Product/Product.aspx?Item=N82E16820147690)
- Motherboard - [ASUS Prime X470-Pro](https://www.newegg.com/Product/Product.aspx?Item=N82E16813119100)
- Power supply - [EVGA SuperNOVA 1000W](https://www.newegg.com/Product/Product.aspx?Item=9SIA6ZP76J4883)
- USB Wifi Adapter - [COMFAST Wireless WiFi Adapter](https://www.amazon.com/gp/product/B078MJB351/ref=ppx_yo_dt_b_asin_title_o00__o00_s00?ie=UTF8&psc=1)
- USB thumb drive - [SanDisk 64GB USB](https://www.amazon.com/gp/product/B007JR5304/ref=ppx_yo_dt_b_asin_title_o01__o00_s01?ie=UTF8&psc=1)

Miscellaneous

- tools to assemple - [iFixit Mako Driver Kit - 64 pieces](https://www.amazon.com/gp/product/B0189YWOIO/ref=ppx_yo_dt_b_asin_title_o02__o00_s00?ie=UTF8&psc=1)
- 27 inch LG monitor
- keyboard
- mouse
- ethernet cable

# Images

DL Machine

![Imgur](https://i.imgur.com/ra8araR.jpg)

All the boxes

![Imgur](https://i.imgur.com/CMK6mif.jpg)

# Jupyter Notebook

I'm putting a section for this so I remember!

First, port forwarding must be setup for the `8888` port for the Wifi Home network to port forward to the DL machine.

Launch Jupyter on the server

```
jupyter notebook --no-browser --port=8888
```

On the client setup port forwarding

```
ssh -N -f -L localhost:8888:localhost:8888 -i ~/.ssh/my.pem  username@hostname
```

Go to `localhost:8888` in the browser and Jupyter should be loaded.

# Useful commands

To see which ssh processes are running, this will show ssh port forwarding

```
ps aux | grep ssh
```

Kill a process by PID

```
kill -9 <pid>
```

List all Process PIDs accessing a Port

```
lsof -ti:<port>
```

Kill all processes accessing a port

```
lsof -ti:<port> | xargs kill -9
```

`wget` in background

```
wget -bqc url
```

# References

Nvidia official CUDA Toolkit Documentation:

[https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#ubuntu-installation](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#ubuntu-installation)

Nvidia CUDA Downloads Page:

[https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal)

Setup DL Machine Tutorials:

[Gaming PC Build YouTube video](https://youtu.be/OZaFqY8UF6I)

[https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-18-04-bionic-beaver-linux](https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-18-04-bionic-beaver-linux)

[Medium - Build your own deep learning machine](https://medium.com/yanda/building-your-own-deep-learning-dream-machine-4f02ccdb0460)

[The $1700 great Deep Learning box: Assembly, setup and benchmarks](https://blog.slavv.com/the-1700-great-deep-learning-box-assembly-setup-and-benchmarks-148c5ebe6415)
