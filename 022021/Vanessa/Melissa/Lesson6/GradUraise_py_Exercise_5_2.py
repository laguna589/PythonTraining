# Exercise 5.2
count = 0
sum = 0.0
lar = None
small = None

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break

    try:
        nval = float(num)
    except:
        print('Invalid input')
        continue

    count = count + 1
    sum = sum + nval

    if lar is None:
        lar = nval
    elif nval > lar:
        lar = nval

    if small is None:
        small = nval
    elif nval < small:
        small = nval

print('Sum:', sum, 'Count:', count, 'Smallest:', small, 'Largest:', lar)
print()
