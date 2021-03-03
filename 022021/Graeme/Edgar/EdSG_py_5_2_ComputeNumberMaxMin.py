#!/usr/bin/env python3

# Exercise 5.1:
# Write a program which repeatedly reads numbers until the user enters
# “done”. Once “done” is entered, print out the total, count, and
# average of the numbers. If the user enters anything other than a number,
# detect their mistake using try and except and print an error message and
# skip to the next number.

line = ''
number = 0.0

count = 0
minimum = None
maximum = None

while (line != 'done') :
    try :
        line = input('Enter a number: ')

        if line == 'done' :
            break
        else :
            number = int(line)

            if minimum is None or number < minimum :
                minimum = number

            if maximum is None or number > maximum :
                maximum = number

            count += 1
    except :
        print('Invalid input')
        continue

print('Maximum is', maximum)
print('Minimum is', minimum)

