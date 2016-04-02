#weather script
print("starting...")
import json
import time
import math
import datetime
import os
import threading
from threading import Thread
 
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
os.chdir(working_dir)


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
 
#Clock logic
def Clock_display():
 while(True):
  now = datetime.datetime.now()
  hour = now.hour
  minute = now.minute
  second = now.second
  global currenttime
  currenttime="TIME: {}:{}::{}".format(hour,minute,second) 
  # print(currenttime)
  time.sleep(1)

'''
#JSON parsing
def read_json_conditions():
  while(True):
   json_cond_text = open(conditions_api_file)
   parsed_cond_json = json.load(json_cond_text)
   weather = parsed_cond_json['current_observation']['weather']
   tempf = str(parsed_cond_json['current_observation']['temp_f'])
   print("{} -- READ FILE: {}".format(currenttime,conditions_api_file))
   print("{} -- {}degF".format(weather,tempf))
   time.sleep(60)
'''

#write to display
def lcd_show_data():
 while(True):
  #LCD_ready()
  #lcd.set_cursor(0,1)
  lcd.message(currenttime)
  print ("wrote to lcd")
  #lcd.set_cursor(1,1)
#  lcd.message("{},{}degF`".format(weather,tempf))
  time.sleep(1)
#####################################################

time.sleep(3)
LCD_enable()
LCD_ready()

if __name__ == '__main__':
    Thread(target = Clock_display).start()
    Thread(target = lcd_show_data).start()
#read_json_conditions()

#####################################################


