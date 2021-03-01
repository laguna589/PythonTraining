#!/usr/bin/env python3

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if hours <= 40 :
    pay = rate * hours
else :
    pay = rate * (40 + (hours - 40) * 1.5)

print('Pay:', pay)

