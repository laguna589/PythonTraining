# Exercise 8.1

fnam = input('Enter a file name: ')

try:
    fhand = open(fnam)
except:
    print('File does not exist')
    quit()

for line in fhand:
    print(line)
    continue

print()
