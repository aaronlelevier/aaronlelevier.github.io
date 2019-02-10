---
layout: post
title: Install USB Wifi dongle on Ubuntu 18.04
tags: [Linux, Networking, Wifi, Ubuntu]
---

![Imgur](https://i.imgur.com/Ixs418w.jpg)

To my benefit or downfall, whichever way you look at it, I bought the [Comfast CF-915AC USB Wifi Adapter](https://www.amazon.com/gp/product/B078MJB351/) from Amazon. This proved to be super difficult to install. Me being a noob in Wifi networking in Linux. After 3 part time days of fiddling with it, it is now work. Here's my steps and how I got it working.

Firstly, the USB Wifi Adapter came with a CD Rom to install the driver. I don't have a CD Rom drive, so I hit Google, and started looking for what driver to use and how to install.

Under the [COMFAST Wiki](https://wikidevi.com/wiki/COMFAST) it's listed as using the **RTL8811AU** Realtek chipset.

I tried looking for RTL8811AU drivers via Google, since the product only came with a disk for installation and couldn't find any drivers that matched. The Comfast official driver download links returned `404 page not found` errors in Chinese!

I then found this [Ubuntu formus blog](https://ubuntuforums.org/showthread.php?t=2375603) and it said that the **RTL8812AU** driver could be used.

I then followed this StackExchange answer to get the USB driver **RTL8812AU** correctly installed:

[https://askubuntu.com/a/1045927/324695](https://askubuntu.com/a/1045927/324695)

Using `ifconfig`, the interface was present, but it didn't have an IP address.

I am using `netplan` and my `/etc/netplan/01-netcfg.yml` currently looks like this:

```
network:
  version: 2
  renderer: networkd
  ethernets:
    enp6s0:
      dhcp4: true
      nameservers:
        addresses: [8.8.8.8,8.8.4.4]
  wifis:
    wlx40a5ef40734c:
      dhcp4: true
      nameservers:
        addresses: [192.168.0.1, 8.8.8.8]
      access-points:
        "my-wifi-router-name":
          password: "my-password"
```

This is becasue I have WPA security enabled, so the `netplan` yaml wasn't work.

I then followed this StackExchange answer:

[https://askubuntu.com/a/16588/324695](https://askubuntu.com/a/16588/324695)

Using the `wpasupplicant` package, I generated a `wpa.conf` file as suggested, and using these commands could connect to the Wifi Router

```
# install package
sudo apt install wpa_supplicant

# generates a file
wpa_passphrase SSID PASSWORD > wpa.conf

# command uses the file to connect, and runs as a daemon
sudo wpa_supplicant -i wlx40a5ef40734c -c wpa.conf -D wext -B
```

Everything is now working. After a reboot, the Wifi still connects. I am smiling!

# Steps only

Here are the commands / steps only extracted from the above blogs.

### Install driver

First remove any old drivers in `/usr/src`

Then, install new driver:

```
sudo apt purge rtl8812au-dkms
sudo apt install git
git clone https://github.com/abperiasamy/rtl8812AU_8821AU_linux.git
cd rtl8812AU_8821AU_linux
sudo make -f Makefile.dkms install
sudo modprobe rtl8812au
```

Can view that driver is covered:

```
modinfo rtl8812au | grep A811
```

Run `ifconfig -a` and the Wifi interface should be up.

### Configure netplan

Configure netplan yaml file, `/etc/netplan/01-netcfg.yml` as shown above

Run `sudo netplan apply` to apply changes.

### wpasupplicant

Install this package for WPA security support

```
sudo apt install wpasupplicant
```

### Reboot and check

Reboot computer and check

```
reboot

# should show the wifi interface now with an IP address if working
ifconfig -a
```

## Logging in remotely

There are 3 steps to do this

### 1. Assign a static IP address to your home network

This can be done from logging into your Wifi router. The URL to login will be on the bottom of your Wifi router.

I have a Netgear router, so I

### 2. The DL machine should be DHCP registered to an IP address

For me, this was already done in the previous step using `netplan`

### 3. Add port forwarding

This is configurable when logged in to the Router config. For me, [this Netgear guide](https://www.noip.com/support/knowledgebase/setting-port-forwarding-netgear-router-genie-firmware/) helped me setup port forwarding.

### 4. Test

I tested by connecting to my phone Wifi hotspot with my laptop then tested that I could ssh to the DL machine

```
ssh -i ~/.ssh/my.pem username@hostname
```

# Some interesting points

## ifconfig

`ifconfig` will show internet interfaces that are up

`ifconfig -a` will show all internet interfaces whether they are up or down

`ifconfig` was showing the Wifi interface as up, but with no IP. This meant that the USB Wifi adapter driver (driver) installation worked and it was registered as an interface in `netplan` but couldn't connect to the network. It was the WPA security blocking it at this point.

## lshw

`lshw -C network` will show hardware. `-C network` to only show "network" class of hardware.

After successfully installing the driver, I could see the wifi network as DISABLED. Then running `netplan apply` this show the network as enabled.


# Commands used

```
# list usb ports and connected devices
lsusb

# configure network interfaces
ifconfig

# configure wifi network interfaces
iwconfig

# get detailed wifi info
iwlist <interface> s

# dynamic kernal support module
dkms

# ip show an manipulate routing, network devices, interfaces
ip link set <interface> up/down

# list hardware
lshw -C network


netplan apply

netplan --debug generate

# check if there's internet
ping -c3 www.ubuntu.com
```
