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
sound_file_1="Zelda_Theme.mp3"

# Check current working directory.
retval = os.getcwd()
print "Current working directory %s" % retval
# Now change the directory
os.chdir( path )

while True:
    if (GPIO.input(5) == False):
        os.system('mpg123 -q sound_file_1 &')
 
    if (GPIO.input(6) == False):
        os.system('mpg123 -q sound_file_1 &')
 
    if (GPIO.input(13)== False):
        os.system('mpg123 -q sound_file_1 &')
        
    if (GPIO.input(19)== False):
        os.system('mpg123 -q sound_file_1 &')
 
    sleep(0.1);
