---
title: Materials
---

The device is made up of two elements: the *plant* and the *clone*.

# The plant

The *plant* is the element connected to a plant, it has sensors and a microcontroller equipped with a WiFi transceiver module ([ESP32-WROOM-32](https://www.digikey.com/product-detail/en/espressif-systems/ESP32-WROOM-32/1904-1010-1-ND/8544305)).

## Soil moisture sensor

TODO: soil moisture sensor - list of materials

### References

- [Smart Citizen Docs - Soil sensors](https://docs.smartcitizen.me/Components/Soil/)
- [Chirp! - The plant watering alarm](https://wemakethings.net/chirp/) (Moisture sensing and light sensing)


## Light sensor

TODO: light sensor - list of materials

### References

- [Chirp! - The plant watering alarm](https://wemakethings.net/chirp/) (Moisture sensing and light sensing)

## Temperature sensor

TODO: temperature sensor - list of materials

## Electrical activity sensor

- Analog to digital converter (ADC): [AD8605ARTZ-REEL7](https://www.digikey.com/product-detail/en/analog-devices-inc/AD8605ARTZ-REEL7/AD8605ARTZREEL7CT-ND/751314)
- Operational amplifier [AD8605, AD8606, AD86081](https://www.analog.com/media/en/technical-documentation/data-sheets/AD8605_8606_8608.pdf)

TODO: electrical activity sensor - list of materials

# The clone

The *clone* is the element that represents the health and activity of the plant.

It is also equipped with ESP32-WROOM-32, and receives its instructions via the WiFi protocol. Depending on the messages it receives, it is been activated, revealing how the plant feels.

## Movement

I'm exploring two different tracks concerning the behavior of the *clone*.

It could be a balloon that inflates and deflates, causing an organic movement that is difficult to control, which must always be in action.

Or a mechanical movement, slow and under control, which could be activated and deactivated at the speed of real changes in the plant and its environment, resulting in something contemplative and less energy consuming.

### Pneumatic


TODO: pneumatic movement - list of materials

### Mechanical

TODO: mechanical movement - list of materials

## Channel selection

TODO: channel selection - list of materials

## Modifiers selection

TODO: modifiers selection - list of materials

## Enclosure

TODO: enclosure - list of materials
