import time
import board
from analogio import AnalogIn

analog_in = AnalogIn(board.A8) # set the pin to be an analog input

while True:
    value = analog_in.value # read the value from the potentiometer
    print(value)
    time.sleep(0.1)