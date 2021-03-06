---
title: Prototyping an incubator
---

As I said, my partner is building an incubator to help us grow mycellium (and other fermented food) and she asked me an hand to help her with the electronic part. In this context, I will prototype an incubator by using the devices I already have. I will do it by following the spiral methodology: a first round with the basic features, and then other ones with additional options.

## Update 2020-11

I have started a new project dedicated to the incubator and the sub-projects it brings. Everything is documented under [incubator-v0-1.html](incubator-v0-1.html).

![](incubator-shield.jpg)

[Incubator](button:incubator-v0-1.html)

## Round #01: the basics

For the first round, I would like to control a fan and a Peltier (thermoelectric cooler) to get an ideal temperature into a closed space, using a Arduino UNO. The Peltier will be used to warm up the temperature and the fan will help us to either cool down or to distribute the heat evenly.

> Thermoelectric coolers (TEC or Peltier) create a temperature differential on each side. One side gets hot and the other side gets cool. Therefore, they can be used to either warm something up or cool something down, depending on which side you use.
>> [Sparkfun - Thermoelectric Cooler](https://www.sparkfun.com/products/15082)

The Peltier could be used to warm up or cool down the space depending on the wanted temperature, to do so, we apparently have to reverse its polarity. I will try to explore this track later. I will focus on the warm side for now.

Because the fan and the Peltier device require a voltage of 12V and the arduino can only supply 5V, I added an external power supply in the circuit. It is then necessary to also include MOSFETs to control how and when the current flows through the devices.

### Material

- Arduino UNO ([pinout](https://content.arduino.cc/assets/Pinout-UNOrev3_latest.pdf))
- Thermoelectric Cooler ([info](https://www.sparkfun.com/products/15082) / [datasheet](https://cdn.sparkfun.com/assets/a/d/2/a/7 TEC112707Thermoelectric_Module_Datasheet.pdf))
- 12V Axial Fan (EverFlow R127025BU DC 12V 0.40AMP 4-pin connector)
- 10K thermistor
- MOSFET N-CH ([datasheet](https://media.digikey.com/pdf/Data%20Sheets/NXP%20PDFs/IRFZ44N_Rev1.pdf))
- 12V external supply
- 10K resistors
- Diode

### Schematics

I did a schematic in [KiCAD](https://www.kicad-pcb.org/) to help me understand the different components ad how to plug them together. Here is a [larger image](files/incubator-schema.jpg) if you like.

![incubator-schema](incubator-schema.jpg)

File: [incubator_01.pro](files/incubator_01.pro)

![incubator prototype](incubator-circuit.jpg)

### Code

I attribute the pins values according to my schematics and define some settings, such as the ideal temperature and the accepted range, but also the fan and Peltier power.

I do not want the system to go from a stage "It is too hot, I have to cool the temperature" to a stage "It is too cold, let's heat it now" too quickly. This is why I implemented the value `tempRange`, saying that there are acceptable values around the ideal, which makes the system less reactive but constant.

The fan and the Peltier do not have to operate at their maximum value all the time. This is why I plugged them on PWM pins, to be more subtle than just `HIGH` and `LOW` values. A pulse-width modulation (PWM) pin allow us to simulate an analog behavior by manipulating the frequency of the signal (read the [Secrets of Arduino PWM](https://www.arduino.cc/en/Tutorial/SecretsOfArduinoPWM)).

In addition, I introduced the values `powerFan` and` powerPeltier`, by mapping a value between 0 and 99 (easier to manipulate) to the real value going from 0 to 255 (analog style), to declare the necessary power to both devices. According to the test I did, a value between 20 and 40 is sufficient and prevents the system from overheating, damaging the wires or the devices.

<pre>
// PINS
int pinFan = 3;
int pinPeltier = 5;
int pinThermo = 0;
// VARIABLES
int val;
float temp;
// SETTINGS
int powerFan = 20; // 0-99
int powerPeltier = 30; // 0-99
int tempIdeal = 28;
int tempRange = 2;

void setup() {
  Serial.begin(9600);
  pinMode(pinFan, OUTPUT);
  pinMode(pinPeltier, OUTPUT);
}

void thermistor(int RawADC) {
  temp = log(((10240000/RawADC) - 10000));
  temp = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * temp * temp ))* temp );
  temp = temp - 273.15;
}

void loop(){
  int levelPeltier = map(powerPeltier, 0, 99, 0, 255);
  int levelFan = map(powerFan, 0, 99, 0, 255);
  int a = analogRead(pinThermo);
  thermistor(a);
  if (temp <= tempIdeal - tempRange) {
    analogWrite(pinPeltier, levelPeltier);
    analogWrite(pinFan, 0);
    Serial.print("Peltier: on / ");
  } else if (temp >= tempIdeal + tempRange) {
    analogWrite(pinFan, levelFan);
    analogWrite(pinPeltier, 0);
    Serial.print("Fan: on / ");
  } else {
    analogWrite(pinFan, 0);
    analogWrite(pinPeltier, 0);
  }
  Serial.print("Temp: ");
  Serial.print(temp);
  Serial.print(" / Ideal: ");
  Serial.println(tempIdeal);
  delay(1000);
}
</pre>

<video><source src="incubator-prototype.mp4"></video>

### Results

The overall result of this prototype is quite good. The temperature is easily regulated with the Peltier and the fan, and the thermistor obtains precise values.

![incubator prototype](incubator-overview.jpg)

When I tried plugging in the devices for the first time, I was running them at 12 V continuously, but the wires and MOSFETS quickly became very hot, which was a concern. There was too much current in the circuit. Fortunately, not using them continuously but at regular intervals has given us much better results: the devices always work as we want when they receive less current, at least for my needs. This brings me to the PWM tip (as mentioned above).

![incubator prototype](incubator-close.jpg)

I put the thermistor and the Pelier in a cup, to allow the system to increase its temperature without losing too much heat in the surrounding environment. The fan is positioned in front of them, which gives us the possibility to expel the hot air.

![incubator prototype](incubator-power.jpg)

# Next

Now that the electronics work as I want, I hand over to my partner. The next step will probably be a real test with a closed space to see how quickly we can lower or increase the temperature inside. We are also thinking of using the fan to distribute the heat evenly. Be sure to read [Maud's documentation](https://maudb.gitlab.io/dok/projects/biolab-kitchen/) to see her progress on the incubator.

### References

- [Biohack Academy: Incubator](https://biohackacademy.github.io/bha6/class/3/pdf/3.4%20Incubator%20design.pdf)
- [BioLab Kitchen by Maud Bausier](https://maudb.gitlab.io/dok/projects/biolab-kitchen/)
- [High-Power Control: Arduino + N-Channel MOSFET](https://bildr.org/2012/03/rfp30n06le-arduino/)
- [Sparkfun: MOSFETS explained](https://www.sparkfun.com/news/819)
- [4 Pin Fan](https://allpinouts.org/pinouts/connectors/motherboards/motherboard-cpu-4-pin-fan/)
- [NodeMCU documentation](https://nodemcu.readthedocs.io/en/master/)
- [NodeMCU details and Pinout](https://www.instructables.com/id/NodeMCU-ESP8266-Details-and-Pinout/)
- [PlatformIO NodeMCU 1.0](https://docs.platformio.org/en/latest/boards/espressif8266/nodemcuv2.html)
