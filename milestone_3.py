

while True :
    guess = input('Please guess a single letter: ')
    if len(guess) == 1 and guess.isalpha() :
        break
    print("Invalid letter. Please, enter a single alphabetical character.")