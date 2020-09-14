---
title: Moisture level sensor
---

Water is a conductive element, and the more water there is in the soil the more electricity can flow through it. So, in order to measure the soil moisture level, we can integrate it into an electrical circuit and measure the voltage. The more voltage in the circuit, the more water there is in the soil.

![moist-setup](moist-setup.jpg)

To represent it, I built a small system that lights a green LED when the soil is wet and a red LED when it's dry.

## Connection

- 5V from the Arduino UNO to the soil
- A0 (anaolog) from the Arduino UNO to the soil
- A0 (analog) from the Arduino UNO to the GND (analog) through a 10kΩ resistor
- 11 (digital) to the red LED through a 220Ω resistor
- 12 (digital) to the green LED through a 220Ω resistor
- LED's to the GND (digital)


![moist-closeup](moist-closeup.jpg)

## Code

The code is basic. If the analog pin gets a high voltage, it means that the soil is moist and the plant is *happy* so we turn on the green LED, and vice versa.

I plan to write a more complex code in the coming weeks, a code that takes into account the amount of water needed for each specific plant, and to alert when it's too dry *or* too weet.

<pre>
int ledGreen = 12;
int ledRed = 11;
int contactVal = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledGreen, OUTPUT);
  pinMode(ledRed, OUTPUT);
}

void loop() {
  contactVal = analogRead(0);
  Serial.println(contactVal);
  if (contactVal >= 350) {
    digitalWrite(ledRed, LOW);
    digitalWrite(ledGreen, HIGH);
  } else {
    digitalWrite(ledRed, HIGH);
    digitalWrite(ledGreen, LOW);
  }
  delay(250);
}
</pre>

Here is my tiny system in action, olé.

<video><source src="moist-test.mp4"</video>
