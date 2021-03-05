# Exercise 6.3
# Exercise 6.2
word = input('Enter a lower case word: ')
search = input('Enter a lower case letter in the word to count: ')

def count(word,search):
    num = 0
    for letter in word:
        if letter == search:
            num = num + 1

            print(num)
count(word,search)
print()
