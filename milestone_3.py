import random

#create word list
word_list = ['mango','apple','pear','coconut','banana']
print(word_list)

#generate a random word from the list
word = random.choice(word_list)
print(word)

#check guess
def check_guess (letter):
    letter = letter.lower()
    if letter in word:
        print(f'Good guess! {letter} is in the word')
    else:
        print(f"Sorry, {letter} is not in the word. Try again.")

#get valid user input
def ask_for_input():
    while True:
        guess = input('Please guess a letter: ')
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)
            break
        else:
            print ('Invalid letter. Please, enter a single alphabetical character. ')
    
ask_for_input()

