import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(letter)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self,word_list,num_lives=5):

        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list) 
        self.word_guessed = ['_' for element in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self,letter):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''

        letter = letter.lower()
        if letter in self.word:
            print(f'Good guess! {letter} is in the word')
            for idx,element in enumerate(self.word):
                if element == letter:
                    self.word_guessed[idx] = element
            print(f'You have correctly guessed: {self.word_guessed}')
            #track correct guesses
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {letter} is not in the word.')
            print(f'You have {self.num_lives} lives left.')


    #get valid user input
    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_guess method.
        '''

        guess = input('Please guess a letter: ')
        if not (len(guess) == 1 and guess.isalpha()):
            print ('Invalid letter. Please, enter a single alphabetical character. ')
        elif guess in self.list_of_guesses:
            print('You already tried that letter!')
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
            print(f'Your guesses: {self.list_of_guesses}')
                

def play_game(word_list):
    '''
    This function  will run all the code to run the game as expected.

    Creates an instance of the Hangman class and assigns this to the variable game.
    Controls the flow of the game based on the number of lives a user has left.  
    If the user has remaining lives, another input is requested.
    Inputs are requested until the word is guessed, or lives are used up.
    
    Parameters:
    ----------
    word_list: list
    The list of words from which the hangman word will randomly be chosen.  Passed in when creating the class instance.

    num_lives: int
    Defaulted to 5, refers to the number of incorrect attempts the player is allowed
    '''
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print(f"You lost!The word was {game.word}.")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print(f'Congratulations!  You won! The word is {game.word}.')
            break 

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
