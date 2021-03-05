# Exercise 4.6
def computepay (hval, rval):
    if hval <= 40 :
        pay = hval * rval
    else :
        pay = (40 * rval + ((hval - 40) * rval * 1.5))
    print ('Pay:' , pay)

hours = input('Enter Hours: ')
try:
    hval = float(hours)
except:
    hval = -1
rate = input('Enter Rate: ')
try:
    rval = float(rate)
except:
    rval = -1

if hval < 0 and rval < 0:
    print('Error - Hours and Rates are not valid numbers; Please enter numeric values')
elif hval < 0:
    print('Error - Hours is not a valid number; Please enter a numeric value')
elif rval < 0:
    print('Error - Rates is not a valid number; Please enter a numeric value')
else:
    computepay (hval, rval)
print()
