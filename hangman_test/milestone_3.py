import random

favourite_fruit_list = ['Banana', 'Easy Peelers', 'Tomato', 'Grape', 'Honeydew melon']

def random_word_selector(list_of_words):
    '''
    This function selects a random word from a given list of words

    The purpose of this function is to select a random word from the list variable given to the function.
    The word is selected using the random.choice function imported from the random module
    '''
    random_word = random.choice(list_of_words)
    return random_word

def ask_for_input(list_of_words) :
    '''
    This function asks for a character input to compare with a random word

    The purpose of this function is to randomly select a word from a list given as a parameter. 
    The user is also asked to provide a single alphabetical character input and the check_guess 
    function is called with the input and randomly selected word as variables.
    '''
    random_word = random_word_selector(list_of_words)
    print(random_word)

    while True :
        guess = input('Please guess a single letter: ')
        if len(guess) == 1 and guess.isalpha() :
            break
        print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess, random_word)


def check_guess(guess, random_word) :
    '''
    This function checks if a guessed character is found in a word

    The purpose of this function is to complete a check on whether the character that is guessed is 
    located in the word that is given. The lower() method is applied to all parameters given for 
    the purpose of the check.
    '''
    guess = guess.lower()
    random_word = random_word.lower()

    checked_guess_feedback = f"Good guess! {guess} is in the word." if guess in random_word else f"Sorry, {guess} is not in the word. Try again."
    print(checked_guess_feedback)


#    if guess in random_word :
#        print(f"Good guess! {guess} is in the word.")
#        print(random_word)
#    else :
#        print(f"Sorry, {guess} is not in the word. Try again.")
#        print(random_word)

ask_for_input(favourite_fruit_list)


