import time
import board
import ssl
import socketpool
import wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT
from digitalio import DigitalInOut, Direction
import neopixel

print("Connecting to WiFi")

# if you would like to see which Wi-Fi networks the board can see, uncomment the 3 lines below
#for network in wifi.radio.start_scanning_networks():
#    print("\t%s\t\tRSSI: %d\tChannel: %d" % (str(network.ssid, "utf-8"), network.rssi, network.channel))   
#wifi.radio.stop_scanning_networks()

wifi.radio.connect('WIRELESS_NETWORK_NAME_HERE', 'WIRELESS_PASSWORD_HERE')
print("Connected to WiFi")

# Setup your topics
mqtt_topic_sub = "led"

pixel_pin = board.D42
num_pixels = 1
pwr = DigitalInOut(board.NEOPIXEL_POWER)
pwr.direction = Direction.OUTPUT
pwr.value = True

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

GREEN = (0, 255, 0)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)

# Define callback methods which are called when events occur
def connected(client, userdata, flags, rc):
    # This function will be called when the client is connected
    # successfully to the broker.
    print(f"Connected to MQTT Broker! Listening for topic changes on {mqtt_topic_sub}")
    # Subscribe to all changes on the onoff_feed.
    client.subscribe(mqtt_topic_sub)


def disconnected(client, userdata, rc):
    # This method is called when the client is disconnected
    print("Disconnected from MQTT Broker!")


def message(client, topic, message):
    # This method is called when a topic the client is subscribed to
    # has a new message.
    print(f"New message on topic {topic}: {message}")
    if(message is "GREEN"):
        print("received Green")
        pixels.fill(GREEN)
        pixels.show()
    elif(message is "PURPLE"):
        pixels.fill(PURPLE)
        pixels.show()
    else:
        pixels.fill(OFF)
        pixels.show()

# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)
ssl_context = ssl.create_default_context()

# Set up a MQTT Client
mqtt_client = MQTT.MQTT(
    broker="mqtt.doubletake.design",
    username="PUT_USERNAME_HERE",
    password="PUT_PASSWORD_HERE",
    socket_pool=pool,
    ssl_context=ssl_context,
)

# Setup the callback methods above
mqtt_client.on_connect = connected
mqtt_client.on_disconnect = disconnected
mqtt_client.on_message = message

# Connect the client to the MQTT broker.
print("Connecting to MQTT Broker...")
mqtt_client.connect()

while True:
    # Poll the message queue
    mqtt_client.loop(timeout=1)
    time.sleep(.01)
