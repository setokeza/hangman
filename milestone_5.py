import random

class Hangman:
    def __init__(self,word_list,num_lives=5):

        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list) 
        self.word_guessed = ['_' for element in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    #check guess
    def check_guess(self,letter):
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
    # Play the game
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
