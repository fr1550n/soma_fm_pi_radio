#!/usr/bin/env python
import signal
import time
from PIL import Image, ImageFont, ImageDraw
from gfxhat import touch, lcd, backlight, fonts

lcd.contrast(40)
def flash():
    for i in range(0, 256, 1):
        print( i), backlight.set_all(i, 0, 0)
        time.sleep(0.001)
        backlight.show()
    for i in range(255, 0, -1):
        print(i), backlight.set_all(i, 0, 0)
        time.sleep(0.001)
        backlight.show()

flash()
