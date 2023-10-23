import random

class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list) 
        self.word_guessed = ['_' for element in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        #testing : print(self.word, self.word_guessed,self.num_letters,self.list_of_guesses)

    #check guess
    def __check_guess(self,letter):
        letter = letter.lower()
        if letter in self.word:
            print(f'Good guess! {letter} is in the word')
            for element in self.word:
                if element == letter:
                    self.word_guessed[self.word.find(element)] = element
                    print(self.word_guessed)
            self.num_letters -= 1
            print(f'number of letters to guess: {self.num_letters}')
        else:
            self.num_lives -= 1
            print(f'Sorry, {letter} is not in the word.')
            print(f'You have {self.num_lives} lives left.')


    #get valid user input
    def ask_for_input(self):
        while True:
            guess = input('Please guess a letter: ')
            if not (len(guess) == 1 and guess.isalpha()):
                print ('Invalid letter. Please, enter a single alphabetical character. ')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(f'list of guesses: {self.list_of_guesses}')
                

letsplay = Hangman(['apple','banana','mango','pear','pineapple'],5)
letsplay.ask_for_input()
