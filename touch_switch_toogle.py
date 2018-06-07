#!/user/bin/env python 
import RPi.GPIO as GPIO
import time 

# breadboard setup 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# assign pin number for TOUch Switch; pin = 31 GPIO 6
touch_pin = 31

# set Touch Switch pin's mode as input 
GPIO.setup(touch_pin,GPIO.IN)

# create infinite loop that reads Touch switch input 
while True : 
    if GPIO.input(touch_pin) == 0 :
 

    if GPIO.input(touch_pin) == 1:

         
