---
layout: post
title: Using Git Aliases and How to Display the Current Git Branch Name in a Terminal Prompt
tags: [Git, Bash, Productivity, Workflow]
---

Here are two Git workflow hacks that help me be more productive.

## Git Aliases

Git aliases help me to be more productive. With how often we as developers type `git` commands, using aliases allows for less typing and less typos. Here are my current `git` aliases.

<script src="https://gist.github.com/aaronlelevier/4147ac784c543bfd8029f13db4669706.js"></script>

I like to keep the above `git` aliases in a separate file `~/.gitshortcuts` from my `~/.bash_profile`. Then I add `source ~/.gitshortcuts` to my `~/.bash_profile`. This helps keep things neat.

## Display the Current Git Branch Name in a Terminal Prompt

I found myself always typing `git status` to find out what branch I was on before running the next `git` command. Always having the current `git` branch name displayed removes the need to always check this.  Here's my terminal prompt.

<script src="https://gist.github.com/aaronlelevier/d70964e817bcbb96af5b061c48c6c7ef.js"></script>

## Use backup branches (Bonus)

I worked with a senior developer that once told me:

> Behind the scenes I'm always managing a backup branch

This really stuck with me. His convention was to create a backup branch with the suffix `-BAK`. This strategy is really helpful. If you're unsure if a `git rebase` will work, and all conflicts will be resolved correctly or some other series of `git` actions, having a backup branch allows you to easily restore from the last time that you were sure about your changes without having to use `git reflog` and so on.

## Conclusion

That's it for now. I'm sure there's a lot more `git` hacks that I should be using. Drop me a line and let me know!

Thank you for reading.