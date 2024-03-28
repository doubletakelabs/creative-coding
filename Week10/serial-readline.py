# This script is intended to be run on your computer
# Be sure to run the serial-listports.py file first to get the correct port
# Use that port on line 9 below to connect to your board. 
# Note that on Windows the port will be something like 'COM9'

# You will need to install pip3 install pyserial before running

import serial
import time

sensor_board = serial.Serial(port="/dev/cu.usbmodem866B3BB2E1C41", baudrate=115200, timeout=.1)

def read():
	time.sleep(0.05)
	data = sensor_board.readline()
	return str(data, 'ascii').split()

while True:
	value = read()
	if(value != []):
		if(value[0] == '1'):
			print("received!")