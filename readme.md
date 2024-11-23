# IoT Home Automation with MQTT

This project demonstrates a basic implementation of an IoT home automation system using MQTT. It includes a **Subscriber** for monitoring device statuses and a **Publisher** for sending control commands.

Ref : https://pypi.org/project/paho-mqtt/
---

## Features

### Subscriber
- **Topic**: `home/automation/devices/status`
- **Functionality**:
  - Listens to device status updates.
  - Example message: `{"device": "living_room_light", "state": "ON"}`
  - Updates a shared `home_state` dictionary to maintain the current state of all devices.

### Publisher
- **Topic**: `home/automation/devices/control`
- **Functionality**:
  - Sends control commands to devices.
  - Users interact via a menu to send commands like turning lights on/off or adjusting the thermostat.

---

## State Management with `userdata`
- **Script**: `subscriber.py`
- **Usage**:
  - The `userdata` parameter is utilized to share the `home_state` dictionary across callback functions.
  - This ensures centralized state management for all connected devices.

---

## Real-World Use Case
This implementation showcases how MQTT can be leveraged for:
- **Device state management**: Keeping a consistent record of device states.
- **IoT automation**: Enabling interactive control and status updates in a smart home setup.

---

## Get Started
1. Clone the repository.
2. Install the required MQTT library:
   ```bash
   pip install paho-mqtt
