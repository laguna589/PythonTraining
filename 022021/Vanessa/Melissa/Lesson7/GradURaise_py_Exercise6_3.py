# Exercise 6.3
word = input('Enter a lower case word: ')
search = input('Enter a lower case letter in the word to count: ')
count = 0
for letter in word:
    if letter == search:
        count = count + 1
print(count)
