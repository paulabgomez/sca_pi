#!/user/bin/env python
#This script turns the passive buzzer on and off using two sound frequencies

import RPi.GPIO as GPIO
import time 

# Breadboard setup 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# assign pin number for passive buzzer; pin = 32 GPIO 12
buzz_pin = 32

# set Passive buzzer pin's mode as output 
GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)

def buzz (freq) : 
    Buzz.ChangeFrequency(freq)
    Buzz.start(50)
    time.sleep(.5)
    Buzz.stop()
   
buzz (392)
buzz (350.23)
buzz (392)
buzz (350.23)
buzz (392)
buzz (293.66)
buzz (349)
buzz (280)
buzz (261.63)



GPIO.cleanup()
