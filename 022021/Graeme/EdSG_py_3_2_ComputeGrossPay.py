#!/usr/bin/env python3

hours = 0.0
try :
    hours = float(input('Enter Hours: '))
except :
    print('Error, please enter numeric input')
    exit(-1)

rate = 0.0
try :
    rate = float(input('Enter Rate: '))
except :
    print('Error, please enter numeric input')
    exit(-1)

if hours <= 40 :
    pay = rate * hours
else :
    pay = rate * (40 + (hours - 40) * 1.5)

print('Pay:', pay)

