# Be sure to run pip install python-osc before running
import argparse
import math

from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server

def print_handler(address, *args):
  print(f"{address}: {args}")

while True:
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="10.206.63.39")
  parser.add_argument("--port",
      type=int, default=7777)
  args = parser.parse_args()

  dispatcher = Dispatcher()
  dispatcher.map("*", print_handler) # change this line to filter for the address you want to listen to
  # an example of a filter would be: dispatcher.map("/outputs", print_handler)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()