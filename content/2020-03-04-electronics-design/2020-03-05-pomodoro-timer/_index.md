---
title: Pomodoro timer
featured: True
featured_image: pomo.jpeg
last_update: 2020-09-15
---

I use a pomodoro timer daily to help me manage my time and effort in the tasks I want to accomplish. For now, I'm using [Pydoro](https://github.com/JaDogg/pydoro), an open source pomodoro terminal timer written in Python but I would like to build mine and have it physically next to my laptop.

> The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. The technique uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks. Each interval is known as a pomodoro, from the Italian word for 'tomato', after the tomato-shaped kitchen timer that Cirillo used as a university student.
> > [Pomodoro Technique, Wikipedia](https://en.wikipedia.org/wiki/Pomodoro_Technique)

![pomo-illu](pomo-illu.png)

## Components

The main component I'm using is the microcontroller [ATtiny1614](https://www.microchip.com/wwwproducts/en/ATTINY1614). It will allow me to program my inputs and outputs needed to run my project.

As outputs, I have 4 LEDs that are used to visualize the time passing by and the interactions with the pomodoro timer.
As inputs, I have to 2 switches (buttons) that allow me to start/pause/resume/reset the timer.

I also need 6 resistor (one for each of the inputs/outputs), a capacitor, a FTDI header (to be able to communicate with the boards), a UPDI header (to program the board).


## Design

I'm using [KiCAD](https://kicad-pcb.org/), a cross platform and [open-source](https://gitlab.com/kicad) software, for designing electronics. The process is divided into two main steps: schematics design and PCB design.

Before making the schematics, I had to import symbols and footprints according to the components which I wanted to use (and which I had at my disposal in the laboratory).

For the symbols, go to `Preferences > Manage Symbol Librairies` to add [this](https://github.com/KiCad/kicad-symbols) and [this](https://kicad.github.io/symbols/MCU_Microchip_ATtiny). For the footprints, go to `Preferences > Manage Footprints Librairies` to add [this](https://github.com/KiCad/kicad-footprints).

In the context of Fab Labs, [this library](http://academany.fabcloud.io/fabacademy/2020/labs/barcelona/site/local/#material/extras/week06/assets/kicad_libraries.zip) is very useful because it contains all the components we have at our disposition.

### Schematics design

To design the schematic of the board, one should first import the right symbols. In my case, the components I listed above on this page. to do so, select the `Place symbol` tool, click on the page and choose the symbol you want.

- `R` to rotate the component
- `C` to copy it
- `M` to move it
- `Delete` to delete it
- `W` to draw a wire

Then, you will have to connect the elements together. To do so, a good practice is to divide the circuit into smaller and more understandable circuits. In my case, I design the switches, LED's, capacitor, ATtiny1614, FTDI and UPDI apart. It's then easier to get a full understanding of the circuit and it's also easier to manipulate.

![schematics-design](schematics-design.jpeg)

Don't be confused, the real design mission is for the next step, now is just about connecting parts together, and about being understandable for the community if you plan to share your design or simply for your future self.

It's always important to check the datasheet of the components you're using. In this case, [the datasheet of the ATtiny1614](http://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny1614-DataSheet-DS40001995B.pdf) helped me to verify the differents connections from the chip to the components.


### PCB design

Now is the "tricky" part: finding the best paths, the most compact as possible while respecting the idea I had in mind. For instance, because I'm building a pomodoro timer, I want my 4 leds to be next to each other, and so has to be the resistors as well. It's about designing with constraints, something I really like, even if it took me hours to find a possible way to design my circuit.

![pcb-design](pcb-design.jpeg)


#### Things I learned while designing it

- always start by connecting the chip to its direct components
- rotate and rotate again the components until it makes sense
- the ground closes the circuit, so it's easier to end with it
- just because you seem to be close to the solution doesn't mean you are really close to the solution. You don't know that until the end, when you connect the last components together
- what is possible in a CAD software may not be easy to do in real life
- optimize your paths and think about how you will solder the  components


### Preparing the files

Once your design is ready (that means that all your components are linked together), you can export your files and prepare them to be sent to the mini milling machine. I used [Inkscape](https://inkscape.org/), [gimp](https://www.gimp.org/) and [fab modules](http://fabmodules.org/) to do so.

![pomo-traces](pomo-traces.png)
![pomo-cut](pomo-cut.png)

![fab-modules](fab-modules.jpeg)

I used Fab Modules to generate the files needed by the mini milling machine using the same settings I set during the [Electronics production](fabac-assignments-electronics-production.html) week.

## Milling and soldering

The machine I used to mill my board is the Roland MonoFab SRM-20, this machine seems very reliable, I had no problem while using it.

![pomo-milling](pomo-milling.jpeg)

![pomo-board](pomo-board.jpeg)

Soldering was fun to do, I really like doing it, even if I started with a big mistake: I was a little in a hurry, the lab was closing and I wanted my job to be done, my focus wasn't really there and I soldered the ATtiny1614 in the wrong direction. I know this little dot on the chip, which gives you the direction of the chip but I wasn't paying attention to it. What should have taken a few minutes took me over an hour: desolder a 14-legs chip isn't that easy!

I managed to unsolder the ATTiny chip with a heatgun: hold the chip in tweezers and heat the solder around the chip with a heatgun, and finally let the gravity do its job. The chip will stay in the tweezers while the board drops onto the worktable.

The heatgun can reach a high temperature and therefore burn the board, so care must be take not to heat the board for too long. Burning your precious is the last thing you want to do right now.

![pomo](pomo.jpeg)

## Testing

In order to test the board, you will need a UPDI for the communication between the board and another computer and a FTDI to program the board itself. Luckily, these are the two I already made.

The power comes from the FTDI and the data from the UPDI.


![pomo-plugged](pomo-plugged.jpeg)
![With FTDI and UPDI connection](pomo-connect.jpg)

First, check if your computer recognizes the board correctly by typing `dmesg -w` in a terminal and see if a new device is detected when you un/plug the board. Save the ID of the board for later.

A simple blink program using the Arduino IDE is the easiest way to check if the communication is possible — and therefore if the board has been done right. Here is the one I used:

<pre>
void setup() {
  pinMode(PA1, OUTPUT);
}

void loop() {
  digitalWrite(PA1, HIGH);
  delay(1000);
  digitalWrite(PA1, LOW);
  delay(1000);
}
</pre>

To make it work, I needed the [megaTinyCore](https://github.com/SpenceKonde/megaTinyCore) in order to *talk* with the ATtiny1614. Find it via the Arduino IDE menu `Tools >   Boards > Boards manager`.

I used [pyupdi](https://github.com/mraardvark/pyupdi) (a Python UPDI driver for programming the "new" tinyAVR and megaAVR devices) to send the code to the chip.

To do so, I had to find the temporary file which is generated by Arduino IDE each time the code is compiled (look at the console and spot the .hex file) and send it via this command to the board.

`pyupdi.py -d tiny1614 -c /dev/ttyUSB0 -b 9600 -f /tmp/arduino_build_342195/Blink.ino.hex -v`

Where `/dev/ttyUSB0` corresponds to the value I got when I did `dmesg -w` earlier and `arduino_build_342195/Blink.ino.hex` corresponds to the temp file I wan to send.

And that's it.

<video><source src="pomo-test.mp4"></video>

## Programming

I will program this board to make it be a pomodoro timer in two weeks, during the *Embedded programming* assignement.

## Files

- Kicad project: [pomodoro-final.zip](file:pomodoro-final.zip)
- Cut PNG file: [pomo-cut.png](file:pomo-cut.png)
- Cut RML file: [pomo-cut.rml](file:pomo-cut.rml)
- Cut XCF file: [pomo-cut.xcf](file:pomo-cut.xcf)
- Traces PNG file: [pomo-traces.png](file:pomo-traces.png)
- Traces RML file: [pomo-traces.rml](file:pomo-traces.rml)
