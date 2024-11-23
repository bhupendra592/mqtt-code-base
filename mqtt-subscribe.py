import paho.mqtt.client as mqtt
from constants import BROKER, PORT, TOPIC_SUB, CLIENT_ID_SUB, KEEP_ALIVE

# Simulating a home automation system state
home_state = {
    "living_room_light": "OFF",
    "kitchen_light": "OFF",
    "bedroom_light": "OFF",
    "thermostat": 22,  # Default temperature
}

# Callback triggered when the client connects to the broker.
def on_connect(client, userdata, flags, rc):
    """
    client: MQTT client instance
    userdata: Custom data passed to the client
    flags: Connection flags sent by the broker
    rc: Connection result code (0 indicates successful connection)
    """
    if rc == 0:
        print("Subscriber connected to broker")
        client.subscribe(TOPIC_SUB)
        print(f"Subscribed to topic: {TOPIC_SUB}")
    else:
        print(f"Subscriber connection failed with code {rc}")

# Callback triggered when a message is received on a subscribed topic.
def on_message(client, userdata, msg):
    """
    client: MQTT client instance
    userdata: Custom data passed to the client
    msg: Message instance containing topic and payload data
    """
    device_state = userdata  # Reference to the shared home state
    payload = msg.payload.decode()
    print(f"Message received on topic {msg.topic}: {payload}")

    # Update device state based on received message
    try:
        command = eval(payload)  # Example payload: {"device": "living_room_light", "state": "ON"}
        device = command["device"]
        state = command["state"]
        if device in device_state:
            device_state[device] = state
            print(f"Updated {device} to {state}")
        else:
            print(f"Unknown device: {device}")
    except Exception as e:
        print(f"Error processing message: {e}")

# Initialize MQTT client with a unique client ID for the subscriber.
client = mqtt.Client(CLIENT_ID_SUB, userdata=home_state)  # Pass home_state as userdata

# Attach callback functions for connection and message handling.
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker using the specified address and port.
try:
    client.connect(BROKER, PORT, KEEP_ALIVE)
except Exception as e:
    print(f"Could not connect to broker: {e}")
    exit(1)

# Start the MQTT network loop to process incoming and outgoing messages.
client.loop_forever()
