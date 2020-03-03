---
title: 3D scanning and printing
tags: draft
---

3D printing is not as simple as pressing the *print* button and waiting for the model to be printed. It is crucial to know how to prepare a 3D model, how the printer works and what are its limits, and how to balance printing time with print quality.

For this week, I'll discover a whole new world, that of 3D printing. I'm going to test a printer, scan and print something.

# Printing a 3D test file

For this week's group assignement, I teamed up with [Tue](https://fabacademy.org/2020/labs/barcelona/students/tue-ngo/) and [David](https://fabacademy.org/2020/labs/barcelona/students/david-prieto/). We picked a [test file](https://www.thingiverse.com/thing:1363023) from Thingiverse in order to test different features of one of the 3D printers we have in Fab Lab Barcelona, the [Creality3D CR-10 S5 3D](https://www.creality3d.shop/products/creality-cr-10s-s5-3d-printer-diy-kit-large-printing-size-500x500x500mm).

![test file](testfilecad.jpeg)

This file allows us to test these features: Z-height check, warp check, spike, hole in wall, raft test, overhang Steps 50° - 70°, 2 different extrusion widths: 0.48mm & 0.4mm.

## Slicing

To be able to print a 3D model, we have to send instructions to the printer, wich are written in [g-code](https://en.wikipedia.org/wiki/G-code) and tells the motors where to move.
To prepare the g-code, we have to *slice* our 3D model (.STL), to simulate and anticipate how the model will be printed, according to the printer settings and gravity law.

![cura lab](cura-lab.JPG)

At Fab Lab Barcelona, a computer with [Ultimaker Cura](https://ultimaker.com/software/ultimaker-cura) is attached to the machines, with all the presets of the differents printers saved in it. It's therefore easier to directly use it in order to slice our model instead of searching the presets and install them on our personal laptop.

### Specific settings that we'd to specify

- layer height: `0.25mm`
- Wall thickness: `0.8mm` (= 2 lines)
- Infill: `10%`
- Print speed: `60mm/s` (= maximum for this printer)

## Printing

The filament we use is a `PLA 1.75mm`. It's a plant-based material made from starches like soybeans or corn. It needs to be heated at 190-200C° to be used.

![testfileprint](testfileprint.JPG)

The printing was done in ~90 minutes without any troubles.

<video><source src="print-test.mp4"></video>

![testprint](testprint.JPG)
![testdetail](testdetail.JPG)

## Results

As we can see in the images above, the definition of the print is quite good, the details are respected and the print angles can be large (in fact more than 45°). Even the small bridges without support were printed correctly. I am very satisfied with this test and the new possibilities that it lets us see.


---

# Print something - An oloid

I'm exploring different types of shapes that could eventually be interesting regarding my final project. One of these is the oloid.

> An oloid is a three-dimensional curved geometric object that was discovered by Paul Schatz in 1929. It is the convex hull of a skeletal frame made by placing two linked congruent circles in perpendicular planes, so that the center of each circle lies on the edge of the other circle. The distance between the circle centers equals the radius of the circles. One third of each circle's perimeter lies inside the convex hull, so the same shape may be also formed as the convex hull of the two remaining circular arcs each spanning an angle of 4π/3.
>> [Oloid, Wikipedia](https://en.wikipedia.org/wiki/Oloid)

<div class="embed-container">
<iframe src="https://www.youtube-nocookie.com/embed/GM3_JuFgJ2E" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

An oloid is a geometric shape that only has one side. That means that if you make it roll on a flat surface, its entire surface will touch the flat surface at some point.

## Modeling

[OpenSCAD](https://www.openscad.org/), the 3D CAD modeller that we use by writing code (as I said [here](computer-aided-design.html)) has a function called `hull()` that displays the [convex hull](https://doc.cgal.org/latest/Convex_hull_2/index.html) of child nodes.

This is why I to use OpenSCAD to model this particular shape instead of another more conventional tool like FreeCAD.

<pre>
$fn = 180; // resolution
radius = 20;

hull() {
  cylinder(r=radius, h=0.1, center=true);	
  rotate(a=90, v=[1,0,0]) {
    translate([radius,0,0]) {
      cylinder(r=radius, h=0.1, center=true);
    }
  }
}
</pre>

<video><source src="oloid-openscad.mp4"></video>

## Slicing

The slicing process of the oloid model was very interesting because I had to add supports to keep the shape in place during printing. It helped me understand how supports work and how to generate them in a slicer software, which is actually super easy.

To do so, I used [Ultimaker Cura](https://ultimaker.com/software/ultimaker-cura) and its pre-configured *Support* options. In order to reduce the printing time and because I knew it from my previous test, I increased the overhang angle to 55° instead of 45°.

## Printing

Printing this oloid wasn't as easy as the first test I did. My first attempt gave something like this:

![oloid-fail](oloid-fail.jpg)

I had to call one of my instructors, Mikel Llobera Guelbenzu, to find out what had happened. But even with him, we didn't know directly where this failure came from. We had to search together, and it was very beneficial for my learning.

At first we thought it came from the amount of material coming from the extruder, as if there was a knot in the spool of filament. There was one, but after another test, it turned out that this wasn't the main problem.

Finally, Mikel discovered that the bed wasn't flat due to a wrong manipulation on previous prints. We recalibrated it and relaunched the print, and yes: it went well!

<video><source src="oloid-print-1.mp4"></video>

The very end of the printing was a bit problematic too. The supports didn't support the model enough and everything started to move according to the movements of the printer . It wasn't that problematic at first, but at one point it really seemed like the oloid could fall. Fortunately, I was around the printer and I could hold my piece in place using my finger. That is something I'll have to consider the next time I have to think about supports.

<video><source src="oloid-print-2.mp4"></video>

## Result

The end result is quite good, even if I could have increased the quality if I had had more printing time. But let's say it's clearly sufficient for rapid prototyping.

![oloid-result](oloid-result-1.jpg)

Look at this geometric beauty.

<video><source src="oloid-roll.mp4"></video>

--- 


# 3D Scan

[Meshroom](https://alicevision.org/#meshroom) is an open-source photogrammetry software.

> Photogrammetry is the art, science and technology of obtaining reliable information about physical objects and the environment through the process of recording, measuring and interpreting photographic images and patterns of electromagnetic radiant imagery and other phenomena.
> > [Photogrammetry, Wikipedia](https://en.wikipedia.org/wiki/Photogrammetry)

### Installation

1. Download the binary from Meshroom home page
2. Unzip it in any folder.
3. Open a terminal and from this folder run `./Meshroom` to launch the GUI.

### How-to

1. Take pictures around the object you want to scan
2. Import them into Meshroom
