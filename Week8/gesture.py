# you can find the libraries for the sensor board at bit.ly/at6190-libraries

# From https://github.com/adafruit/Adafruit_CircuitPython_APDS9960/blob/main/examples/apds9960_gesture_simpletest.py
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
from adafruit_apds9960.apds9960 import APDS9960

i2c = board.I2C()  # sets up the protocol to communicate with our sensor

apds = APDS9960(i2c) # creates the sensor object
apds.enable_proximity = True # enables proximity detection
apds.enable_gesture = True # enables gesture detection

apds.rotation = 270 # rotate the gesture detection to match the orientation of our board, you can change this

while True:
    gesture = apds.gesture()

    if gesture == 0x01:
        print("up")
    elif gesture == 0x02:
        print("down")
    elif gesture == 0x03:
        print("left")
    elif gesture == 0x04:
        print("right")