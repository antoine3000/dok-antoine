---
title: How to read a datasheet
---

Reading a datasheet isn't the easiest thing to do. It is full of technical details that often interfere with the actual data one can look after.

I'll now take a tour of the things that seem important to me when reading a datasheet. And for that, we'll have a look at the [datasheet of the ATTiny1614](http://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny1614-16-17-DataSheet-DS40002204A.pdf) from Microship.

To easily navigation into a large PDF document, use the `ctrl + f` to open a search box and type the term you're looking for.

## Configuration summary

The *configuration summary* is the section where one can have a quick look at what the chip can or cannot do. How many pins does the chip have, what its memory size, how many inputs/outputs or AC pins are free to use. It may seem obvious but having a look at the summary before digging deeper in the content will save you time.

## Pinout

Then comes the pinout. This section is, for me, the most important. It will tell you how you will be able to interact with you microchip. The major part of finding *the* appropriate chip is the understand if it offers you the connections you need.

How many digital pins do you need in your project? What is their reference? Offer they PWM? etc. These a crucial questions when designing an electronic project around a microchip.

## Memories

The *Memories* section will indicate how much memory the microchip has. This is good to know when choosing a chip to be sure it will support your future program. Do you have to deal with data collection? How complex is your code logic? etc.

## Power consumption

The *Power consumption* section indicates the voltage the chip needs to run and therefore what voltage it can serve. Some chip work with 3.3V or 5V, some only with 3.3V, others with 5V. How many amps will you need to bring to the chip could also be an important factor.


## Package drawings

Microchip can come in different packages. Choosing the wrong one when designing a PCB can lead to unusable work. Double compare the microchip you have and the package drawing you use in your circuit board design software to be sure you have a good one.