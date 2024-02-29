# this library has functions that let us manipulate the timing of our Python sketch
import time  
# this library lets us control the pins of the microcontroller
import board 
# import two functions to help us control digital pins
from digitalio import DigitalInOut, Direction 

led = DigitalInOut(board.D13) # store pin13 into the variable led
led.direction = Direction.OUTPUT # make the LED an output

while True: # our main loop
	led.value = False # set the LED to be off
	time.sleep(1)  # in seconds, delays the code from running
	led.value = True # set the LED to be on
	time.sleep(1)  # in seconds, delays the code from running