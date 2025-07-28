import spidev
import RPi.GPIO as GPIO
from PIL import Image
import time

DC = 25
RST = 17
BUSY = 19
CS = 8

EPD_WIDTH = 400
EPD_HEIGHT = 300

class EPD:
    def __init__(self):
        self.reset_pin = RST
        self.dc_pin = DC
        self.busy_pin = BUSY
        self.cs_pin = CS
        self.width = EPD_WIDTH
        self.height = EPD_HEIGHT

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.reset_pin, GPIO.OUT)
        GPIO.setup(self.dc_pin, GPIO.OUT)
        GPIO.setup(self.cs_pin, GPIO.OUT)
        GPIO.setup(self.busy_pin, GPIO.IN)

        self.spi = spidev.SpiDev(0, 0)
        self.spi.max_speed_hz = 2000000

        self.init()

    def digital_write(self, pin, value):
        GPIO.output(pin, value)

    def digital_read(self, pin):
        return GPIO.input(pin)

    def delay_ms(self, milliseconds):
        time.sleep(milliseconds / 1000.0)

    def send_command(self, command):
        self.digital_write(self.dc_pin, 0)
        self.digital_write(self.cs_pin, 0)
        self.spi.writebytes([command])
        self.digital_write(self.cs_pin, 1)

    def send_data(self, data):
        self.digital_write(self.dc_pin, 1)
        self.digital_write(self.cs_pin, 0)
        if isinstance(data, list):
            self.spi.writebytes(data)
        else:
            self.spi.writebytes([data])
        self.digital_write(self.cs_pin, 1)

    def wait_until_idle(self):
        while self.digital_read(self.busy_pin) == 0:
            time.sleep(0.1)

    def reset(self):
        self.digital_write(self.reset_pin, 1)
        self.delay_ms(200)
        self.digital_write(self.reset_pin, 0)
        self.delay_ms(2)
        self.digital_write(self.reset_pin, 1)
        self.delay_ms(200)

    def init(self):
        self.reset()
        self.send_command(0x01)  # POWER SETTING
        self.send_data(0x03)
        self.send_data(0x00)
        self.send_data(0x2b)
        self.send_data(0x2b)

        self.send_command(0x06)  # BOOSTER SOFT START
        self.send_data(0x17)
        self.send_data(0x17)
        self.send_data(0x17)

        self.send_command(0x04)  # POWER ON
        self.wait_until_idle()

        self.send_command(0x00)  # PANEL SETTING
        self.send_data(0x3F)

        self.send_command(0x30)  # PLL CONTROL
        self.send_data(0x3C)

        self.send_command(0x61)  # RESOLUTION SETTING
        self.send_data((self.width >> 8) & 0xFF)
        self.send_data(self.width & 0xFF)
        self.send_data((self.height >> 8) & 0xFF)
        self.send_data(self.height & 0xFF)

        self.send_command(0x82)  # VCOM Voltage
        self.send_data(0x28)

        self.send_command(0X50)  # VCOM AND DATA INTERVAL SETTING
        self.send_data(0x97)

    def display_image(self, image: Image.Image):
        # Convert image to 4-level grayscale and then to 2-bit
        image = image.convert("L").resize((self.width, self.height))
        buf = self._image_to_2bit(image)

        self.send_command(0x10)
        self.send_data(buf)

        self.send_command(0x12)  # Display Refresh
        self.wait_until_idle()

    def _image_to_2bit(self, image):
        levels = [0, 85, 170, 255]
        pix = list(image.getdata())
        buf = bytearray()

        for i in range(0, len(pix), 4):
            b = 0
            for j in range(4):
                if i + j >= len(pix):
                    level = 0
                else:
                    gray = pix[i + j]
                    if gray < 64:
                        level = 0b00
                    elif gray < 128:
                        level = 0b01
                    elif gray < 192:
                        level = 0b10
                    else:
                        level = 0b11
                b |= (level << (6 - 2 * j))
            buf.append(b)
        return buf

    def sleep(self):
        self.send_command(0x02)  # POWER OFF
        self.wait_until_idle()
        self.send_command(0x07)  # DEEP SLEEP
        self.send_data(0xA5)

    def clear(self):
        blank = Image.new("L", (self.width, self.height), 255)
        self.display_image(blank)

