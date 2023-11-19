
import random

class Hangman :
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
        word (str) :
        the word to be guessed from a provided list
        word_guessed (list) :
        a list of the letters of the word, with _ for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        num_letters (int) :
        number of UNIQUE letters in the word that have not been guessed yet
        num_lives (int) :
        number of lives left to play the game
        word_list (list) :
        the provided list of words
        list_of_guesses (list) :
        a list of the guesses that have been attempted

        Methods:
    -------
    _check_guess_(guess)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives = 5):
        
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len([unique_letter for unique_letter in set(list(self.word) + self.word_guessed) if unique_letter.isalpha()])
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    
    def ask_for_guess(self) :
        '''
        This function is used to request user input of a single alphabetical character.

        Returns:
        It returns the input to the _check_guess_ function and appends the input to a list.
        '''
        while True :
            print("New Round")
            guess = input('Please guess a single letter: ')
            guess = guess.lower()
            if guess in self.list_of_guesses :
                print("You already tried that letter!")
            elif len(guess) != 1 or not guess.isalpha() :
                print("Invalid letter. Please, enter a single alphabetical character.")
            else :
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


    def check_guess(self, guess) :
        '''
        This function is used to return whether a guessed character is found in the word

        Args:
            guess (str) : the letter guessed.
        
        Returns:
            list : a list of the letters found in the word that have been guessed
            str: confirmation if the guess is or is not in the word
            str: the number of lives remaining

        '''    

        if guess in self.word :
            print(f"Good guess! {guess} is in the word.")

            for idx, letter in enumerate(self.word) :
                if letter == guess :
                    self.word_guessed[idx] = guess

            self.num_letters -= 1

        else :
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
        
        print("Hangman:", ''.join(self.word_guessed))


def play_game(word_list) :
    game = Hangman(word_list, num_lives=5)
    while True :
        if game.num_lives == 0 :
            print('You lost!')
            break
        elif game.num_letters > 0 :
            game.ask_for_guess()
        elif game.num_lives != 0 and game.num_letters <= 0 :
            print('Congratulations. You won the game!')
            break


favourite_fruit_list = ['Banana', 'Clementines', 'Tomato', 'Grape', 'Melon', 'Strawberries', 'Apple', 'Pineapple', 'Cantaloupe', 'Plantain', 'Pear',]
play_game(favourite_fruit_list)


