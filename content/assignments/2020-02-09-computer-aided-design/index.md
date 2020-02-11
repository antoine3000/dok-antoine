---
title: Computer-aided design
---

A tour of open-source softwares for computer-aided design, in order to discover and learn some of the tools that I'll use to design my future projects.

## GIMP

GIMP is a raster graphics editor used for image retouching and editing, converting between different image formats, free-form drawing, …

Installation: `$ sudo apt-get install gimp`

![references](references-making.png)

Even if I only used GIMP to draw a quick moodboard for my project, I directly had a good feeling with it, the software seems robust and well designed. There's a huge online community behind it, which makes finding tips and tricks super easy.

![references](references.png)

### Shortcuts

- Move: `m`
- Scale: `shift + t`
- Crop and resize: `shift + c`
- Rotate: `shift + r`

And many more with a "GIMP shortcuts" [research](https://duckduckgo.com/?q=GIMP+shortcuts&t=canonical&atb=v195-1&ia=cheatsheet&iax=1) in DuckDuckGo.


## Inkscape

Inkscape is a vector graphics editor. Its primary vector graphics format is SVG (Scalable Vector Graphics).

Installation: `$ sudo apt-get install inkscape`

![schema](schema-making.png)

I didn't really like spending time in Inkscape. I had a few bugs, the software crashed several times, the handling of the vectors was not precise. Surely I have to spend more time on it, maybe to tweak it a bit, because the community behind the software seems to agree that it has a great potential. Next time, I'll go for some Python script experimentation, an area where Inkscape seems very interesting.

In the meantime, I have drawn a basic but vector schema of my project.

![schema](schema.png)

### Shortcuts

- Select: `s`; Node: `n`
- Zoom tool: `z`; Zoom in: `+`; Zoom out: `-`
- Transform: `ctrl + shift + M`
- Ellipse/arc tool: `e`
- Rectangle tool: `r`
- Convert selected object(s) to path: `shift + ctrl + C`
- Bezier tool: `b`
- Calligraphy tool: `c`
- Color picker: `d`

And many more with a "Inkscape shortcuts" [research](https://duckduckgo.com/?q=Inkscape+shortcuts&t=canonical&atb=v195-1&ia=cheatsheet&iax=1) in DuckDuckGo.


## FreeCAD

Freecad is general-purpose parametric 3D CAD modeler software made to design real-life objects of any size. It is highly customizable and extensible and it can read and write to many open file formats.

Installation: `$ sudo apt-get install freecad`

Each view has a custom set of tools. So it's important to switch to the appropriated view before doing some manipulations. The more useful ones are Sketcher and Part Design.

## OpenSCAD

OpenSCAD is a software for creating solid 3D CAD (computer-aided design) objects. It is a script-only based modeller that uses its own description language; parts can be previewed, but it cannot be interactively selected or modified by mouse in the 3D view. An OpenSCAD script specifies geometric primitives (such as spheres, boxes, cylinders, etc.) and defines how they are modified and combined (for instance by intersection, difference, envelope combination and Minkowski sums) to render a 3D model.

Installation: `$ sudo apt-get install openscad`

![openscad-box-1](openscad-box-1.png)
![openscad-box-2](openscad-box-2.png)

<pre>
$fn = 40;
length = 50;
width= 40;
height = 20;
radius = 2;
wallTickness = 1.5;

module roundedBox(length, width, height, radius) {
  dRadius = 2*radius;
  minkowski() {
    cube(size = [width-dRadius, length-dRadius, height]);
    cylinder(r = radius, h = 0.01);
  }
}

// box
translate([radius, radius, 0]) {
  difference () {
    roundedBox(length, width, height, radius);
    translate([wallTickness, wallTickness, wallTickness]) {
      roundedBox(length-wallTickness*2, width-wallTickness*2, height, radius);
    }
  }
}

// lid
translate([width*2 + radius, 0, 0]){
  mirror([1,0,0]) {
    translate([radius, radius, 0]) {
      union() {
        roundedBox(length, width, 1, radius);
        difference() {
          translate([wallTickness, wallTickness, 0]) {
            roundedBox(length-wallTickness*2, width-wallTickness*2, 4, radius);
          }
          translate([wallTickness*2, wallTickness*2, 0]) {
            roundedBox(length-wallTickness*4, width-wallTickness*4, 6, radius);
          }
        }
      }
    }
  }
}

</pre>

## Blender

Blender is 3D computer graphics software used for creating animated films, visual effects, 3D printed models, motion graphics, …

Installation: `$ sudo snap install blender --classic`

![setup](setup.png)
![setup2](setup2.png)

Blender is super powerful and can be used in a wide variety of fields. I don't see any real use for me right now, as I mainly focus on exporting models from my computer to the real world, instead of polishing virtual things. However, it will be my weapon of choice for quickly sketching an idea in 3D and animating it if necessary.

### Shortcuts

- Switch between edit and object mode: `tab`
- Switch the preview mode: `z`
- Move: `g`; + the axe if needed `x`, `y`, `z` or multiple ones `xy`
- Select box: `b`; select circle: `c`; select lasso `l`; (un)select all: `a`
- Cut a shape: `ctrl + R`
- In edit mode, switch between the select modes (vertex, edge or face): `1 or 2 or 3`
- Insert faces: `i`