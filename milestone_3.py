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

fruit = random_word_selector(favourite_fruit_list)

while True :
    guess = input('Please guess a single letter: ')
    if len(guess) == 1 and guess.isalpha() :
        break
    print("Invalid letter. Please, enter a single alphabetical character.")

print(guess)

# what we want to do is create a check on if guess is in our random_word, then return ...

if guess in fruit :
    print(f"Good guess! {guess} is in the word.")
    print(fruit)
else :
    print(f"Sorry, {guess} is not in the word. Try again.")
    print(fruit)
