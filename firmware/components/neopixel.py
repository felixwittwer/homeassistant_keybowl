import board
import neopixel
import time

NUM_PIXELS = 9
PIN = board.D16

class NeoPixelStrip:
    def __init__(self):
        self.pixels = neopixel.NeoPixel(PIN, NUM_PIXELS, brightness=0.3, auto_write=False)

    def set_color(self, color):
        for i in range(NUM_PIXELS):
            self.pixels[i] = color
        self.pixels.show()

    def clear(self):
        self.pixels.fill((0, 0, 0))
        self.pixels.show()

    def rainbow_cycle(self, wait=0.05, iterations=5):
        for j in range(256 * iterations):
            for i in range(NUM_PIXELS):
                pixel_index = (i * 256 // NUM_PIXELS) + j
                self.pixels[i] = self.wheel(pixel_index & 255)
            self.pixels.show()
            time.sleep(wait)

    def wheel(self, pos):
        # Generate rainbow colors across 0-255 positions.
        if pos < 85:
            return (pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return (255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return (0, pos * 3, 255 - pos * 3)
