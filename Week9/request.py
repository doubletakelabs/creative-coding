import time
import wifi
import ssl
import socketpool
import adafruit_requests
import microcontroller

print()
print("Connecting to WiFi")

#  connect to your SSID
wifi.radio.connect('WIRELESS_NETWORK_NAME_HERE', 'WIRELESS_PASSWORD_HERE')
print("Connected to WiFi")

url = "https://date.nager.at/api/v3/publicholidays/2024/US"
pool = socketpool.SocketPool(wifi.radio)

requests = adafruit_requests.Session(pool, ssl.create_default_context())

try:
    #  sends a request to the public holiday API
    response = requests.get(url)
    response_as_json = response.json()
    print(response_as_json)
    
except Exception as e:
    print("Error:\n", str(e))
    print("Resetting microcontroller in 10 seconds")
    time.sleep(10)
    microcontroller.reset()