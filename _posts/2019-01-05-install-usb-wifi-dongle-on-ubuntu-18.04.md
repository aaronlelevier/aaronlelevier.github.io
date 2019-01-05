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

# Some interesting points

## ifconfig

`ifconfig` will show internet interfaces that are up

`ifconfig -a` will show all internet interfaces whether they are up or down

`ifconfig` was showing the Wifi interface as up, but with no IP. This meant that the USB Wifi adapter driver (driver) installation worked and it was registered as an interface in `netplan` but couldn't connect to the network. It was the WPA security blocking it at this point.

## lshw

`lshw -C network` will show hardware. `-C network` to only show "network" class of hardware.

After successfully installing the driver, I could see the wifi network as DISABLED. Then running `netplan apply` this show the network as enabled.


# Commands used

lsusb

ifconfig

iwconfig

iwlist <interface> s

dkms

ip link set <interface> up/down

lshw -C network

netplan apply

netplan --debug generate

ping -c3 www.ubuntu.com
