from PIL import Image, ImageDraw, ImageFont
import json
import os
from components.homeassistant import get_state
from components import tagreader

KEY_DB_PATH = "db/keys.json"
DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 300
MARGIN = 10
LINE_SPACING = 24

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_SIZE = 20
SMALL_FONT_SIZE = 16

def load_registered_keys():
    try:
        with open(KEY_DB_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def generate_dashboard():
    image = Image.new("L", (DISPLAY_WIDTH, DISPLAY_HEIGHT), 255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    small_font = ImageFont.truetype(FONT_PATH, SMALL_FONT_SIZE)

    keys = load_registered_keys()
    key_states = tagreader.key_db

    y = MARGIN
    draw.text((MARGIN, y), "Key Presence:", font=font, fill=0)
    y += LINE_SPACING

    if not keys:
        draw.text((MARGIN, y), "No keys registered.", font=small_font, fill=128)
        y += LINE_SPACING
    else:
        for tag_id, key_info in keys.items():
            name = key_info.get("name", f"Key {tag_id[-4:]}")
            state = key_states.get(tag_id, "absent")
            fill = 0 if state == "present" else 128
            draw.text((MARGIN + 10, y), f"{name}: {state}", font=small_font, fill=fill)
            y += LINE_SPACING

    # Weather at the bottom
    weather_state = get_state("weather.home")
    if weather_state:
        weather_text = f"{weather_state['state'].capitalize()}"
        attrs = weather_state.get("attributes", {})
        temp = attrs.get("temperature")
        cond = attrs.get("condition")
        if temp is not None:
            weather_text += f", {temp}°C"
        if cond:
            weather_text += f" ({cond})"
    else:
        weather_text = "Weather unavailable"

    draw.line([(0, DISPLAY_HEIGHT - 45), (DISPLAY_WIDTH, DISPLAY_HEIGHT - 45)], fill=200)
    draw.text((MARGIN, DISPLAY_HEIGHT - 40), f"Weather: {weather_text}", font=small_font, fill=0)

    return image
