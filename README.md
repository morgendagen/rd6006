# RIDEN RD6006 Python module

This module allows to control a RD6006 using Python.

As with previous models, the RD6006 uses the Modbus protocol over serial, the
registers however are different than the DPS models. The registers are described
in the [registers.md](registers.md) file.

## Features

It allows to control the following options :
 * Output voltage and current
 * Protection voltage and current
 * Backlight
 * Enable status

Communicate with the RD6006 over :
 * USB
 * WiFi (using an ESP-01 module with special firmware)

## Installation
```
$ python setup.py install --user
```

## Usage

See examples in the [examples](examples) directory.
