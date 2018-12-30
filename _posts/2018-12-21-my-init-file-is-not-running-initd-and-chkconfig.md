---
layout: post
title: My init file is not running - init.d and chkconfig
tags: [init.d, chkconfig, bash, strace, ps]
---

![Imgur](https://i.imgur.com/PMHxDFs.png)

So, the problem to solve is that an `init.d` script isn't running and I'm not sure why. When this problem first occurred I hit Google, and was still lost. After Googling and asking around, here is how to solve it and some helpful commands.

## Initial Start

At the start, the contents of my script, let's call it `my-init`, looked like this:

```
#!/bin/bash
# chkconfig:  - 85 15
# start(), stop(), etc...
```

I had attempted to add it to the `init.d` startup scripts by calling:

`sudo chkconfig --add /etc/init.d/my-init`

The first problem was that there were no run levels. This line:

`# chkconfig:  - 85 15`

Has a `-` where the run levels should go. I changed my runlevels to: `# chkconfig:  345 85 15`  and then ran these commands to re-add my script:

```
# remove the old file
sudo chkconfig --del /etc/init.d/my-init

# add file back with new changes
sudo chkconfig --add /etc/init.d/my-init
```

This site has a good description of runlevels:

[https://www.tldp.org/HOWTO/HighQuality-Apps-HOWTO/boot.html](https://www.tldp.org/HOWTO/HighQuality-Apps-HOWTO/boot.html)

Okay, now runlevels are fixed, but it isn't running. If that's fixed, then where to look next?

## Look in `/etc/`

If `my-init` was added correctly, then the file should be in the `/etc/init.d/` directory. Run `ls /etc/init.d/` and the file should be listed.

Each runlevel has a directory under `/etc/` named `/etc/rc<run-level>.d/`, so `/etc/rc3.d/` for all init scripts that have a runlevel of 3.

If the script has been correctly added to runlevel 3 for example, run this command:

`sudo ls -l /etc/rc3.d/`

And it should show a symlinked file, like:

`/etc/rc3.d/S85my-init -> /etc/init.d/my-init`

The `85` is the order number that the script will be called at system boot. init scripts are called in ascending order from `1 - 99`

Okay, so the script is correctly linked, but it's still not getting called, where next?

## ps and strace

We can look at all running processes and the command used to envoke them using:

`ps -ef`

The output is something like:

```
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 02:15 ?        00:00:01 /sbin/init
root      3177  1915  0 02:16 ?        00:00:00 /bin/sh /etc/rc3.d/S82something start
```

At this point, we should be looking for a process that is running that was invoked by the system start. The system is stuck on an init script with a lower level then ours. In this case `82`

A couple of things can be done now. `strace`, which may be present or can be installed from the package manager, can be used to inspect the current running process and what it's doing, by running:

```
strace -f -y -p <PID>
```

This will show the current output. If there's nothing useful, then try invoking the failing startup script with verbose output using `-x` and see what is happening when it first get's invoked. Command:

`sudo bash -x /etc/rc3.d/S82something start`

This should show something useful output.

At this point, the issue was solved and the script was looking for some content it couldn't find. After that failed, it was polling, trying to find it again, and repeat, so it was never exiting.

## Conclusion

For me, the problem to be solved and how these commands and concepts go together helped me remember and be able to debug when it happened relatively soon again on a different script and issue. I hope that this helps you as well. Thanks for reading.

-Aaron
