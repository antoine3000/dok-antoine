---
title: Materials
---

My project is made up of three elements: the *plant*, the *clone* and the *panel*.

---

## The plant

The *plant* is a device connected to a plant. It has sensors and a microcontroller equipped with a WiFi transceiver module. Its role is to sense data from the plant and its environment, process them and send them to the *clone*.

- Microcontroller (ESP32)
- Light sensor
- Temperature sensor
- Soil moisture sensor
- Electrical activity sensor (ADC, Operational amplifier)
- Capacitive sensor
- Power supply
- Enclosure (wood and acrylic)

### References
  - [Smart Citizen Docs - Soil sensors](https://docs.smartcitizen.me/Components/Soil/)
  - [Chirp! - The plant watering alarm](https://wemakethings.net/chirp/)
  - Analog to digital converter (ADC): [AD8605ARTZ-REEL7](https://www.digikey.com/product-detail/en/analog-devices-inc/AD8605ARTZ-REEL7/AD8605ARTZREEL7CT-ND/751314)
  - Operational amplifier [AD8605, AD8606, AD86081](https://www.analog.com/media/en/technical-documentation/data-sheets/AD8605_8606_8608.pdf)

  ---

## The clone

The *clone* is a device that receives data from the plant and its environment and transforms them into physical movement using an air pump to inflate and deflate a flexible material, creating a movement inspired by our breathing cycle, revealing how the plant feels.

- Air pump
- Solenoid
- Pipes
- Balloon (made out of recycled plastic)
- Cover (made out of flexible fabric)
- Power supply
- Enclosure (wood and acrylic)

### References

- [Blower - Squirrel Cage (12V)](https://www.sparkfun.com/products/11270)

---

## The panel

The *panel* is a wooden structure that can host up to five *clones* to create a more detailed and unique installation with custom parameters.

- Wood panels
- 3D printed joinery
