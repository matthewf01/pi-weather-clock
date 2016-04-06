import time
#!/usr/bin/env python
 
import os
from time import sleep
 
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)

sound_file_path = "/home/pi/Music/test"


# Check current working directory.
# Now change the directory
os.chdir(sound_file_path)
retval = os.getcwd()
print "Current working directory %s" % retval

while True:
    if (GPIO.input(5) == True):
        os.system('mpg123 -q Zelda_Theme.mp3 &')
        print ("Green pressed")
 
    if (GPIO.input(6) == True):
        os.system('mpg123 -q Zelda_Theme.mp3 &')
        print ("Red pressed")
 
    if (GPIO.input(13)== True):
        os.system('mpg123 -q Zelda_Theme.mp3 &')
        print ("Yellow pressed")
        
    if (GPIO.input(19)== True):
        os.system('mpg123 -q Zelda_Theme.mp3 &')
        print ("Blue pressed")
 
    sleep(0.1);