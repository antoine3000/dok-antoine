---
title: My documentation tool
---

My ideal documentation tool is as light as possible and requires very little energy to operate; is perfectly understandable and does the tasks I want it to do - nothing more; evolves with my needs; has no Javascript, no cookies, no trackers.

> A sustainable website means ensuring support for older hardware, slower networks and improving the portability and archivability of the blog’s content.
> > [Homebrewserver.club](https://homebrewserver.club/low-tech-website-howto.html) / [Low-tech Magazine](https://solar.lowtechmagazine.com/2018/09/how-to-build-a-lowtech-website.html)

The best way to meet these requirements and to fully understand how it works is to write it, from scratch. So that's what I did, and that's what you have in front of you right now.

It may not be as efficient or extensible as other static site generators (like [Hugo](https://gohugo.io/), [Jekyll](https://jekyllrb.com/) or [Pelican](https://blog.getpelican.com/)) but everything works pretty well and I am satisfied with the tool I made, it is minimal and matches my values.

## Sources

This documentation tool is open-source by default, as all the things I (try to) do. Sources are available on [Gitlab](https://gitlab.com/antoinestudio/dok-antoine-studio).

Feel free to use it, copy it, do whatever you want, but keep in mind that it was written in one specific context and may not work properly in another.


## Core functionalities

In order to be able to develop this low-tech static site generator myself, I have to keep it simple and add functionalities one after the other according to my needs, as show in a [spiral model methodology](https://en.wikipedia.org/wiki/Spiral_model), in order to keep a tool wich works.

TODO: Update the content, since I refactored everything :-)

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