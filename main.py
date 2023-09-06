"""

Used MQTT Device API for ThingsBoard Integration

This Python script connects to a ThingsBoard MQTT broker and performs the following tasks:
1. Subscribes to attribute updates for a device.
2. Publishes telemetry data to the device.
3. Handles disconnection and uncaught exceptions gracefully.


To use this script:
1. Replace THINGSBOARD_HOST and ACCESS_TOKEN with demo ThingsBoard server URL and device access token.
2. Install the required library: `pip install requirements.txt`.

Make sure you have a device with the given access token in your ThingsBoard instance.

Developer: Rohit Chaurasia
Date: 06-09-2023

"""

import paho.mqtt.client as mqtt
import signal
import sys
import json
import time


# Thingsboard server details
THINGSBOARD_HOST = "demo.thingsboard.io"  # Replace with your demo Thingsboard server URL
ACCESS_TOKEN = "KohIJGqur27g0X5vH3ZY"  # Replace with your device's access token


# MQTT topics
attributes_topic = "v1/devices/me/attributes"
telemetry_topic = "v1/devices/me/telemetry"
attributes_request_topic = "v1/devices/me/attributes/request/1"
attributes_response_topic = attributes_request_topic.replace("request", "response")

# Initialization of MQTT client using Thingsboard host and device access token
print(f"Connecting to: {THINGSBOARD_HOST} using access token: {ACCESS_TOKEN}")
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)

# Initialize Global variable to track the last received value of 'data' shared attribute
last_data_value = None

# Triggers when client is successfully connected to the Thingsboard server
def on_connect(client, userdata, flags, rc):
    print("Client connected!")

    # Subscribe to shared attribute changes on the server side
    client.subscribe(attributes_topic)

client.on_connect = on_connect

# function to handle incoming MQTT messages
def on_message(client, userdata, msg):
    topic = msg.topic
    message = msg.payload.decode("utf-8")

    global last_data_value

    if topic == attributes_topic:
        # Process attributes update notification
        print(f"Received attribute update notification: {message}")
        data = json.loads(message)

        if "data" in data:
            current_data_value = data["data"]

            # Check if the 'data' value has changed
            if current_data_value != last_data_value:
                # Update the 'echo_data' telemetry with the new value
                telemetry_data = {
                    "echo_data": current_data_value
                }
                print(f"Publishing 'echo_data': {current_data_value}")
                client.publish(telemetry_topic, json.dumps(telemetry_data))

                # Update the last known value
                last_data_value = current_data_value

client.on_message = on_message

# Catches ctrl+c event
def on_sigint(signal, frame):
    print("\nDisconnecting...")
    client.disconnect()
    print("Thank You Nunam!")
    sys.exit(0)


# function to handle uncaught exceptions
def on_uncaught_exception(exctype, value, traceback):
    print("Uncaught Exception...")
    print(traceback)
    sys.exit(99)

# Set signal handler for Ctrl+C
signal.signal(signal.SIGINT, on_sigint)
# Set exception handler for uncaught exceptions
sys.excepthook = on_uncaught_exception

# Start the MQTT client loop
client.loop_start()

# Run the script indefinitely
while True:
    # Send a request for the 'data' shared attribute
    client.publish(attributes_request_topic, json.dumps({"sharedKeys": "data"}))
    time.sleep(1)  # Wait for 1 second before requesting again
