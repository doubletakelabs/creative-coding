# You will need to run pip install paho-mqtt before running
# This example is intended to be run on your computer

import paho.mqtt.client as mqtt

sub_topic = "status"
pub_topic = "led"

# The callback for when the client receives a connected response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe(sub_topic)

# The callback for when a message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    client.publish(pub_topic, "hello") # publish a message to the led topic

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("USERNAME_HERE", "PASSWORD_HERE")
client.connect("mqtt.doubletake.design", 1883, 60)
client.loop_forever() # if you use this line, the script will run forever and just listen for messages

# another option is to use client.loop_start() and client.loop_stop() to start and stop the loop - see below
#while True:
#    client.loop_start()
