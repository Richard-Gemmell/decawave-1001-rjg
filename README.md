# decawave-1001-rjg
## Introduction
This is a device driver enable a Raspberry Pi to use the Decawave 1001 UWB positioning module.

The Decawave is a low cost UWB positioning module. A group of at least 4 modules forms a mesh network that can locate a fifth, mobile module with an accuracy of around +-0.2 meters. For more information and datasheets see [Decawave's website](https://www.decawave.com/product/dwm1001-development-board/).

The DWM1001 is available as a development board about the size of a credit card.

## Driver Features
* Connects over SPI
* Supports hardware interrupts for data ready
* Optionally enables high priority thread scheduling

## Limitations
* Requires python 3.7

## Examples
Examples are available on [Github](https://github.com/Richard-Gemmell/decawave-1001-rjg/tree/master/examples).
