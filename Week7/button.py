# this library has functions that let us manipulate the timing of our Python sketch
import time  
# this library lets us control the pins of the microcontroller
import board 
# import three functions to help us control digital pins
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.D13) # stores pin13 into the variable led
led.direction = Direction.OUTPUT # make the LED an output

# use board.D16 for Button1 or board.D15 for Button2
button = DigitalInOut(board.D16) #  stores pin16 into the variable button 
button.direction = Direction.INPUT # make the button an input
button.pull = Pull.DOWN # set the pull direction for the button

while True:
	if button.value is True: # if the button is pressed
		led.value = True # turn the LED on
	else: # if the button is not pressed
		led.value = False # turn the LED off

	time.sleep(0.01) # small amount of time for debounce