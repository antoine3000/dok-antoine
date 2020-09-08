---
title: 3D scanning
---


There aren't many open source tools available and maintained for 3D scanning, but [Meshroom](https://alicevision.org/#meshroom) is one of them. It is an open source photogrammetry software.

> Photogrammetry is the art, science and technology of obtaining reliable information about physical objects and the environment through the process of recording, measuring and interpreting photographic images and patterns of electromagnetic radiant imagery and other phenomena.
> > [Photogrammetry, Wikipedia](https://en.wikipedia.org/wiki/Photogrammetry)

![scan-success](scan-success.jpeg)

# Requirements

Meshroom needs a [CUDA-Enabled GPU](https://en.wikipedia.org/wiki/CUDA) in order to run properly. My computer doesn't have this type of processor, but I found a solution to get decent results without the full capacity of the software. I will explain it later in the process.


## Installation

1. Download the binary from [Meshroom home page](https://alicevision.org/#meshroom)
2. Unzip it in any folder.
3. Open a terminal and from this folder run `./Meshroom` to launch the GUI. In my case I have to type ` ~/Documents/Apps/Meshroom-2019.2.0/./Meshroom` to launch the app.

# How-to

1. Take pictures around the object you want to scan
2. Import them into Meshroom, in drag and drop in the window.
3. If you have a CUDA-Enabled GPU, simply press the `start` button. If not, you will have to delete 3 nodes: `PrepareDenseScene` `DepthMap` and `DepthMapFilter` and connect the output of `StructureFromMotion` to the input of `Meshing`, and finally press the `start` button.

# Problems I encountered

I had some problems getting decent results with photogrammetry. Almost all of my attempts weren't even close to a recognizable 3D scan of the object I was trying to get the shape from.

![scan-fail](scan-fail-1.jpeg)

These things didn't work because the objects were either too reflective, or too small, or the light was changing from pictures to pictures, or my camera (from my phone) had a too small aperture.

![scan-fail](scan-fail-2.jpeg)
![scan-fail](scan-fail-3.jpeg)
![scan-fail](scan-fail-4.jpeg)

I knew that Meshroom wasn't the problem because I tried with a set of pictures validated by the community, as something that works and that can be used to test the settings of the software.

![scan-monument](scan-monument.jpeg)

Finally, a little desperate, I went to my roof to get some fresh air and I saw this plant pot, surrounded by tiles forming a grid around the object. It looked like a last try before giving up.

<video><source src="scan-success.mp4"></video>

And it more or less worked… I got the shape of the pot, its structure and texture. Maybe I should have taken a lot more pictures of the plant, all its leaves and its little detail to get it rendered in the final scan.

![scan-success](scan-success-2.jpeg)

# My tips for scanning an object with the photogrammetry process

- the bigger the better
- Preferably outside, with natural light
- No blurred area on the pictures, the software needs to understand the background
- A lot of pictures are needed (~70) from every angle
- Matt objects are the easiest (by far!)

# Conclusion

The result is clearly worse than I imagined when thinking about photogrammetry. But it's an exploration, between cutting-edge technology and open source software driven by the community, between a beginner (me) and a very specific technique. I will have to practice taking appropriate photos for photogrammetry if I want to scan something for a real need.
