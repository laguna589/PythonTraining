fhand = open('romeo.txt')
unique = []

for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in unique : continue
        unique.append(word)
unique.sort()
print(unique)
