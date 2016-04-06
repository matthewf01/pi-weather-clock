import time
#!/usr/bin/env python
 
import os
from time import sleep
 
import RPi.GPIO as GPIO

#buttons 
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
#LEDs
GPIO.setup(16,GPIO.OUT) #BLUE
GPIO.output(16,0)
GPIO.setup(20,GPIO.OUT) #GREEN
GPIO.output(20,0)
GPIO.setup(21,GPIO.OUT) #RED
GPIO.output(21,0)

# 010 purple
# 101 green
# 001 teal
# 110 red
# 011 blue
# 000 white
# 100 yellow
# 111 off


sound_file_path = "/home/pi/Music/test"
sound_file_zelda ="Zelda_Theme.mp3"

# Check current working directory.
# Now change the directory
os.chdir(sound_file_path)
retval = os.getcwd()
print "Current working directory %s" % retval


while True:
 '''
    request=raw_input("RGB-->")
    if (len(request) == 3):
     GPIO.output(16,int(request[0]))
     GPIO.output(20,int(request[1]))
     GPIO.output(21,int(request[2]))
 '''
    if (GPIO.input(5) == True):
        #os.system('mpg123 -q sound_file_zelda &')
        print ("Green pressed")
        GPIO.output(16,1)
        GPIO.output(20,0)
        GPIO.output(21,1)
        time.sleep(1)
 
    if (GPIO.input(6) == True):
        #os.system('mpg123 -q Zelda_Theme.mp3 &')
        print ("Red pressed")
        GPIO.output(16,1)
        GPIO.output(20,1)
        GPIO.output(21,0)
        time.sleep(1)
 
    if (GPIO.input(13)== True):
        #os.system('mpg123 -q Zelda_Theme.mp3 &')
        print ("Yellow pressed")
        GPIO.output(16,1)
        GPIO.output(20,0)
        GPIO.output(21,0)
        time.sleep(1)
        
    if (GPIO.input(19)== True):
        #os.system('mpg123 -q Zelda_Theme.mp3 &')
        print ("Blue pressed")
        GPIO.output(16,0)
        GPIO.output(20,1)
        GPIO.output(21,1)
        time.sleep(1)
 
    sleep(0.1);
