---
title: Computer-controlled cutting
---

## Basics of lasercutting
The lasercutter is a excellent machine: it gives quick results, it's easy to learn, it works with different types of materials (wood, acrylic, cardboard, etc.), the cutting looks good.

### Security
Because the lasercutter is fun and easy to use, it's also easy to forget that it can be dangerous. Here are some basic rules that accompany the use of the machine:

- Do not leave the machine unattended
- Cut only materials that you know are safe (no chromium, no carbon, no PVC, no PVP)
- Always use the filter and wait for the smoke to disappear before opening the cover
- Make sure you know what to do in case of fire

### Focus
The focus is calculated based on the distance between the material and the laser. It must be adjusted before any cutting, depending on the thickness of the material.

### Speed & power 
Speed and power are the two parameters that we have to adjust according to the desired results. The speed is defined in millimeters per second (0-400) and the power is defined in (a relative) percentage (0-100%). To cut something big, you will need to set a high power and a low speed, so that the laser stays longer at the same points and burns the material more. On the other hand, to slightly engrave, set a high speed and a low power, so that the laser does not have enough time to burn the material.

### Kerf
The laser burns away a portion of material when it cuts through. This is known as the laser kerf and ranges from 0.08mm – 1mm depending on the material properties and thickness. It is super important the know the value of the kerf and to integrate it into the design, if we want to cut things perfectly.


## Get to know the machine

### Calculate the kerf

| Material | Intended | Actual | Difference | Kerf (difference/10) | Offset (kerf/2) |
| --- | --- | --- | --- | --- | --- |
| Cardboard 2mm | 100mm | 95mm | 5mm | 0.5mm | 0.25mm |
| Cardboard 4mm | 100mm | 95mm | 5mm | 0.5mm | 0.25mm |
| Cardboard 6mm | 100mm | 95mm | 5mm | 0.5mm | 0.25mm |

---

# A parametric construction kit

Design, lasercut, and document a parametric construction kit, accounting for the lasercutter kerf, which can be assembled in multiple ways.
