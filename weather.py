#weather script
working_dir="/home/pi/Documents/pi-weather-clock/"
weather_conditions_json="weatherconditions.json"
#weather_forecast_json="weatherforecast.json"

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

#LCD SETUP
# Character LCD pin configuration:
lcd_rs        = 27
lcd_en        = 22
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 
                           lcd_columns, lcd_rows, lcd_backlight)

os.chdir(working_dir)

api_file = working_dir + weather_conditions_json

#Clock logic
def Clock_display():
 while(True):
  now = datetime.datetime.now()
  hour = now.hour
  minute = now.minute
  second = now.second
  lcd(ready()
  currenttime="TIME: {}:{}::{}".format(hour,minute,second) 
  lcd.message(currenttime)
  time.sleep(1)

def LCD_disable():
 lcd.clear()
 lcd.set_backlight(0)
 lcd.enable_display(False)
 
def LCD_enable():
 lcd.enable_display(True)
 lcd.clear()
 lcd.home()
 lcd.set_backlight(1)

def LCD_ready():
 lcd.clear()
 lcd.home()
#####################################################

LCD_enable()
LCD_ready()
Clock_display()

#####################################################
gpio.cleanup()

