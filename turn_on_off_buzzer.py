#!/user/bin/env python
# THis script turns the passice buzzer on and off

import RPi.GPIO as GPIO 
import time 

# breadboard setup 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# assign pin number for Passive Buzzer ; pin 32 = GPIO 12 
buzz_pin = 32

# set Passive Buzzer pin's mode as output 
GPIO.setup(buzz_pin, GPIO.OUT)

#create Buzz function and set initial sound frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin, 1000)

#change frequency and start passive buzzer using buzz functiuon with 50% duty fo r1 second
Buzz.ChangeFrequency(2000)
Buzz.start(50)
time.sleep(1)
Buzz.stop()


#reser GPIO resourcess used by script
GPIO.cleanup()
