from components.homeassistant import HomeAssistantMQTT

ha_mqtt = HomeAssistantMQTT()

def update_homeassistant(key_db):
    for key_id, status in key_db.items():
        ha_mqtt.publish_discovery(key_id)
        ha_mqtt.publish_key_state(key_id, status)
    ha_mqtt.publish_availability(True)
