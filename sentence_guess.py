#!/usr/bin/env python 
from sense_hat import SenseHat
sense = SenseHat()
i = 0
yellow = (255, 255, 0) 
black= (0, 0, 0) 

speed = 0.01
message = "Hello World!"

sense.show_message(message, speed, text_colour=yellow, back_colour=black)
user_guess = raw_input("What is your guess?")

while i < 10 :
    i = i +1

if user_guess == message :
    print "Your Guess is correct!"

if user_guess != message:
    print "Your Guess is not correct!"
    
    speed = 0.05
    message = "Hello World!"

    sense.show_message(message, speed, text_colour=yellow,  back_colour=black)

    user_guess = raw_input("What is your guess?")

    if user_guess == message :
        print "Your Guess is correct!"

    if user_guess != message:
        print "Your Guess is not correct!"
        
        speed = 0.05
        message = "Hello World!"

        sense.show_message(message, speed, text_colour=yellow,  back_colour=black)

        user_guess = raw_input("What is your guess?")

        if user_guess == message: 
            print "Your guess is correct!"

        if user_guess != message:
            print "Your guess is not correct!"
    

sense.clear()
