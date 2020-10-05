---
title: Electronics Design
---


# Components

- 4 solenoids
- 1 air pump
- 1 microchip ATMega16U2

## ATMega16U2

- Same microshop used in the Arduino Uno in order to exchange information via USB
- Has enough pins for my project

## Steps

- Understand the USB part of the Arduino Uno schematics
- Test how the mosfet + solenoid part is acting in term of voltage drop
- Check the footprints of the different elements
  - Are they available?
  - Is it ok to solder them?
  - Aren't the pads to close to each other, or the lines too thin (or thick)?
- Are all the components available at the lab?

## Crystal

Oscar recommended using a resonator instead of the crystal because it is easier to use and solder than the crystals, but I found another piece of advice in the documentation from a former student.

From Andrew Mao's [documentation](http://fab.cba.mit.edu/classes/863.14/people/andrew_mao/week11/):
> In order to use Full-speed (12 Mbit/s) USB, the microcontroller needs to be able to generate a precize 48 MHz clock with a deviation of no more than 0.25%. Since resonators have 0.5% tolerance, This means only quartz crystals can be used, and moreover they need to evenly divide into this frequency in order for a phase-locked loop to generate this clock. For the ATMega16U2, this will require a 8MHz or 16MHz crystal - no substitutes.

But using a crystal induces having more components and thus harder to assemble. According to Oscar, at our level, in the Fab ecosystem, we don't especially need that precision. A resonator is totally fine for what I need.

# Design tips

- Check the correct clearance before tracing the routes
- Apply a common ground at the end of the design
- Global deletation > tracks, as soon as I'm blocked
- Clean tracks to be sure there are no undesired portions of track

# Export Kicad

Oscar's project to export SVG to PNG from Kicad using the Inkscape API.
No holes for now, so I'm using Via's. I've to document that.
The outer zone of the traces file must be filled in black and then inverted when imported into fabmodules.org.
- link to gitlab project
- Command line SVG -> PNG
- What Oscar has been changed, for Python3 compatibility

# Soldering
- I have changed some components when I was doing my shopping list because not all of them were available at the lab. Here is the updated list and what I had planned to use:
- Mini USB is much easier to solder than the micro usb, that why I used it. The only thing with that USB version is that is a bit more complicated to find the right cable.

## Debugging

- When plugged to my computer, I first tried to read my USB ports by typing `$ lsusb` but the new device didn't appear there. Then I checked more deeply with `$ dmesg -w` and saw that I had an over-current condition on the new device's port.

# ISP programming

First of all, I have to program the chip to tell it what will be its behaviour. For that I am going to use a AVRISP mkII programmer.





# Questions

QUESTION: How many pumps and solenoid are really needed?

- In the *Programmable Air* project, they use 2 pumps and 3 valves in order to be able to manipulate entirely an air flow. I would like to reach that precision level but I'm not sure how much is needed

QUESTION: One single board or few modular ones?

- One single board is easier to do because everything is physically connected together and thus we don't have to think about communication between the different parts. On the other hand, a modular approach allows to prototype faster, to make errors and improvements without having to fabricate everything again. I will begin to design and fabricate a single board and then iterate to different modules according to my time management.

# References

- [Arduino Uno Schematics](https://www.arduino.cc/en/uploads/Main/arduino-uno-schematic.pdf)
- [Arduino USB Connection](https://rheingoldheavy.com/arduino-from-scratch-part-7-arduino-usb-connection/)
- [ATmega8U2/16U2/32U2 datasheet](https://www.mouser.es/datasheet/2/268/doc7799-1315152.pdf)
- [AVR USB Devices and Programming](http://fab.cba.mit.edu/classes/863.14/people/andrew_mao/week11/)
- [Oscar's documentation](http://archive.fabacademy.org/2018/labs/barcelona/students/oscar-gonzalezfernandez//2018/04/18/Week-11-Output-Devices.html)
- [ATMega16u2 pinouts](https://microcontrollerslab.com/atmega16-microcontroller-pinout-programming-features-applications/)
