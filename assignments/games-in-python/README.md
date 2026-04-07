
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

In this assignment, you will build a command-line Hangman game in Python. You will practice working with strings, loops, conditionals, and user input while managing game state.

## 📝 Tasks

### 🛠️	Build Core Hangman Gameplay

#### Description
Create the main game loop for Hangman where a random word is selected and the player guesses one letter at a time.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list.
- Display the hidden word using underscores for unguessed letters (for example: `_ _ _ _`).
- Reveal all matching positions when a correct letter is guessed.


### 🛠️	Handle Attempts and End Conditions

#### Description
Track incorrect guesses, prevent invalid input from breaking the game, and end the game with clear results.

#### Requirements
Completed program should:

- Decrease remaining attempts only when a new incorrect letter is guessed.
- End the game with a win message when the full word is guessed.
- End the game with a lose message showing the correct word when attempts reach zero.
