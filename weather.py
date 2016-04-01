#weather script
working_dir="/home/pi/Documents/pi-weather-clock/"


import json
import time
import math
import datetime
import os
 
#imports modules for 16x2 character LCD
import Adafruit_CharLCD as LCD

''' uncomment when using OLED
#imports modules for OLED display
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Image
import ImageDraw
import ImageFont
'''

# Character LCD pin configuration:
lcd_rs        = 27
lcd_en        = 22
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4

os.chdir("/home/pi/Documents/pi-weather-clock/")

api_file = "/home/pi/weatherunderground.json"
