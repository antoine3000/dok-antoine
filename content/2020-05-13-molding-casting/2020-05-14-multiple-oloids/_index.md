---
title: Multiple oloids
---

![](oloid-model.png)

Remember the oloid I printed during the [3D printing](3D-scanning-printing-oloid-shape.html) week?
For this *Molding & Casting* week, I'm going to mold an oloid and to cast it in the variety of materials that we have here, in Fab Lab Barcelona.

# Mold design

The molding and casting workflow consists of:

1. Milling a positive version of the desired object into a block of wax
2. Filling it with silicon to get a negative (and flexible) mold
3. Filling the previously made mold with another type of silicon of resin to get the final (and positive) object.

I'll use the oloid model I already did as a starting point.

![](mold-freecad.png)

The main idea is to model the wax block according to its actual dimensions `88mm * 36mm * 146mm`, make a pocket to host half of the desired object, add guides and pouring holes.

Then, because my oloid is symmetrical and because it fits into the wax block, I could duplicate what I did to make both sides of the mold at the same time. If the wax block had been smaller, I would have milled once and made two molds with the same wax block.

## Guides

I added guides to the model so that I could easily close the two sides together, making sure they are in the perfect position.

![](mold-detail-1.png)

## Pouring hole and air flow

I had to add two holes to the model, one to pour the material into the mold and the second to allow the air to escape. Without the second, it would be almost impossible to pour the material into the enclosed space.

![](mold-detail-2.png)

## Resources

- [Tutorial](https://www.youtube.com/watch?v=5lwENZeNiNg) on how to modify a `.stl` model in Freecad
- [Tue's documention](http://academany.fabcloud.io/fabacademy/2020/labs/barcelona/students/tue-ngo/assignments/week-15-molding-and-casting.html)

# Generate toolpaths

I'll use the milling machine *Roland monoFab SRM-20* to mill my block of wax.

I generated the `.rml` files using [Fab Modules](http://fabmodules.org/). We have to produce two files, one for the rough cut and the other for the finish cut.

## Global

These are the settings I used to generate the toolpaths.

- input format: `.stl`
- modifiy the units/in to `25.4` and dpi to `500` (to use millimeters instead of inches)
- calculate the height map
- output form: `.rml`
- select the proper process: `wax rough cut` (1/8) or `wax finish cut` (1/8)
- machine: `SRM-20`
- origin: `0,0,0` (x,y,z)
- zjog: `12 mm`
- home: `0,0,12` (x,y,z)
- choose the end mill type, tool diameter, offset overlap, and tool overlap settings for each process (rough of finish cut)
- Calculate
- Save

## Wax rough cut

- tool diameter: `3.175 mm`
- type: `flat end-mill`
- tool overlap: `50%`

![Screenshot of the generated paths in Fab Modules, rough cut](fabmodules-rough.png)

## Wax finish cut

- tool diameter: `3.175 mm`
- type: `ball end-mill`
- tool overlap: `90%`

![Screenshot of the generated paths in Fab Modules, final cut](fabmodules-finish.png)

# Fabrication

![](wax-block.jpg)
![](milling-z.jpg)

<video><source src="milling.mp4"></video>

![](wax-wax.jpg)

![](final-result-2.jpg)
![](final-result-3.jpg)
![](final-result-4.jpg)

<video><source src="final-result.mp4"></video>

![](first-result-1.jpg)
![](first-result-2.jpg)
![](first-result-3.jpg)

<video><source src="mix-well.mp4"></video>

![](mold-detail-1.jpg)
![](mold-detail-2.jpg)
![](mold-press.jpg)
![](pine-resin-1.jpg)
![](pine-resin-2.jpg)
![](pine-resin-3.jpg)
![](pine-resin-4.jpg)
![](pine-resin-5.jpg)
![](pine-resin-6.jpg)
![](pine-resin-7.jpg)
![](pine-resin-8.jpg)
![](plastic-resin-1.jpg)
![](plastic-resin-2.jpg)
![](plastic-resin-3.jpg)



# Files

- 3D model > [oloid-model-mold.FCStd](file:oloid-model-mold.FCStd)
- Fabrication file, rought cut > [oloid-wax-rough-3-175-flat.rml](file:oloid-wax-rough-3-175-flat.rml)
- Fabrication file, final cut [oloid-wax-final-3-175-ball.rml](file:oloid-wax-final-3-175-ball.rml)



