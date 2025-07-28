import time
from threading import Timer

from components.epaper import EPD
from components.wordclock import generate_wordclock_image
from dashboards.dashboard_1 import generate_dashboard
from components.homeassistant import HomeAssistantMQTT
from components.rfid_r200 import check_keys

# Constants
DASHBOARD_DISPLAY_TIME = 30  # seconds

# State
last_tag_seen = None
dashboard_timer = None
is_showing_dashboard = False

# Initialize hardware/services
epd = EPD()
mqtt = HomeAssistantMQTT()

def show_wordclock():
    global is_showing_dashboard
    is_showing_dashboard = False
    image = generate_wordclock_image()
    epd.display(image)

def show_dashboard():
    global is_showing_dashboard, dashboard_timer
    is_showing_dashboard = True
    image = generate_dashboard()
    epd.display(image)

    if dashboard_timer:
        dashboard_timer.cancel()
    dashboard_timer = Timer(DASHBOARD_DISPLAY_TIME, show_wordclock)
    dashboard_timer.start()

def main():
    global last_tag_seen

    print("Starting system...")
    epd.init()
    mqtt.publish_availability(True)

    show_wordclock()

    try:
        while True:
            changes = check_keys()
            if changes:
                for tag_id, state in changes.items():
                    print(f"[KEY] {tag_id} is now {state}")
                    mqtt.publish_discovery(tag_id)
                    mqtt.publish_key_state(tag_id, state)

                    if state == "present" and (tag_id != last_tag_seen or not is_showing_dashboard):
                        last_tag_seen = tag_id
                        show_dashboard()

            time.sleep(1)

    except KeyboardInterrupt:
        print("Shutting down...")

    finally:
        mqtt.disconnect()
        epd.sleep()
        epd.close()

if __name__ == "__main__":
    main()
