#!/usr/bin/env python3

def compute_pay(hours, rate) :
    pay = 0.0
    
    if hours <= 40 :
        pay = rate * hours
    else :
        pay = rate * (40 + (hours - 40) * 1.5)
    
    return pay


h = 0.0
try :
    h = float(input('Enter Hours: '))
except :
    print('Error, please enter numeric input')
    exit(-1)

r = 0.0
try :
    r = float(input('Enter Rate: '))
except :
    print('Error, please enter numeric input')
    exit(-1)

print('Pay:', compute_pay(h, r))

