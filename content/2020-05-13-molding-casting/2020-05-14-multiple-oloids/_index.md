---
title: Multiple oloids
last_update: 2020-10-04
---

![](oloid-model.png)

Remember the oloid I printed during the [3D printing](3D-scanning-printing-oloid-shape.html) week?
For this *Molding & Casting* week, I'm going to mold an oloid and to cast it in the variety of materials that we have here, in Fab Lab Barcelona.

# Mold design

The molding and casting workflow consists of:

1. Milling a positive version of the desired object into a block of wax
2. Filling it with silicon to get a negative (and flexible) mold
3. Filling the previously made mold with another type of silicon or resin to get the final (and positive) object.

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

Now that the files are ready, let's play with this reproduction technique. The first step will be to mill the negative mold, then mold the positive mold from it, to finally be able to cast the oloid shape I designed in various materials.

## Milling the negative mold

The negative mold is made out of a block of wax. The wax is soft enough to allow a high accurancy and can easily be re-used multiple times. 

![File-A-Wax block](wax-block.jpg)

For this project, I was lucky to start with a brand new block of wax. If that wasn't the case, I would have had to mill the first layer to make sure the block was perfectly flat and the right size.

I used the [MonoFab SRM-20](https://www.rolanddga.com/products/3d/srm-20-small-milling-machine), the same one we use to mill PCB's, to mill the wax. I like how this machine is accurate and reliable in different tasks.

![Setting the XYZ positions](milling-z.jpg)

To set properly the X and Y, the center of the endmill has to be exactly on top of the bottom left corner of the block of wax.

<video><source src="milling.mp4"></video>

Milling a block of wax produces a messy environment full of wax flakes. But don't worry, we recover everything at the end of the process to melt it down and transform it into another block of wax. Almost no waste!

![](wax-wax.jpg)

The final result is quite impressive. The lines we can see have been produced by the rough cut, but then the finish cut smoothes everything super well.

The end result is quite impressive. The lines we can see were produced by the rough cut, but the final cut smoothes everything superbly.

![](large:wax-milled.jpg)

## Molding the positive mold

![](small:wax-release-1.jpg)
![](small:wax-release-2.jpg)
![](wax-release.jpg)

![](easyplat.jpg)

<video><source src="mix-well.mp4"></video>
<video><source src="pouring.mp4"></video>

![](silicon-result-1.jpg)
![](silicon-result-2.jpg)
![](silicon-result-3.jpg)
![](large:silicon-result-4.jpg)
![](large:silicon-result-5.jpg)


# (re)Production

![](mold-press.jpg)
![](setup.jpg)

## Platinum silicone

<video><source src="pouring-first-material.mp4"></video>

![](first-result-1.jpg)
![](first-result-2.jpg)
![](first-result-3.jpg)

## Pine resin

![](pine-resin-1.jpg)
![](pine-resin-2.jpg)
![](pine-resin-3.jpg)
![](pine-resin-4.jpg)
![](pine-resin-5.jpg)
![](pine-resin-6.jpg)
![](pine-resin-7.jpg)
![](pine-resin-8.jpg)

## Urethane resin

![](plastic-resin-1.jpg)
![](plastic-resin-2.jpg)
![](plastic-resin-3.jpg)
![](plastic-resin-4.jpg)
![](plastic-resin-5.jpg)
![](plastic-resin-6.jpg)
![](plastic-resin-7.jpg)







# Final results

![](final-result-2.jpg)
![](final-result-3.jpg)
![](final-result-4.jpg)

<video><source src="final-result.mp4"></video>











# Files

- 3D model > [oloid-model-mold.FCStd](file:oloid-model-mold.FCStd)
- Fabrication file, rought cut > [oloid-wax-rough-3-175-flat.rml](file:oloid-wax-rough-3-175-flat.rml)
- Fabrication file, final cut [oloid-wax-final-3-175-ball.rml](file:oloid-wax-final-3-175-ball.rml)



