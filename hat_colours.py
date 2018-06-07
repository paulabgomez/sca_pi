#!/usr/bin/env python 
from sense_hat import SenseHat
sense = SenseHat()

# use RGB values to define colors 
yellow = (0, 0, 255)
blue = (0, 0, 0)

speed = .1

message = "OoF"

sense.show_message (message, speed, text_colour=yellow, back_colour=blue)

sense.clear()
