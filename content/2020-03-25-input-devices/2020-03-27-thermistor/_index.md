---
title: Thermistor
---

Or how to measure temperature using a resistor.

> To measure the temperature, we need to measure the resistance. However, a microcontroller does not have a resistance-meter built in. Instead, it only has a voltage reader known as a analog-digital-converter. So what we have to do is convert the resistance into a voltage, and we will do that by adding another resistor and connecting them in series. Now you just measure the voltage in the middle, as the resistance changes, the voltage changes too, according to the simple voltage-divider equation. We just need to keep one resistor fixed
> > Analog Voltage Reading Method, [Adafruit](https://learn.adafruit.com/thermistor/using-a-thermistor)

![thermo-photo-1](uno-thermo-photo-1.jpg)
![thermo-photo-2](uno-thermo-photo-2.jpg)

## Connection

The thermistor is linked to the `5V` pin and to an analog pin `0` through a 10k resistor, and to `GND`.

![uno-thermi](uno-thermi.png)

([image source](https://learn.adafruit.com/thermistor/using-a-thermistor))

## Code

Here is the piece of code that print the value of the analog pin `0` and convert its values into a Celcius temperature.

<pre>
int analogPin = 0;
int beta = 3950;
int resistance = 10;

void setup() {
  Serial.begin(9600);
}

void loop() {
  long a = analogRead(analogPin);
  float temp = beta / (log((1025.0*10/a-10)/10) + beta/298.0)-273.0;
  Serial.println(temp);
  delay(1000);
}
</pre>

TODO: Update values according to [this tutorial](https://computers.tutsplus.com/tutorials/how-to-read-temperatures-with-arduino--mac-53714)
