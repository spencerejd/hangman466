
import random

class Hangman :
    # class constructor
    def __init__(self, word_list, num_lives = 5):
        
        #attributes
        self.word = ''
        self.word_guessed = [''] * len(self.word)       #   I suspect this needs additional functionality to take in the word that is guessed and replace the '_'. Index?
        self.num_letters =                  #TODO I suspect the above needs to be nailed on to calculate this correctly
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def random_word_selector(self):
        '''
        This function selects a random word from a given list of words

        The purpose of this function is to select a random word from the list variable given to the function.
        The word is selected using the random.choice function imported from the random module
        '''
        return random.choice(self.word_list)

    
    def ask_for_input(list_of_words) :
        '''
        This function asks for a character input to compare with a random word

        The purpose of this function is to randomly select a word from a list given as a parameter. 
        The user is also asked to provide a single alphabetical character input and the check_guess 
        function is called with the input and randomly selected word as variables.
        '''
        
        while True :
        guess = input('Please guess a single letter: ')
        if len(guess) == 1 and guess.isalpha() :
            break
        print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess, random_word)