# Exercise 3.1
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
if int(hours)<= 40 :
    pay = int(hours) * float(rate)
else :
    pay = (40 * float(rate) + ((int(hours) - 40) * float(rate) * 1.5))
print('Pay:' , pay)
print()
