# you can find the libraries for the sensor board at bit.ly/at6190-libraries

# From https://github.com/adafruit/Adafruit_CircuitPython_APDS9960/blob/main/examples/apds9960_proximity_simpletest.py
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
from adafruit_apds9960.apds9960 import APDS9960

i2c = board.I2C()  # sets up the protocol to communicate with our sensor

apds = APDS9960(i2c) # creates the sensor object
apds.enable_proximity = True # enables proximity detection

while True:
    distance = apds.proximity # gets a proximity reading
    print(distance)