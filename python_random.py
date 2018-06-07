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
    if guessed_number == random_number: 
        print "your guessed it"
        break

