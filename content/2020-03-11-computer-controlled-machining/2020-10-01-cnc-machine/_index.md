---
title: CNC machine
--- 

# Introduction

For this week's assignement we have to characterise the CNC machine. This was done when we had the opportunity to return to the lab after the lockdown situation due to the COVID-19 pandemic.

I had a chance to team up with my classmates [Tue Ngo](http://academany.fabcloud.io/fabacademy/2020/labs/barcelona/students/tue-ngo/), [Arman Naraji](https://fabacademy.org/2020/labs/barcelona/students/arman-najari/), [David Prieto](https://fabacademy.org/2020/labs/barcelona/students/david-prieto/) and [Lynn Dika](https://fabacademy.org/2020/labs/barcelona/students/lynn-dika/) for this group assignment.

On this page, I will highlight the key point of the process. Tue has detailed everything on her page, please feel free to go there for the full documentation.

[Full documentation](button:http://academany.fabcloud.io/fabacademy/2020/labs/barcelona/students/tue-ngo/assignments/week-07-computer-controlled-machining.html)

---

# Personal notes

## Software

Unfortunately, Fab Lab Barcelona uses [RhinoCAM](https://mecsoft.com/rhinocam/) (~1500€), a plug-in for [Rhino3D](https://www.rhino3d.com/) (995€), to perform this task. Paying ~2495€ for a propriatary software that students can't get unless they crack it is a very bad idea for me, especially in the context of Fab Labs. But Fab Lab Barcelona made this choice and configured RhinoCAM with all the necessary parameters to work with the [RaptorX-SL](https://www.cnc-step.com/milling-machine/), the big CNC.

I hope that open-source solutions will evolve robustly in the near future to counter this proprietary monopoly.

![RhinoCAM](large:test-cam-1.png)
![RhinoCAM](large:test-cam-2.png)

## G-code

To mill something with the CNC, we first have to screw a wooden board onto the machine bed to make sure it won't move during the process. But as we don't want to mill on a screw, which can cause a fire, we first have to place the screws on our drawing and generate a G-code (*Machining Operation > Engraving*) just for that. Then another g-code (*Machining Operation > 2-axis Profiling*) has to be generated with our design only.

## What we need to know

- the **thickness of the material** we are going to mill, and **its chip load** value (the thickness of material removed by each cutting edge during a cut)
- the **diameter of the endmill** and the **number of flutes** it has (the sharp slots that corkscrew upwards along the length of a milling bit)
- the spindle speed at which the spindle of the machine rotates


## Tool's feed and speed

`Feed rate = N x CPT x RPM` is the formula used to calculate the tool's feed and speed. Where **feed rate** is the speed at which the cutter engages the part,  **N** as the number of flutes, **CPT** as the chip load and **RPM** as the spindle speed at which the spindle of the machine rotates.

## Machining with the RaptorX-SL

We used the [Raptor X-SL 3200/S20](https://www.cnc-step.com/raptorx-sl-xl-gantry-cnc-router-machine-3200s20-with-3200-x-2010mm-traverse-path/) machine and its software [KinetiC-NC](https://www.cnc-step.com/cnc-software/kinetic-nc-cnc-control-software/) to do the test. The detailed specs of the machine:

- Working area: `3,200 x 2,010 x 300mm`
- Clamping area: `X -3,500mm x Y -2,200mm`
- Positioning speed X+Y/Z: `maximum 40,000mm/min`
- Working speed: `maximum 20,000mm/min`
- Step width X: `0.0213mm`
- Step width Y+Z: `0.0113mm`

![](large:test-1.jpg)
![](large:test-2.jpg)
![](large:test-3.jpg)
![](large:test-4.jpg)

# Conclusion

The Raptor CNC machine is impressive in power and size. It can carry out large projects, but it can also be dangerous, which is why it is important to observe the safety rules:

- Wear safety glasses
- know where the emergency button is located
- switch on the ventilation

It is also very important to know and understand all the data we have to deal with. Running the machine too fast can damage the material and the machine itself, too slow can produce too much heat and start a fire, etc. With this giant machine you don't play with rules and mathematics.

Making the toolpath (g-code) is the big part of working with the CNC, and because of the Rhino software that I don't have, because I use Linux and open source software, I'm not very confident in the process. I'm looking forward to doing my personal project to have more time to absorb the knowledge we need to know. See you at the next step!


