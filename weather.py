#!/usr/bin/env python
#weather script

import json
import time
import math
import RPi.GPIO as GPIO
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

#set paths to files
working_dir="/home/pi/Documents/pi-weather-clock/"
weather_conditions_json="weatherconditions.json"
#weather_forecast_json="weatherforecast.json"
conditions_api_file = working_dir + weather_conditions_json
#forecast_api_file = working_dir + weather_forecast_json

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

#JSON parsing
def read_json_conditions():
  json_cond_text = open(conditions_api_file)
  parsed_cond_json = json.load(json_cond_text)
  global weather
  global tempf
  global weatherdisplay
  weather = parsed_cond_json['current_observation']['weather']
  tempf = str(parsed_cond_json['current_observation']['temp_f'])
  obs_time=str(parsed_cond_json['current_observation']['observation_time'])
  weatherdisplay=("{} -- {}`F -- {}".format(weather,tempf,obs_time))
  timenow = time.strftime("%X")
  datenow = time.strftime("%x")
  print("{} {} READ FILE: {}".format(timenow,datenow,conditions_api_file))
  print("{} -- {}`F -- {}".format(weather,tempf,obs_time))
  global weather_aging
  weather_aging=0
  return

#####################################################

#initialize everything
print("initializing...")
LCD_enable()
LCD_ready()
lcd.set_cursor(0,1)
lcd.message("Checking weather")
read_json_conditions()
weather_aging_refresh=60 #how many S to re-read the weather JSON file. JSON file pulled in a configurable interval in get-weather-json.py
weather_aging=weather_aging_refresh -2

def main():
 while (True):
 # Main program block
  global weather_aging
  weather_aging=weather_aging + 1
  if weather_aging > weather_aging_refresh:
   read_json_conditions()
   LCD_ready()
   lcd.set_cursor(0,1)
   lcd.message(weatherdisplay)
   break
  else:
   #LCD_ready()
   lcd.set_cursor(0,0)
   lcd.message((datetime.datetime.now().strftime('%b %d  %I:%M %p')))
   time.sleep(1)


#if __name__ == '__main__':

while (True):
 main()

#####################################################


