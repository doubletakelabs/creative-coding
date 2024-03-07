import board
import pwmio

led = pwmio.PWMOut(board.D13)

while True:
    for cycle in range(0, 65535):
        led.duty_cycle = cycle
    for cycle in range(65534, 0, -1):
        led.duty_cycle = cycle