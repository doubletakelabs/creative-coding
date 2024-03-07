import analogio
import board
import time

mic = analogio.AnalogIn(board.A9)

while True:
    value = mic.value
    if mic.value > 40000:
        print("loud")
        time.sleep(.1)