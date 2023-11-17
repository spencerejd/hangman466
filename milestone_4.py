
import random

favourite_fruit_list = ['Banana', 'Easy Peelers', 'Tomato', 'Grape', 'Honeydew melon']

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

    
    def check_guess(self, guess) :
        '''
        This function checks if a guessed character is found in a word

        The purpose of this function is to complete a check on whether the character that is guessed is 
        located in the word that is given. The lower() method is applied to all parameters given for 
        the purpose of the check.
        '''
        guess = guess.lower()
        random_word = self.word.lower()

        checked_guess_feedback = f"Good guess! {guess} is in the word." if guess in random_word else f"Sorry, {guess} is not in the word. Try again."
        print(checked_guess_feedback)

        for idx, letter in enumerate(random_word) :
            if letter == guess :
                self.word_guessed[idx] = guess
        self.num_letters -= 1


    
    def ask_for_input(self) :
        '''
        This function asks for a character input to compare with a random word

        The purpose of this function is to randomly select a word from a list given as a parameter. 
        The user is also asked to provide a single alphabetical character input and the check_guess 
        function is called with the input and randomly selected word as variables.
        '''
        while True :
            guess = input('Please guess a single letter: ')
            if not len(guess) == 1 and guess.isalpha() :
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses :
                print("You already tried that letter!")
            else :
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

hangman_game = Hangman(favourite_fruit_list)            #creates an instance of the Hangman class. You CANNOT access methods without creating the instance first
hangman_game.ask_for_input()

# At the moment, it is returning where the function is, not actually the result of the function. You need to figure out how to get it to return your function itself.