---
title: PlatformIO
---

[PlatformIO](https://platformio.org/) is a cross-platform, cross-architecture and multiple framework tool for embedded programming. It replaces Arduino IDE and offers a lot more subtilities and flexibility to write organized code for micro-controllers.

I use PlatformIO as a replacement for Arduino IDE because it allows me to use the text editor I want (I use [Neovim](https://neovim.io/), an hyperextensible Vim-based text editor) and because it integrates librairies of more than 700 differents boards, including the ones I use. It also has a unified debugger and a static code analyze which seems super useful for large scale projects.

### Initialization

Because PlatformIO is based on Python, the installation is pretty straight-forward using *pip*: `$ pip install -U platformio`

An empty folder to host the project is needed for PlatformIO to set up its environment. Make a new one and go in it `$ mkdir my-project && cd my-project` then type `$ pio init` to initialize this folder with the PlatformIO structure.

> `pio` is the the shortcut for `platformio`, it's the exact same thing but shorter

Then the structure should look like this:

<pre>
platformio.ini
src/
- main.cpp
- main.h
- …
lib/
- input/
- - input.cpp
- - input.h
- - …
- output/
- - output.cpp
- - output.h
- - …
boards/
- board_definition.json
</pre>

Next, search for the depedencies ID you might need, in this case the `Adafruit_CircuitPlayground.h`, by typing `$ pio lib search "header:Adafruit_CircuitPlayground.h"`. The lib ID I need is `602`.

Configure the project for this specific board, by following the datasheet found [here](https://docs.platformio.org/en/latest/boards/atmelsam/adafruit_circuitplayground_m0.html).

These values have to be written in the `platformio.io` file.

<pre>
[env:adafruit_circuitplayground_m0]
platform = atmelsam
board = adafruit_circuitplayground_m0
lib_deps =
  602
</pre>

### Run & upload

Write your program into the `src` folder. The librairies have to be included at the very beginning of your program's files. In this case, the Arduino framework `#include <Arduino.h>` and the Circuit Playground framework `#include <Adafruit_CircuitPlayground.h>`.

Once everything is set up (not that much actually, because PlatformIO does a few thing for us), launch the `$ pio run` command to run and compile the code.

![pio-run](large:pio-run.jpeg)

If it has been verified correctly, send it to your board to make it alive by typing `pio run -t upload`.

![pio-upload](large:pio-upload.jpeg)

I have been using my pomodoro timer every day since I coded it, the Circuit Playground is always by my computer to remind me to take a 5-minutes break every 25 minutes and help me stay focused.