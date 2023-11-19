# Hangman

## Table of Contents
1. [Introduction](#introduction)
2. [Installation instructions](#installation-instructions)
3. [Usage instructions](#usage-instructions)
4. [File structure of the project](#file-structure-of-the-project)
5. [Licence information](#licence-information)

## Introduction
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word from a provided list and the user tries to guess it. 

## Installation instructions
1. Clone the repository:
`git clone https://github.com/spencerejd/hangman466.git`
2. Navigate to the project directory:
`cd hangman466`
3. Run the game:
`python hangman_game.py`


## Usage instructions
### How to Play
The game starts with a random word from the provided word list.
The player has a default number of lives.
Guess a letter by entering a single alphabetical character when prompted.
The game will inform you if the letter is in the word or not.
Continue guessing until you either guess the word or run out of lives.

## File structure of the project
The project is structured as follows:
`hangman_game.py`: The main Python script containing the implementation of the Hangman game. The script initialises the game, checks guesses and handles user input.
`README.md`: Documentation file providing information about the Hangman game.
`hangman_test`: Directory containing files that show the development process and commit history of the Hangman game development.

hangman466/
│

├── hangman_game.py

├── hangman_test/

│   └── hangman_Template.py

│   └── milestone_2.py

│   └── milestone_3.py

│   └── milestone_4.py

└── README.md



## Licence information
Unlicense: This license is used for dedicating works to the public domain, allowing users complete freedom to use, modify, and distribute the code without any restrictions