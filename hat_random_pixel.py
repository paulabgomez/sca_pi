#!/usr/bin/env python 
from sense_hat import SenseHat
sense = SenseHat()
import time
import random 
i = 0 
while i < 10 
    x = random.randint(0,7)
    y = random.randint(0,7)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
   sense.set_pixel(x, y (r, g, b))
time.sleep(2)
sense.clear()
