---
title: Interface application programming
---

This week is devoted to programming interfaces and applications, a subject that I really like. I would not say that I am a good programmer, I have little experience. But it's something I love to do: solve logic problems, create software that produces the result I want (or the result I didn't expect, because I also find unexpected things beautiful).

TODO: hero video & short description of the final result

---

## My coding journey

### Processing (Java / Javascript)

In art school, I had two years of digital art workshops. The main tool we used in this class was [Processing](https://processing.org/). And it was so refreshing. Being able to produce an artistic installation with algorithms was something I was looking for. But it was also the rise of another movement: Internet culture. This quickly made me drop Processing for its javascript version, [p5js](https://p5js.org/) and html/css, in order to create websites. It was not really good, Processing (p5js) is not so exciting when it is stuck in a browser. But the mix of graphic design and coding was definitely the right direction for me. I had the insight I needed with Processing and the motivation to continue creating websites, and then to found my web studio.

### Javascript

In my web studio, I made websites with html/css and Javascript. I used to mainly use [vanilla Javascript](https://en.wikipedia.org/wiki/JavaScript) and [Vue.js](https://vuejs.org/) to build reactives web interfaces. I always found it tricky and not really intuitive. Even if Javascript is powerful and can do many things, I find that it is also a kind of poison for the web: websites get heavier, they track you more and more, and they need an updated browser to be viewed. It is not a language in which I would like to invest myself more. I would even prefer the Internet without it, without advertising and tracking, filled with lighter websites that run on older browsers.

### Python

Then I discovered Python, a language that also has many uses, but outside the browser. I'm at the very beginning of my Python's journey but I can already tell that I like it! My static website you are reading now is the result of the second program I wrote in Python (the first was a little expense tracking tool). I wrote about it [during the first week](project-management.html) of the academy. I like the natural feeling of writing on Python, removing the syntax barrier and inviting us to focus on logic.

### TidalCycles (Haskell)

I sometimes do live coding music. Live coding means that I write music in real time, from a blank file. Compose rhythms with logical loops, create synth melodies with random variables. The pattern language I use is called [TidalCycles](https://tidalcycles.org) and it is written in [Haskell](https://www.haskell.org/). I couldn't tell you much about the Haskell language, but I can tell you that programming music is super fun to do and reveals its beauty on performances rather than on pure compositions.

### Arduino (C++)

Since the beginning of the academy, I started to learn a little C ++ and the Arduino framework in order to speak with microcontrollers and to obtain an interaction between machines and their environment. I really like the new perspective that this gives to my coding practice: I do not only write software from my computer for other computers, but I now interact with the "real" world, being able to better understand and interact with it. Learning the basics of C ++ helps me to better understand some of the main programming concepts, which I had previously learned on the fly, without structure.

## What's next

The feeling of having given up on processing too soon mixed with the new excitement of writing programs for microcontrollers using Arduino and C++ makes me want to dig a lot deeper into the relationship between creative coding and the physical world.

### openFrameworks

To explore that path, I don't want to specifically use Processing itself, which now seems a bit limited compared to what I want to do, but [openFrameworks](https://openframeworks.cc/), another Processing-type framework, written in C++ (like Arduino) and able to create more powerful programs and therefore produce more complex artistic installations or tools or whatever you want.

---

## My first openFrameworks application

For my first openFrameworks application, I would like to get sensor data and convert it to an interactive visual and audio piece. I'm going to use the [Circuit Playground Express](https://learn.adafruit.com/adafruit-circuit-playground-express/overview) and its multiple integrated sensors and buttons to help me quickly prototype my idea.

### Installation

I first had to install openFrameworks on my machine. Speaking of my machine, I switched from [Elementary OS](https://elementary.io/) to [Manjaro](https://manjaro.org/) two three weeks ago. I no longer depend on the [APT](https://en.wikipedia.org/wiki/APT_(software)) package manager (Advanced Package Tool, from Debian) but from [AUR](https://aur.archlinux.org/) (Arch User Repository), from the Arch Linux community.

My first intention was to look for the openFrameworks package in PAMAC, the graphical AUR package manager for Manjaro Linux, but unfortunately the package is broken there. Which means manual installation is the thing to do. I must say that AUR packages are generally super easy to install, which makes them quite convenient. Too bad this is not the case for openframeworks, and I don't understand enough how it works to lend a hand. Maybe later.

Fortunately, the openFrameworks [download](https://openframeworks.cc/download/) and [installation](https://openframeworks.cc/setup/linux-install/) pages are clear enough and the community is very (re)active and helpful. This gives me hope for my future use of this tool.

### Project architecture

Finding a minimal project architecture was more difficult than expected. The project generator provided by openFrameworks does not work on my system, for whatever reason.

Fortunately, [a project on github](https://github.com/hiroMTB/vscode_oF) shows how to start an openFrameworks project when using VSCode as a text editor. I no longer use this editor but the structure shown there is easily reproducible for any other text editor (I am currently juggling between Vim, Emacs and Atom).

That's why I uploaded my own version of a [minimal starter kit for openFrameworks projects](https://gitlab.com/antoine.j/openframerworks-starter) on Gitlab, hopefully it will help other people get started on their projects.

<pre>
bin/
obj/linux64/Release
src/
- main.cpp
- ofApp.cpp
- ofApp.h
Makefile
addons.make
config.make
</pre>

When oF (openFrameworks) and the starter kit are correctly installed, go to the project folder and use these commands:

- to compile the C++ code: `make`
- to run the program: `make run`
- to compile and run: `make && make run`

### Sending data from Arduino

The first step of my program is to collect the data from the sensors and transmit it to my oF program. To do this, I used a [Circuit Playground Express](https://learn.adafruit.com/adafruit-circuit-playground-express/overview) and its built-in sensors, [PlatformIO](https: // platformio. org /) to compile / send the code to the microcontroller and the [serial communication](https://learn.sparkfun.com/tutorials/serial-communication/all) port.

To create a Pio project, inside the main oF project, which will be used to talk to the Circuit Playground:

<pre>mkdir pio && cd pio && pio project init --board adafruit_circuitplayground_m0</pre>

Then, create a new `main.cpp` file into the `pio/src` folder.

<pre>
#include &lt;Arduino.h&gt;
#include &lt;Adafruit_CircuitPlayground.h&gt;

float lightValue, soundValue;
bool buttonLeft, buttonRight;
bool dark = false;

void setup() {
  CircuitPlayground.begin();
  Serial.begin(9600);
}

void darkSwitch() {
  if (dark) {
    for (int i = 0; i < 10; i++) {
      CircuitPlayground.setPixelColor(i, 0,   0,   255);
    }
  } else {
    CircuitPlayground.clearPixels();
  }
}

void loop() {
  // get
  lightValue = CircuitPlayground.lightSensor();
  soundValue = CircuitPlayground.mic.soundPressureLevel(10);
  buttonLeft = CircuitPlayground.leftButton();
  buttonRight = CircuitPlayground.rightButton();
  // send
  Serial.print(String(lightValue) + "," + String(soundValue) + "," + String(buttonLeft) + "," + String(buttonRight));
  if (Serial.available()) {
    // receive
    char inByte = Serial.read();
    if (inByte == 1) {
    // the received data is '1'
    dark = !dark;
  }
}
darkSwitch();
delay(100);
}
</pre>

([this tool](https://www.freeformatter.com/html-escape.html) helped me to format the code in order to display it correctly in a `<pre>` tag)

The main thing here is this line:

<pre>
Serial.print(String(lightValue) + "," + String(soundValue) + "," + String(buttonLeft) + "," + String(buttonRight));
</pre>

It converts the values to a string format, using the `String ()` [function](https://www.arduino.cc/reference/en/language/variables/data-types/stringobject/), separates them with a `,` and prints them on the serial. It can be a `,` character or any other character that helps you differentiate between the data you are processing.

Another important part of this program is:

<pre>
if (Serial.available()) {
  // receive
  char inByte = Serial.read();
  if (inByte == 1) {    // Whether the received data is '1'
  dark = !dark;
}
</pre>

This means that the `inByte` variable is updated if a serial message is available. It switches the variable "dark" if the program receives a `1` (true) from the serial. This message is sent by the oF program.

We can now send and receive messages via the serial.

### Receiving data to openFrameworks

First, I declare some variables in the `ofApp.h` file. The number `20` must be declared depending on the length of the message we receive.

<pre>
char receivedData[20]; // length we receive
char sendData = 1;
ofSerial serial;
</pre>

I call my custom function into update().

<pre>
void ofApp::update(){
	serialValues();
}
</pre>

In `serialValues()`, while the serial is available, we write the data in a `receivedDate` variable and run another `valuesConversion` function to do something with it.

I prefer to keep these two functions separate to facilitate their reuse later. I will definitely reuse the `serialValues` function as it is, but I don't think that will be the case for `valuesConversion ()`.

<pre>
void ofApp::serialValues() {
	while(serial.available() > 0) {
		serial.readBytes(receivedData, 20);
		valuesConversion();
	}
}
</pre>

Then I parse the `receivedData` to make an array, which I write in `values`. I can now call `values.at(0)` to get the first value, and so on. The separator `,` must correspond to the separator that we chose previously, in the Arduino code.

<pre>
void ofApp::valuesConversion() {
	vector<string> values;
	values = ofSplitString(receivedData, ",");
	lightValue = ofToFloat(values.at(0));
	soundValue = ofToFloat(values.at(1));
	buttonLeft = ofToBool(values.at(2));
	buttonRight = ofToBool(values.at(3));
	lightLevel = ofMap(lightValue, 0, 1023, 0, 100);
	soundLevel = ofMap(soundValue, 50, 100, 0, 100);
	cout << "light: " << lightLevel << " / sound: " << soundLevel << endl;
	cout << "left: " << buttonLeft << " / right: " << buttonRight << endl;
}
</pre>

The `ofMap()` function allows us to map a value, from its initial range to a new one.
For example, the light sensor collects data in a range of 0 to 1023, but for ease of use, I convert it to another value, from 0 to 100.

I can now receive data from the serial and convert it to the type of variable I need, in an easy-to-use range. I have everything I need to create my application.

### Make something out of it


TODO: video of the final result

---

# Useful links


- [pio and linux](https://docs.platformio.org/en/latest/faq.html#platformio-udev-rules)
- [pio playground express](https://docs.platformio.org/en/latest/boards/atmelsam/adafruit_circuitplayground_m0.html)
- [oF ofSerial](https://openframeworks.cc/documentation/communication/ofSerial/)
- [tuto data send/receive](https://maker.pro/arduino/projects/how-to-send-and-receive-data-through-the-openframeworks-platform-using-arduino)
- [light sensor](https://learn.adafruit.com/circuit-playground-lesson-number-0/light-sensor)
- [sound sensor](https://learn.adafruit.com/circuit-playground-lesson-number-0/sound-sensor)
- [accelerometer](https://learn.adafruit.com/circuit-playground-lesson-number-0/accelerometer)
- [ofToFloat](https://openframeworks.cc/documentation/utils/ofUtils/#!show_ofToFloat)
- [muliple analog arduino](https://forum.openframeworks.cc/t/reading-multiple-analog-input-from-arduino/29805)
- [separate values arduino](https://forum.openframeworks.cc/t/how-can-separate-values-from-arduino/24246)
- [how to send and receive data](https://maker.pro/arduino/projects/how-to-send-and-receive-data-through-the-openframeworks-platform-using-arduino)
