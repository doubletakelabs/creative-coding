# this is to be run on your computer with your sensor board connected over USB
# on a mac, you should look for the device like this "/dev/cu.usbmodem866B3BB2E1C41: COLUMBIA-DSL-SENSOR-BOARD-V1"
# your 'port' will be different than mine though. 
# You want to copy the port name, the part that looks like this: "/dev/cu.usbmodem866B3BB2E1C41"
# this can then be used in the serial-readline.py file

# You will need to install pip3 install pyserial before running

import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))