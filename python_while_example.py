x = int(raw_input("Enter an integer:  (> 1):"))
print 'x = ' , x
# Get an integer > 1 from user
while x < 2:
    x = int(raw_input("Enter an integer (> 1): "))
    print 'x = ' , x

# print i and i*i for 1<= 1 < x
i = 1
while i < x:
    print i, ' ' , i * i 
    i = i + 1
