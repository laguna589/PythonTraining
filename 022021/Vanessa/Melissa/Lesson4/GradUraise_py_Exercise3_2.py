# Exercise 3.1
hours = input('Enter Hours: ')
try:
    hval = int(hours)
except:
    hval = -1

rate = input('Enter Rate: ')
try:
    rval = int(rate)
except:
    rval = -1

if hval < 0 and rval < 0:
    print('Error - Hours and Rate are not valid numbers; Please enter numeric values')
elif hval < 0:
    print('Error - Hours is not a valid number; Please enter numeric value')
elif rval < 0:
    print('Error - Rate is not a valid number; Please enter numeric value')
else:
    if int(hours)<= 40:
        pay = int(hours) * float(rate)
        print('Pay:', pay)
    else :
        pay = (40 * float(rate) + ((int(hours) - 40) * float(rate) * 1.5))
        print('Pay:', pay)
print()
