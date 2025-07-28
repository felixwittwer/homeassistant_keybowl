import paho.mqtt.client as mqtt
import requests
import json
import os

# MQTT Setup
MQTT_BROKER = os.getenv("MQTT_BROKER", "your_mqtt_broker_ip_or_hostname")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USERNAME = os.getenv("MQTT_USERNAME", "your_username")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", "your_password")
MQTT_BASE_TOPIC = "home/keybowl"

# Home Assistant REST API Setup
HASS_URL = os.getenv("HASS_URL", "http://homeassistant.local:8123/api")
HASS_TOKEN = os.getenv("HASS_TOKEN", "your_long_lived_access_token")

HEADERS = {
    "Authorization": f"Bearer {HASS_TOKEN}",
    "Content-Type": "application/json"
}

class HomeAssistantMQTT:
    def __init__(self):
        self.client = mqtt.Client("keybowl_pi")
        self.client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        self.client.connect(MQTT_BROKER, MQTT_PORT, 60)
        self.client.loop_start()

    def publish_key_state(self, key_id, state):
        topic = f"{MQTT_BASE_TOPIC}/key/{key_id}"
        self.client.publish(topic, state, retain=True)

    def publish_discovery(self, key_id, name=None):
        sensor_name = name or f"Key {key_id[-4:]}"
        config_topic = f"homeassistant/binary_sensor/keybowl_{key_id}/config"
        config_payload = {
            "name": sensor_name,
            "state_topic": f"{MQTT_BASE_TOPIC}/key/{key_id}",
            "payload_on": "present",
            "payload_off": "absent",
            "unique_id": f"keybowl_{key_id}",
            "device_class": "presence",
            "availability_topic": f"{MQTT_BASE_TOPIC}/status",
        }
        self.client.publish(config_topic, json.dumps(config_payload), retain=True)

    def publish_availability(self, available=True):
        self.client.publish(f"{MQTT_BASE_TOPIC}/status", "online" if available else "offline", retain=True)

    def disconnect(self):
        self.publish_availability(False)
        self.client.loop_stop()
        self.client.disconnect()

def get_state(entity_id):
    try:
        url = f"{HASS_URL}/states/{entity_id}"
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f"HA REST error {resp.status_code} for {entity_id}")
            return None
    except Exception as e:
        print("HA REST request failed:", e)
        return None
