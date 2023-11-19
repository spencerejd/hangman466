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

> Make sure you do the following before you complete this project.
_You are requested by AiCore to document your experience creating this game by doing the following_
_Add documentation to your GitHub README file. You can refer to the relevant lesson in the prerequisites for this task for more information._
_At **minimum**, your README file should contain the following information:_

**_Installation instructions_**,
**_Usage instructions_**,
**_File structure of the project_**,
**_License information_**

## Installation instructions
1. Clone the repository:
`git clone https://github.com/spencerejd/hangman466.git`
2. Navigate to the project directory:
`cd hangman466`
3. Run the game:
`python hangman.py`


## Usage instructions
### How to Play
The game starts with a random word from the provided word list.
The player has a default number of lives.
Guess a letter by entering a single alphabetical character when prompted.
The game will inform you if the letter is in the word or not.
Continue guessing until you either guess the word or run out of lives.

## File structure of the project
The project is structured as follows

hangman-game/
│
├── hangman.py
├── tests/
│   └── test_hangman.py
└── README.md



## Licence information
Unlicense: This license is used for dedicating works to the public domain, allowing users complete freedom to use, modify, and distribute the code without any restrictions