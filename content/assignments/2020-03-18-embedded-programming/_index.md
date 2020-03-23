---
title: Embedded programming
tags: draft
---

Two weeks ago, I designed a pomodoro timer during the [Electronics design](electronics-design.html) week. It's now time to program it. I'm going to write the piece of code that will light my LEDs as time goes by and find a way to send it to the ATtiny1614 chip. I'm going to focus on the latter: how to send a program (= program) a chip.

Unfortunately, in the meantime, the coronavirus has hit Spain (and the whole world). We are now all in quarantine, with no access to the lab. I'll have to work from home, with the equipment I already have, nothing more. 

For this reason, I'm going to use a [Circuit Playground Express](https://www.adafruit.com/product/3333). This tiny board is already equipped with 10 mini NeoPixels, 1 motion sensor, 1 temperature sensor, 1 sound sensor, 1 mini speaker, 2 push buttons, 1 slide switch, infrared receiver and transmitter and 8 alligator-clip friendly input/output pins. It's a perfect board for quick prototyping and code experiments.

## Pomodoro code

How I want to use my pomodoro:

- Press the left button to start the timer
- If it's running, press the left button to pause the timer
- If it's paused, press the left button to resume the timer
- If it's paused, press the right button to stop the timer
- When it's running, the LEDs light up one by one until the time limit
- When it's running and it's a work period, LEDs are red
- When it's running and it's a break period, LEDs are green
- When it's paused, all the LEDs are light up and blue

The code that does that:

<pre>
bool button_left;
bool button_right;
bool is_active = false;
bool is_paused = false;
int counter = 0;
int steps = 10;
int pomo = 30 * 600;
int pomo_work = pomo / 6 * 5;
int pomo_break = pomo / 6 * 1;

void setup() {
  CircuitPlayground.begin(); 
}

void on_second(int counter) {
  CircuitPlayground.clearPixels();
  if (counter <= pomo_work) {
    // work
    for (int i = 0; i <= steps; i++) {
      if (counter > pomo_work / steps * i) {
        CircuitPlayground.setPixelColor(i, 255,   0,   0);
      }
    }
  } else if (counter > pomo_work && counter <= pomo) {
    // break
    for (int i = 0; i <= steps; i++) {
      if (counter - pomo_work > pomo_break / steps * i) {
        CircuitPlayground.setPixelColor(i, 0,   255,   0);
      }
    }
  }
}

void bip() {
  CircuitPlayground.playTone(200, 10);
}

void loop() {
  button_left = CircuitPlayground.leftButton();
  button_right = CircuitPlayground.rightButton();

  if (counter > pomo) {
    CircuitPlayground.clearPixels();
    counter = 0;
  }

  if (button_left) {
    CircuitPlayground.clearPixels();
    if (!is_active) {
      is_active = true;
      bip();
    } else if (is_active && !is_paused) {
      is_paused = true;
      bip();
    } else if (is_paused) {
      is_paused = false;
      bip();
    }
  }

  if (button_right) {
    if (is_active && is_paused) {
      is_active = false;
      is_paused = false;
      counter = 0;
      CircuitPlayground.clearPixels();
      bip();
    }
  }
 
  if (is_active && !is_paused) {
    counter = counter + 1;
  }
  
  if (is_paused) {
    for (int i = 0; i <= steps; i++) {
      CircuitPlayground.setPixelColor(i, 0,   0,   55);
    }
  }
  
  if (counter % 10 == 0) {
    on_second(counter);
  }

  delay(100);
}
</pre>

## PlatformIO

[PlatformIO](https://platformio.org/) is a cross-platform, cross-architecture and multiple framework tool for embedded programming. It replaces Arduino IDE and offers a lot more subtilities and flexibility to write organized code for micro-controllers.

I use PlatformIO as a replacement for Arduino IDE because it allows me to use the text editor I want (I use [Neovim](https://neovim.io/), an hyperextensible Vim-based text editor) and because it integrates librairies of more than 700 differents boards, including the ones I use. It also has a unified debugger and a static code analyze which seems super useful for large scale projects.

### Initiation

Because PlatformIO is based on Python, the installation is pretty straight-forward using `pip`: `$ pip install -U platformio`

An empty folder to host the project is needed for PlatformIO to set up its environment `$ mkdir my-project && cd my-project`, then type `$ pio init` to  initialize it. 

`pio` is the the shortcut for `platformio`, it's the exact same thing but shorter.

Configure the project for this specific board, as found [here](https://docs.platformio.org/en/latest/boards/atmelsam/adafruit_circuitplayground_m0.html) and search for the library ID `$ pio lib search "header:Adafruit_CircuitPlayground.h"`.

On the `platformio.io` file:
<pre>
[env:adafruit_circuitplayground_m0]
platform = atmelsam
board = adafruit_circuitplayground_m0
lib_deps =
  602
</pre>

The code on the file `src/main.ccp`

Compile: `pio run`

Upload the code on the device `pio run -t upload`





