#!/usr/bin/env python
import time
import signal
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw # https://pillow.readthedocs.io/en/3.1.x/reference/index.html

class Screen:
    """Wrapper around the Gfx HAT"""
    def __init__(self):
        # led_states = [False for _ in range(6)]
        self.led_brightness = 127
        self.width, self.height = lcd.dimensions()
        self.image = Image.new('P', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.truetype(fonts.FredokaOne, 20)
        self.fontLine2 = ImageFont.truetype(fonts.PressStart2P, 10)
        self.line1 = ""
        self.line2 = ""


    def flash_buttons(self):
        self.flash_anti_clockwise()
        self.flash_clockwise()

    def flash_anti_clockwise(self):
        for x in range(6):
            self.toggle_led(x, 0.1)

    def flash_clockwise(self):
        for x in range(5,-1,-1):
            self.toggle_led(x, 0.1)

    def toggle_led(self, led_no, sleep_duration):
        touch.set_led(led_no, 1)
        time.sleep(sleep_duration)
        touch.set_led(led_no, 0)

    def flash_backlight(self):
        backlight.set_all(255, 255, 255)
        backlight.set_all(0, 0, 0)
        backlight.show()

    def display(self, line1, line2):
        lcd.contrast(40)
        backlight.set_all(self.led_brightness, self.led_brightness, self.led_brightness)
        backlight.show()
        self.draw.text((0, 1), line1, 1, self.font)
        self.draw.text((0, 30), line2, 1, self.fontLine2)
        self.w, self.h = self.font.getsize(self.line1)
        self.x = (self.width - self.w) // 2
        self.y = (self.height - self.h) // 2

        for self.x in range(128):
            for self.y in range(64):
                pixel = self.image.getpixel((self.x, self.y))
                lcd.set_pixel(self.x, self.y, pixel)
        lcd.show()

    # TODO had trouble clearing the screen so this is not pretty but works - REFACTOR ME!
    def clear(self):
        self.width, self.height = lcd.dimensions()
        self.image = Image.new('P', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.truetype(fonts.FredokaOne, 20)
        self.fontLine2 = ImageFont.truetype(fonts.PressStart2P, 10)
        self.line1 = ""
        self.line2 = ""
        lcd.contrast(40)
        backlight.set_all(self.led_brightness, self.led_brightness, self.led_brightness)
        backlight.show()
        self.draw.text((0, 1), self.line1, 1, self.font)
        self.draw.text((0, 30), self.line2, 1, self.fontLine2)
        self.w, self.h = self.font.getsize(self.line1)
        self.x = (self.width - self.w) // 2
        self.y = (self.height - self.h) // 2

        for self.x in range(128):
            for self.y in range(64):
                pixel = self.image.getpixel((self.x, self.y))
                lcd.set_pixel(self.x, self.y, pixel)
        lcd.show()

    def turn_off(self):
        self.clear()
        lcd.contrast(0)
        backlight.set_all(0,0,0)
        lcd.show()
        backlight.show()

#screen = Screen()
#screen.display("hello", "world")
#screen.turn_off()