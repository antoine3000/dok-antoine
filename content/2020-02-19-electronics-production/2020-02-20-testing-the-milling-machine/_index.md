---
title: Testing the compact milling machine
---


The goal of this group assignment is for us to know the potential gaps between our traces, or how thin the traces could be. Since the machines were always occupied and the booking system at Fab Lab Barcelona was not really effective, our class couldn't have a chance to do many group tests. In the end, we were able to finish only 1 group test with the participation of the whole class.

We used the Roland MonoFab SRM-20 machine to mill a test file.

![linetest](linetest.png)

## Detailed specs of the machine:

- Work area: 203 x 152 x 60mm
- Loadable workpiece weight: 2kg
- Operating speed: 6mm/min - 1,800mm/min
- Spindle speed: 3,000 – 7,000rpm
- Input Format : RML-1
- Material: Modeling Wax, Chemical Wood, Foam, Acrylic, PCB


![group-1](group-1.png)
![group-2](group-2.png)

We prepared the `.rml` files using [Fab Modules](http://fabmodules.org/).


1. Select `.png` input format and load the .png file
2. Select `.rml` output format
3. Select the proper process: `PCB traces (1/64)` or `PCB outline (1/32)`. This will define the cut depth (0.1mm for milling traces and 0.6mm for cutting).
4. Select `SRM-20` in the output machine.
5. Modify settings to origin `0,0,0 (x,y,z)`; `zjog = 12` (to make sure the milling bit will be lifted up while moving across the workpiece and avoid damaging both the traces and the fragile bit itself); and home `0,0,12 (x,y,z)`.
6. Select the proper direction. If there are thin traces on the board, we need to select the conventional direction in order to avoid broken traces.
7. Click the `calculate` button to calculate the toolpath and click the `save` button to save the `.rml` file.

![linetest](testline-2.jpg)

![linetest](testline-1.jpg)

We had an issue with the outlines cutting. One side was not cut completely. We managed to generate the file multiple times and did the process again, but we still had the same problem. However, we could tell from the failed test that using the default settings of Fab Modules, the machine is able to mill up to 0.010mm thin trace.

I hope we will find a way to better manage the time we have for the coming weeks. I would like to have more time with the machines, to be able to experiment more an go further than the assignments.
