# Exercise 7.2

fnam = input('Enter a file name: ')
try:
    fhand = open(fnam, 'r')
except:
    print('File does not exist')
    quit()


count = 0
sum = 0
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    start = line.find(' ')

    count = count + 1
    number = line[start:]
    number = number.strip()
    sum = sum + float(number)

print('Average spam confidence:',sum/count)

print()
