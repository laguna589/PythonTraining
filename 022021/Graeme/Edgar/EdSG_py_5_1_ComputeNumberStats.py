#!/usr/bin/env python3

# Exercise 5.1:
# Write a program which repeatedly reads numbers until the user enters
# “done”. Once “done” is entered, print out the total, count, and
# average of the numbers. If the user enters anything other than a number,
# detect their mistake using try and except and print an error message and
# skip to the next number.

line = ''
number = 0.0

total = 0
count = 0
average = None

while (line != 'done') :
    try :
        line = input('Enter a number: ')

        if line == 'done' :
            break
        else :
            number = float(line)

            total += number
            count += 1
    except :
        print('Invalid input')
        continue

if total > 0 and count > 0 :
    average = total / count

print(total, count, average)

