
import random

favourite_fruit_list = ['Banana', 'Clementines', 'Tomato', 'Grape', 'Melon']

class Hangman :
    '''
    This class is used to represent the game Hangman.

    Attributes:
        word (str) : the word to be guessed from a provided list
        word_guessed (list) : a list of the letters of the word, with _ for each letter not yet guessed
        num_letters (int) : number of unique letters in the word that have not been guessed yet
        num_lives (int) : number of lives left to play the game
        word_list (list) : the provided list of words
        list_of_guesses (list) : a list of the guesses that have been attempted    
    '''
    def __init__(self, word_list, num_lives = 5):
        
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len([unique_letter for unique_letter in set(list(self.word) + self.word_guessed) if unique_letter.isalpha()])
                            # 1. convert the random word into a list of each string - list(self.word)
                            # 2. we should now have two lists, i.e one is list(self.word) ['f','r','u','i','t'] and the other is self.word_guessed ['_','_','_','_','_',]
                            # 3. now let's combine them to give us a single list that is unique and contains just alphabetical characters
                            # 4. uniquemerged_set = set(list(self.word) + self.word_guessed)
                            # 5. however, word_guessed contains special characters, you will need to filter this out
                            # 6. uniquemerged_set = [unique_letter for unique_letter in set(list(self.word) + set(self.word_guessed)) if unique_letter.isalpha()]
                            # 7. and this should produce a list of unique letters that have not been guessed yet! Add the len function and we have what we're after!
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    
    def _check_guess_(self, guess) :
        '''
        This function is used to return whether a guessed character is found in the word

        Args:
            guess (str) : the letter guessed.
        
        Returns:
            list : a list of the letters found in the word that have been guessed
            str: confirmation if the guess is or is not in the word
            str: the number of lives remaining

        '''
        random_word = self.word.lower()
        print("Number of unique letters before we check our guess:", self.num_letters)
        print("The unique letters in our word", set(self.word))

        if guess in random_word :
            print(f"Good guess! {guess} is in the word.")

            for idx, letter in enumerate(random_word) :
                if letter == guess :
                    self.word_guessed[idx] = guess

            self.num_letters -= 1
            print("Hangman:", self.word_guessed)

        else :
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

        print("Number of unique letters remaining in word:",self.num_letters)

    
    def ask_for_input(self) :
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
                self._check_guess_(guess)
                self.list_of_guesses.append(guess)
                #print("Your list of guesses:",self.list_of_guesses)

hangman_game = Hangman(favourite_fruit_list)            #creates an instance of the Hangman class. You CANNOT access methods without creating the instance first
hangman_game.ask_for_input()

# At the moment, it is returning where the function is, not actually the result of the function. You need to figure out how to get it to return your function itself.