---
title: Project management
---

An important part of the [Fab Academy](https://fabacademy.org/), apart from learning digital fabrication techniques, consists of documenting everything we do in order to create a shared and open knowledge base between all students, and for everybody.

One of my goals for this academy is to use only open-source tools. I want to be able to see what is inside the tools I use, modify it in case of need and share with others the projects I do with the environment necessary for their functioning.

> Practice shapes tools, tools shape practice
> > [Open Source Publishing](http://osp.kitchen/)

## My computer

Few months ago, I decided to switch from the closed Apple ecosystem to the wonderful and open world of Linux. I'm running [Elementary OS](https://elementary.io/), a distribution based on Ubuntu, on a mid-2014 macbook pro. This machine isn't the more convenient to run a Linux distribution but I will keep using it as long as I can, even if I have some tiny hardware issues, simply because the more sustainable computer is the one I already have.

- Text editor: [VSCodium](https://vscodium.com/) + [NeoVim](https://neovim.io/)
- Terminal: [Terminator](https://github.com/software-jessies-org/jessies/wiki/Terminator)
- version control system: [GIT](https://git-scm.com/)
- Static site generator: my own "spaghetti script" that I wrote in Python
- Browser: [Firefox](https://www.mozilla.org/en-US/firefox/new/)

---

# My ideal documentation tool

My ideal documentation tool is as light as possible and requires very little energy to operate; is perfectly understandable and does the tasks I want it to do - nothing more; evolves with my needs; has no Javascript, no cookies, no trackers.

> A sustainable web site means ensuring support for older hardware, slower networks and improving the portability and archivability of the blog’s content.
> > [Homebrewserver.club](https://homebrewserver.club/low-tech-website-howto.html) / [Low-tech Magazine](https://solar.lowtechmagazine.com/2018/09/how-to-build-a-lowtech-website.html)

The best way to meet these requirements and to fully understand how it works is to write it, from scratch. So that's what I did, and that's what you have in front of you right now.

It may not be as efficient or extensible as other static site generators (like [Hugo](https://gohugo.io/), [Jekyll](https://jekyllrb.com/) or [Pelican](https://blog.getpelican.com/)) but everything works pretty well and I am satisfied with the tool I made, it is minimal and matches my values.

## Sources

This documentation tool is open-source by default, as all the things I (try to) do. Sources are available on [Gitlab](https://gitlab.com/antoine.j/antoine.studio).

Feel free to use it, copy it, do whatever you want, but keep in mind that it was written in one specific context and may not work properly in another.


## Core functionalities

In order to be able to develop this low-tech static site generator myself, I have to keep it simple and add functionalities one after the other according to my needs, as show in a [spiral model methodology](https://en.wikipedia.org/wiki/Spiral_model), in order to keep a tool wich works.

Files are organized in different folders depending on the content type (pages/articles/assignments/flux), for clarity. Articles are written in [markdown](https://en.wikipedia.org/wiki/Markdown), to facilitate the writing process. Images are optimized and resized on the fly, to keep the generated website as light as possible. URLs are simple and stay the same even if the project architecture changes, because I might break it more than once.

### Content organization

There are four main types of content: `assignments/` (for our weekly assignments), `posts/` (for additional content that may not be linked to the academy), `pages/` (for more generic purposes), `flux/` (different from the others, it will only be used to display a grid of images).

To add an new article inside the folder related to the desired content type (assignments, posts, pages), make a new directory named as follows: `YYYY-MM-DD-article-title`. The script will store the title to make the URL of the article and the date to keep things organized. Inside this newly created folder: create a `index.md` file wich will contain the text content and add the images (if necessary).

### Website generation

In order to run the script and therefore to generate the html files, go to the project folder (`cd Websites/antoine` in my case), and run `python main.py`.

The script will generate the html files from the markdown files using the html templates written in `templates`. It will also copy the images from the content folder to the `public/medias` folder while compressing them. Refresh your web browser to see the changes.


### Image optimization

Depending on the file format of the images, the script may or may not optimize them. If an image is formatted as `.jpg`, `.jpeg` or `.png`, the script will resize it to acceptable size for the web. This will not modify the `.gif` images as it is a little more complex to manage without losing important attributes such as animation.

### Dependencies

Even though I tried to keep the dependencies as low as possible, I had to use some existing tools to create mine. I will try to narrow the list when I gain more knowledge about programming in Python.

<pre>
import os
import shutil
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from markdown2 import markdown
from PIL import Image
</pre>

### Project structure

<pre>
content/
- assignments/
- - 2020-01-01-assignement-title/
- - - index.md
- flux/
- - image.jpg
- pages/
- - 2020-01-01-page-title/
- - - index.md
- posts/
- - 2020-01-01-post-title/
- - - index.md
public
templates
- article.html
- base.html
- flux.html
- home.html
- index.html
main.py
</pre>

---

# GIT cheatsheet

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

## Useful commands

Start a project from scratch: `git init` and then `git remote add origin {repository-url}`

Pull the last commits from the distant server: `git pull`

Add all the modifications to the stack: `git add .`

Do a commit with a description: `git commit -m "message"`

Push the commit(s) on the distant server: `git push`

Discard the changes on uncommited files: `git checkout .`

Create a new branch: `git branch {new-branch}`

Merge the current branch with another: `git merge {other-branch}`

Delete a local branch: `git branch -d {local-branch}`

Delete a remote branch: `git push origin --delete {remote-branch}`

Change your working branch: `git checkout {branch-name}`

### Visualization

Get the repo's status `git status` or the repo's history: `git log`

Get the list of branches:  `git branch ` or `git branch -v` to get more info

Get the the commit-tree of all branches: `git log --oneline --abbrev-commit --all --graph --decorate --color`

### Configuration

Keep the password in memory for the next 8 hours: `git config --global credential.helper 'cache --timeout 28800'`

Add a shortcut to add and commit at the same time: `git config --global alias.ac '!git add -A && git commit'` and then `git ac -m "message"`

Configure an alias to display the commit-tree:  `git config --global alias.gg 'log --oneline --abbrev-commit --all --graph --decorate --color'` and then use `git gg`

---

# MISC

### Video compression

`ffmpeg -i video.mp4 -b 1000000 compressed-video.mp4` or `ffmpeg -i video.mp4 -b 1000000 -t 10 compressed-video.mp4` where `-t 10` is the duration (10 sec.)
