import random

favourite_fruit_list = ['Banana', 'Easy Peelers', 'Tomato', 'Grape', 'Honeydew melon']

def random_word_selector(list_of_words):
    '''
    This function selects a random word from a given list of words

    The purpose of this function is to select a random word from the list variable given to the function.
    The word is selected using the random.choice function imported from the random module
    '''
    fruit = random.choice(favourite_fruit_list)
    return fruit

def input_check_func():
    '''
    This function checks if the input received is a single letter

    The purpose of this function is to request input from the user and complete a check
    to confirm if the user input contains a single character, that is alphabetic.
    '''
    guess = input('Please enter a single letter: ')
    input_checker = "Good guess" if len(guess) == 1 and guess.isalpha() else "Oops! That's not a valid input"
    return input_checker



print(random_word_selector(favourite_fruit_list))
print(input_check_func())