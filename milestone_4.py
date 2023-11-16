
import random

class Hangman :
    # class constructor
    def __init__(self, word_list, num_lives = 5):
        
        #attributes
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len([unique_letter for unique_letter in set(list(self.word) + self.word_guessed) if unique_letter.isalpha()])           #TODO I suspect the above needs to be nailed on to calculate this correctly
                            # 1. convert the random word into a list of each string - list(self.word)
                            # 2. we should now have two lists, i.e one is list(self.word) ['f','r','u','i','t'] and the other is self.word_guessed ['_','_','_','_','_',]
                            # 3. now let's combine them to give us a single list that is unique and contains just alphabetical characters
                            # 4. uniquemerged_set = set(list(self.word) + self.word_guessed)
                            # 5. however, word_guessed contains special characters, you will need to filter this out
                            # 6. uniquemerged_set = [unique_letter for unique_letter in set(list(self.word) + self.word_guessed) if unique_letter.isalpha()]
                            # 7. and this should produce a list of unique letters that have not been guessed yet! Add the len function and we have what we're after!
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    
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