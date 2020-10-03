---
title: Other tools
last_update: 2020-10-03
---

## Video compression

`ffmpeg -i video.mp4 -b 1000000 compressed-video.mp4` or `ffmpeg -i video.mp4 -b 1000000 -t 10 compressed-video.mp4` where `-t 10` is the duration (10 sec.)

## Imagemagick recipes

[Imagemagick](https://imagemagick.org/index.php) can resize, flip, mirror, rotate, distort, shear and transform images, adjust image colors, apply various special effects, or draw text, lines, polygons, ellipses and Bézier curves. Via the terminal.

- Rotate `mogrify -rotate 180 *.jpg`
