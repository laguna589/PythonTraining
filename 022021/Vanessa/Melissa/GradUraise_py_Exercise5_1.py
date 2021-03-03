# Exercise 5.1
count = 0
sum = 0.0

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    else:
        try:
            nval = float(num)
        except:
            nval = None
            print('Invalid input')

    if nval is None:
        continue
    else:
        count = count + 1
        sum = sum + nval

print(sum, count, sum / count)
print()
