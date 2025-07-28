from components.epaper import EPD
from components.wordclock import generate_wordclock_image

epd = EPD()
epd.init()
image = generate_wordclock_image()
epd.display(image)
epd.sleep()
epd.close()