from pyembedded.rfid_module.rfid import RFID
import time
import json
from pathlib import Path

DB_PATH = Path("key_states.json")

def load_key_db():
    if DB_PATH.exists():
        with open(DB_PATH, "r") as f:
            return json.load(f)
    return {}

def save_key_db(db):
    with open(DB_PATH, "w") as f:
        json.dump(db, f)

key_db = load_key_db()

rfid = RFID(port='/dev/ttyS0', baud_rate=115200, timeout=1)

def read_tags():
    tag_id = rfid.get_id()
    return {tag_id} if tag_id else set()

def check_keys():
    current_tags = read_tags()
    changes = {}

    for tag in current_tags:
        prev_state = key_db.get(tag)
        if prev_state != "present":
            key_db[tag] = "present"
            changes[tag] = "present"

    for tag in list(key_db):
        if key_db[tag] == "present" and tag not in current_tags:
            key_db[tag] = "absent"
            changes[tag] = "absent"

    if changes:
        save_key_db(key_db)

    return changes

if __name__ == "__main__":
    try:
        while True:
            changes = check_keys()
            if changes:
                print("State changes:", changes)
            time.sleep(5)
    except KeyboardInterrupt:
        print("Exiting...")
