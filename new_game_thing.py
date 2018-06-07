import random 
i = 0
random_number = random.randint(1,10)
while i < 10:
    i = i +1
    guessed_number = int(raw_input("Guess and Integer (between 1 and 10): "))
 
    if guessed_number != random_number:
        print "Your guess was not correct"
        if guessed_number > random_number:
            print "Your guess is too high"
        if guessed_number < random_number:
            print "Your guess is too low"
        import RPi.GPIO as GPIO 
        import time 
        # breadboard setup 
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        # assign pin number for Passive Buzzer ; pin 32 = GPIO 12 
        buzz_pin = 32
        GPIO.setup(buzz_pin, GPIO.OUT)

        #create Buzz function and set initial sound frequency to 1000 Hz
        Buzz = GPIO.PWM(buzz_pin, 1000)

        #change frequency and start passive buzzer using buzz functiuon with 50% duty fo r1 second
        Buzz.ChangeFrequency(440)
        Buzz.start(50)
        time.sleep(1)
        Buzz.stop()


        #reser GPIO resourcess used by script
        GPIO.cleanup()
        
    if guessed_number == random_number: 
        import RPi.GPIO as GPIO
        import time

        # breadboard setup
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        # assign pin number for Auto Flash LED ; pin 11 = GPIO 17 
        led_pin = 11

        # set Auto Flash LED pin's mode as output 
        GPIO.setup(led_pin, GPIO.OUT)

        # turn on Auto Flash LED
        GPIO.output(led_pin,True)
        time.sleep(5)

        # turn off Auto Flash LED 
        GPIO.output(led_pin, False)

        # reset GPIO resources used by script 
        GPIO.cleanup()
        print "your guessed it"
        break

