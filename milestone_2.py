import random

#create word list
word_list = ['mango','apple','pear','coconut','banana']
print(word_list)

#generate a random word from the list
word = random.choice(word_list)
print(word)

#get user input
guess = input('Please enter a letter: ')

if len(guess) == 1 and guess.isalpha():
    print ('Good guess!')
else:
    print ('Oops! That is not a valid input')

