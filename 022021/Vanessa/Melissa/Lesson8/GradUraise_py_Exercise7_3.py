# Exercise 7.3

fnam = input('Enter a file name: ')
if fnam == "na na boo boo":
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    quit()
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
    sum = float(sum) + float(number)

print('Average spam confidence:',sum/count)

print()
