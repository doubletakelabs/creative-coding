# This example is similar to the one from the Adafruit website. If you would like some more
# functionality, take a look at their example page which also shows how to have the microcontroller
# behave like a mouse. These are great for connecting to py5 or other scripts on your computer

# this library has functions that let us manipulate the timing of our Python sketch
import time  
# this library lets us control the pins of the microcontroller
import board 
# import three functions to help us control digital pins
from digitalio import DigitalInOut, Direction, Pull

# make sure to include the adafruit_hid library folder on your microcontroller
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# use board.D16 for Button1 or board.D15 for Button2
button = DigitalInOut(board.D16) #  stores pin16 into the variable button 
button.direction = Direction.INPUT # make the button an input
button.pull = Pull.DOWN # set the pull direction for the button

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US but you can select a different country if you would like

last_button_state = False

while True:
    if button.value is True and button.value is not last_button_state:
        key = Keycode.A # the key you would like to press
        keyboard.press(key)
        keyboard.release_all()
        
    last_button_state = button.value # saving the state of the button so we don't have multiple key presses
        
    time.sleep(0.01) # small amount of time for debounce