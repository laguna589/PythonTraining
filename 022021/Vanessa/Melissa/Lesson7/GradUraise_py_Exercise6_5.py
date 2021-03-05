# Exercise 6.5
str = 'X-DSPAM-Confidence: 0.8475 '
lspc = str.find(':')
num = str[lspc+1:]
print(float(num))
print()
