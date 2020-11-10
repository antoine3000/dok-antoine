---
title: Electronics
---

The electronic part of the incubator must remain as simple as possible, to offer the possibility of being understood and modified by others. I don't want to lock the users in a device they don't understand.

It is built as an extra board that comes with a Barduino, allowing it to operate with two 12V outputs and one 5V input.

# Components

## Barduino

A [Barduino](https://gitlab.com/fablabbcn-projects/electronics/barduino), an ESP32 development board made in Barcelona, is used as the brain. This allows me to use a Wifi compatible board with a functional USB connection without having to do it (again) by myself Moreover, it allows me to design a shield (something I've never done before) and to participate in an open-source project that I'd like to support.

## Humidity and temperature sensor

A [DHT11](https://www.adafruit.com/product/386) humidity and temperature sensor provides information on what is happening in the incubator. I use the DHT11 mainly because it is available in the laboratory. I am not entirely satisfied with this sensor because it is slow and sometimes skips some data. It is clearly sufficient for this project because I don't need a high efficiency sensor, but it is not ideal.

## Heating pad

A [heating pad](https://www.adafruit.com/product/1481) ([datasheet](https://cdn-shop.adafruit.com/datasheets/Ultra+Heating+Fabric.pdf)) is used to warm up the temperature inside the incubator. When supplied with 12V, it can reach up to 110°C. It is not necessary to reach this temperature, but it will allow us to have the desired temperature even if the incubator is not fully insulated.

## Fan

A [12V fan](https://www.sparkfun.com/products/16034) is used to distribute the heat evenly inside the incubator, or to try to cool it down in case it gets too hot (which could easily happen in the Barcelona sun).

