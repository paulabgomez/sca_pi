#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time 

sense.show_letter("H", (255, 54, 45))
time.sleep(1)
sense.show_letter("I", (32, 65, 123))
time.sleep(1)
sense.show_letter("!", (255, 154, 76))
time.sleep(1)
sense.clear()
