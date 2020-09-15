---
title: Programming the ATtiny1614
---

The ATtiny1614 isn't yet supported by PlatformIO and therefore needs another method to be programmed. Fortunately, [pyupdi](https://github.com/mraardvark/pyupdi) is here! Pyupdi is a Python UPDI driver for programming the "new" tinyAVR and megaAVR devices.

## Connectivity

Power comes from a USB cable via a FTDI connector. The data comes from the UPDI connector and goes through another FTDI connector.

## Install

`git clone https://github.com/mraardvark/pyupdi`

`pip install -r requirements.txt`

## Compile

The first thing to do is to compile the code with the Arduino IDE and then send it with `pyupdi`.
To be able to compile the code, first install the [megaTinyCore](https://github.com/SpenceKonde/megaTinyCore) library using the Libraries manager into the Arduino IDE and select the ATtiny1614 board.

From the Arduini IDE console, locate the `.ino.hex` that is generated when you compile and copy its path. It should be something like `/tmp/arduino_build_342195/Blink.ino.hex`.

## Upload

Once your program is correctly compiled, open a terminal to send it to your device.

First, run `ls /dev/* | greb usb` to know the name of your port. It should look like `/dev/ttyUSB0`.

Then, run pyupdi with the name of the board you're working on `tiny1614`, the port where you want to send the code `/dev/ttyUSB0` and the code itself `/temp/arduino_buid_342195/Blink.ino.hex`.

<pre>
pyupdi.py -d tiny1614 -c /dev/ttyUSB0 -b 9600 -f /tmp/arduino_build_342195/Blink.ino.hex -v
</pre>

<video><source src="pomo-test.mp4"></video>