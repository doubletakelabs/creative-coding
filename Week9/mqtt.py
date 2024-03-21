import time
import ssl
import socketpool
import wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT

print("Connecting to WiFi")
wifi.radio.connect('WIRELESS_NETWORK_NAME_HERE', 'WIRELESS_PASSWORD_HERE')
print("Connected to WiFi")

# Setup your topics
mqtt_topic_pub = "publish_topic"
mqtt_topic_sub = "subscribe_topic"


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

temp_val = 0
while True:
    # Poll the message queue
    mqtt_client.loop(timeout=1)

    # Send a new message
    mqtt_client.publish(mqtt_topic_pub, temp_val)
    print("Sent!")
    temp_val += 1
    time.sleep(5) # wait 5 seconds and then send another message
