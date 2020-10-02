---
title: Fab stool & bench
---

I wanted to have a stool and bench for my flat, so I designed and fabricated them using the large CNC at Fab Lab Barcelona.

I designed one element, the stool, with parametric values and then produced the other element, the bench, automatically. This process can be useful for everyone, to adapt the furnitures (or anything else) to their needs and the context in which it will be used.

# Design

I first designed this project on paper and then in [Freecad](https://www.freecadweb.org/), my favorite open-source software for 3D modeling.

The stool/bench consists of a seat, two legs and a stretcher. The bench is simply the long version of the stool.

![](stool-view-1.png)
![front view](stool-view-4.png)
![top view](stool-view-5.png)

## Parametric values

I used parametric values in order to easily modify values such as the lengths of the seat, the height of the legs, the thickness of the material, the endmill diameter I will use, the length of the slots, etc.

![](parametric-values.png)

Once the document is well organised and the values in the part design workbench call up values from the datasheet, changing the values automatically changes the rest. This allows me to design without knowing everything in advance, such as the diameter of the milling cutter that will be used to mill the project, and above all it allows the design to be adapted quickly and almost frictionlessly to new constraints.

## Be ready for fabrication

### Tolerance

It is strongly recommended to take a tolerance value into account when working with a CNC machine. This is because the machine will not produce a perfect result and if the cuts are too tight, there is a good chance that it will be almost impossible to put the project together.

![Tolerance detail](tolerance.png)

In this case I used a tolerance value of `0.2 mm`. This means that there is an extra `0.1 mm` on each side of the cut to make sure that the parts fit together.

### Dogbones

Right angles are not accessible by the endmills, which will produce an undesirable result.

To avoid this, it is common practice to create dog bone shapes by adding holes the size of the endmill in the right angles. The space left by the cut will then correspond to the piece that is supposed to fit into it.

![](dogbones1.png)
![](dogbones2.png)

### Export

When the different parts are well designed, take into account the tolerance of the CNC and have dogbones shapes to ensure that the actual measurements will be as expected, export all parts in a technical drawing sheet at the correct scale (1:1). This sheet should be exported as a `.dxf` file and then imported into RhinoCAM.

![](techdraw.png)

# Toolpaths

# Fabrication

# Conclusion
