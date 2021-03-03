def computepay (hours, rate):
    if float(hours)<= 40 :
        pay = int(hours) * float(rate)
    else :
        pay = (40 * float(rate) + ((int(hours) - 40) * float(rate) * 1.5))
    print ('Pay:' , pay)

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
computepay (hours, rate)
print()
