# Exercise 8.6
numlist = []

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break

    try:
        nval = float(num)
    except:
        print('Invalid input')
        continue

    numlist.append(nval)

print('Maximum: ', max(numlist))
print('Minium: ', min(numlist))
print()
