---
title: Oloid shape
---

I'm exploring different types of shapes that could eventually be interesting regarding my final project. One of these is the oloid.

> An oloid is a three-dimensional curved geometric object that was discovered by Paul Schatz in 1929. It is the convex hull of a skeletal frame made by placing two linked congruent circles in perpendicular planes, so that the center of each circle lies on the edge of the other circle. The distance between the circle centers equals the radius of the circles. One third of each circle's perimeter lies inside the convex hull, so the same shape may be also formed as the convex hull of the two remaining circular arcs each spanning an angle of 4π/3.
>> [Oloid, Wikipedia](https://en.wikipedia.org/wiki/Oloid)

<div class="embed-container">
<iframe src="https://www.youtube-nocookie.com/embed/GM3_JuFgJ2E" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

An oloid is a geometric shape that only has one side. That means that if you make it roll on a flat surface, its entire surface will touch the flat surface at some point.

The oloid shape can only be achieved by using an additive technique, such as 3D
printing, and not a subtractive technique, such as laser cutting or milling,
because the shape itself must be worked in all directions, not just from bottom
to top (or by using another machine, a robot, with more axes, but then the technique begins to be too complex for a small piece like this one).

## Modeling

[OpenSCAD](https://www.openscad.org/), the 3D CAD modeller that we use by writing code (as I said [here](fabac-assignments-computer-aided-design.html)) has a function called `hull()` that displays the [convex hull](https://doc.cgal.org/latest/Convex_hull_2/index.html) of child nodes.

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

Here is the code I wrote to model the oloid. It's simple isn't it?

<video><source src="oloid-openscad.mp4"></video>

## Slicing

The slicing process of the oloid model was very interesting because I had to add supports to keep the shape in place during printing. It helped me understand how supports work and how to generate them in a slicer software, which is actually super easy.

To do so, I used [Ultimaker Cura](https://ultimaker.com/software/ultimaker-cura) and its pre-configured *Support* options. In order to reduce the printing time and because I knew it from my previous test, I increased the overhang angle to 55° (instead of 45°).

Here is the .std file I made for printing: [oloid.stl](files/oloid.stl)

## Printing

Printing this oloid was'nt as easy as the first test I did. My first attempt failed and I had to stop printing. It gave something like this:

![oloid-fail](oloid-fail.jpg)

I had to call one of my instructors, Mikel Llobera Guelbenzu, to find out what had happened. But even with him, we didn't know directly where this failure came from. We had to search together, and it was very beneficial for my learning.

At first we thought it came from the amount of material coming from the extruder, as if there was a knot in the spool of filament. There was one, but after another test, it turned out that this wasn't the main problem.

Finally, Mikel discovered that the bed wasn't flat due to a wrong manipulation on previous prints. We recalibrated it and relaunched the print, and yes: it went well!

<video><source src="oloid-print-1.mp4"></video>

The very end of the printing was a bit problematic too. The supports didn't support the model enough and everything started to move according to the movements of the printer.

At one point it really seemed like the oloid could fall. Fortunately, I was around the printer and I could hold my piece in place using my finger. That is something I will have to consider the next time I have to think about supports.

<video><source src="oloid-print-2.mp4"></video>

## Result

The end result is quite good, even if I could have increased the quality if I had had more printing time. But let's say it's clearly sufficient for rapid prototyping.

![oloid-result](oloid-result-1.jpg)

Look at this geometric beauty.

<video><source src="oloid-roll.mp4"></video>

