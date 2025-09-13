# Guess the Number Game

This is a simple Python program that implements a classic "Guess the Number" game.

## Description
The program randomly selects a number between 1 and 100. The player has 6 attempts to guess the correct number. 
After each guess, the program will indicate whether the guess is too low, too high, or correct. 
The game also handles invalid inputs gracefully and provides clear feedback.

## How to Play
1. Run the Python script (`guess_number.py`).
2. Enter your name when prompted.
3. Try to guess the number by entering a value between 1 and 100.
4. The program will guide you by telling you if your guess is "TOO low" or "TOO high".
5. You have a maximum of 6 attempts.
6. At the end, the program will tell you if you guessed correctly or reveal the correct number.

## Features
- Random number generation between 1 and 100.
- Input validation to ensure the user enters a valid number.
- Keeps track of the number of guesses.
- Provides feedback on each guess.
- Friendly user interaction with name input and messages.

## Requirements
- Python 3.x

## How to Run
```bash
python guess_number.py
```