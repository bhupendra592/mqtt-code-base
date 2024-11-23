import paho.mqtt.client as mqtt
from constants import BROKER, PORT, TOPIC_PUB, CLIENT_ID_PUB, KEEP_ALIVE
import time

# Callback triggered when the client connects to the broker.
def on_connect(client, userdata, flags, rc):
    """
    client: MQTT client instance
    userdata: Custom data passed to the client
    flags: Connection flags sent by the broker
    rc: Connection result code (0 indicates successful connection)
    """
    if rc == 0:
        print("Publisher connected to broker")
    else:
        print(f"Publisher connection failed with code {rc}")

# Callback triggered when a message is successfully published.
def on_publish(client, userdata, mid):
    """
    client: MQTT client instance
    userdata: Custom data passed to the client
    mid: Message ID (assigned by the broker for tracking delivery)
    """
    print(f"Message published with mid: {mid}")

# Initialize MQTT client with a unique client ID for the publisher.
client = mqtt.Client(CLIENT_ID_PUB)

# Attach callback functions for connection and publishing.
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the MQTT broker using the specified address and port.
try:
    client.connect(BROKER, PORT, KEEP_ALIVE)
except Exception as e:
    print(f"Could not connect to broker: {e}")
    exit(1)

# Start the MQTT network loop in a separate thread to process incoming and outgoing messages.
client.loop_start()

# Publish messages in a loop until the user exits.
try:
    while True:
        # Simulate commands for home automation devices
        print("\nChoose an action:")
        print("1. Turn ON living room light")
        print("2. Turn OFF living room light")
        print("3. Set thermostat temperature")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            command = {"device": "living_room_light", "state": "ON"}
        elif choice == "2":
            command = {"device": "living_room_light", "state": "OFF"}
        elif choice == "3":
            temperature = input("Enter temperature: ")
            command = {"device": "thermostat", "state": int(temperature)}
        elif choice == "4":
            break
        else:
            print("Invalid choice")
            continue
        
        # Publish the command to the control topic
        client.publish(TOPIC_PUB, payload=str(command), qos=1)
        print(f"Published command: {command}")
        time.sleep(1)  # Delay between messages
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    # Stop the network loop and disconnect the client gracefully.
    client.loop_stop()
    client.disconnect()
    print("Disconnected from broker")
