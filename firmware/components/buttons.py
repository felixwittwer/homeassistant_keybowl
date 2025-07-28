import RPi.GPIO as GPIO
import time

COL_PINS = [20, 21]
ROW_PINS = [5, 6, 33]

KEY_MAP = {
    (0, 0): "BTN_1",
    (0, 1): "BTN_2",
    (0, 2): "BTN_3",
    (1, 0): "BTN_4",
    (1, 1): "BTN_5",
    (1, 2): "BTN_6",
}

class ButtonMatrix:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        # Setup column pins as outputs and set high
        for pin in COL_PINS:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)

        # Setup row pins as inputs with pull-ups
        for pin in ROW_PINS:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.last_state = set()

    def scan(self):
        pressed = set()
        for col_idx, col_pin in enumerate(COL_PINS):
            GPIO.output(col_pin, GPIO.LOW)
            time.sleep(0.01)  # debounce settle time

            for row_idx, row_pin in enumerate(ROW_PINS):
                if GPIO.input(row_pin) == 0:  # button pressed
                    pressed.add(KEY_MAP[(col_idx, row_idx)])

            GPIO.output(col_pin, GPIO.HIGH)
        return pressed

    def detect_changes(self):
        current = self.scan()
        pressed = current - self.last_state
        released = self.last_state - current
        self.last_state = current
        return pressed, released

    def cleanup(self):
        GPIO.cleanup()
