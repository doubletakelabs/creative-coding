# this script is intended to be put on your microcontroller

import time  
import board 
from digitalio import DigitalInOut, Direction, Pull

# use board.D16 for Button1 or board.D15 for Button2
button = DigitalInOut(board.D16) #  stores pin16 into the variable button 
button.direction = Direction.INPUT # make the button an input
button.pull = Pull.DOWN # set the pull direction for the button

last_button_state = False

while True:
    if button.value is True and button.value is not last_button_state:
        value = 1
        print(value)
        
    last_button_state = button.value # saving the state of the button so we don't have multiple key presses
        
    time.sleep(0.01) # small amount of time for debounce