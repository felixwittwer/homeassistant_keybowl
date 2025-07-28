from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# Clock letter grid (10x11)
LETTER_GRID = [
    "ESKISTAFÜNF",
    "ZEHNZWANZIG",
    "DREIVIERTEL",
    "VORFUNKNACH",
    "HALBAELFÜNF",
    "EINSXAMZWEI",
    "DREIPMJVIER",
    "SECHSNLACHT",
    "SIEBENZWÖLF",
    "ZEHNEUNKUHR",
]

WORD_POSITIONS = {
    "ES": (0, 0, 2),
    "IST": (0, 3, 3),
    "FÜNF_MIN": (0, 7, 4),
    "ZEHN": (1, 0, 4),
    "ZWANZIG": (1, 4, 7),
    "VIERTEL": (2, 4, 7),
    "DREIVIERTEL": (2, 0, 11),
    "VOR": (3, 0, 3),
    "NACH": (3, 7, 4),
    "HALB": (4, 0, 4),
    "EIN": (5, 0, 3),
    "EINS": (5, 0, 4),
    "ZWEI": (5, 7, 4),
    "DREI": (6, 0, 4),
    "VIER": (6, 7, 4),
    "FÜNF": (4, 7, 4),
    "SECHS": (7, 0, 5),
    "SIEBEN": (8, 0, 6),
    "ACHT": (7, 7, 4),
    "NEUN": (9, 4, 4),
    "ZEHN_H": (9, 0, 4),
    "ELF": (4, 5, 3),
    "ZWÖLF": (8, 6, 5),
    "UHR": (9, 8, 3),
}

# Font and layout
FONT_SIZE = 22
FONT = ImageFont.load_default()

def get_time_words(hour, minute):
    words = ["ES", "IST"]
    min_rounded = (minute + 2) // 5 * 5
    display_dots = minute % 5

    # Wordclock logic
    if min_rounded == 0:
        words += [hour_word(hour), "UHR"]
    elif min_rounded == 5:
        words += ["FÜNF_MIN", "NACH", hour_word(hour)]
    elif min_rounded == 10:
        words += ["ZEHN", "NACH", hour_word(hour)]
    elif min_rounded == 15:
        words += ["VIERTEL", "NACH", hour_word(hour)]
    elif min_rounded == 20:
        words += ["ZWANZIG", "NACH", hour_word(hour)]
    elif min_rounded == 25:
        words += ["FÜNF_MIN", "VOR", "HALB", hour_word(hour + 1)]
    elif min_rounded == 30:
        words += ["HALB", hour_word(hour + 1)]
    elif min_rounded == 35:
        words += ["FÜNF_MIN", "NACH", "HALB", hour_word(hour + 1)]
    elif min_rounded == 40:
        words += ["ZWANZIG", "VOR", hour_word(hour + 1)]
    elif min_rounded == 45:
        words += ["DREIVIERTEL", hour_word(hour + 1)]
    elif min_rounded == 50:
        words += ["ZEHN", "VOR", hour_word(hour + 1)]
    elif min_rounded == 55:
        words += ["FÜNF_MIN", "VOR", hour_word(hour + 1)]

    return set(words), display_dots

def hour_word(h):
    h = h % 12 or 12
    return {
        1: "EINS",
        2: "ZWEI",
        3: "DREI",
        4: "VIER",
        5: "FÜNF",
        6: "SECHS",
        7: "SIEBEN",
        8: "ACHT",
        9: "NEUN",
        10: "ZEHN_H",
        11: "ELF",
        12: "ZWÖLF"
    }[h]

def generate_wordclock_image():
    now = datetime.now()
    hour, minute = now.hour, now.minute

    active_words, minute_dots = get_time_words(hour, minute)

    image = Image.new('1', (400, 300), 255)
    draw = ImageDraw.Draw(image)

    # Draw grid
    cell_w = 36
    cell_h = 28
    x_off = 10
    y_off = 10

    for y, line in enumerate(LETTER_GRID):
        for x, char in enumerate(line):
            active = any(
                y == pos[0] and x >= pos[1] and x < pos[1] + pos[2]
                for word in active_words if (pos := WORD_POSITIONS.get(word))
            )
            color = 0 if active else 255
            draw.text((x_off + x * cell_w, y_off + y * cell_h), char, font=FONT, fill=color)

    # Draw minute dots in corners
    dot_radius = 5
    dots = [
        (10, 280),
        (390, 280),
        (10, 10),
        (390, 10),
    ]
    for i in range(minute_dots):
        draw.ellipse([
            (dots[i][0] - dot_radius, dots[i][1] - dot_radius),
            (dots[i][0] + dot_radius, dots[i][1] + dot_radius)
        ], fill=0)

    return image

