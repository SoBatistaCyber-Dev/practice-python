"""

Exercise: Guess the Number Game

Objective: Practice using loops, conditionals, random numbers, and user input in Python.
Instructions:

    Write a program where the computer picks a random number between 1 and 10.
    The player has to guess the number:
    When the player guesses the correct number, display a congratulatory message and the number of attempts it took.

Example Output:

Welcome to the Guess the Number Game!
I'm thinking of a number between 1 and 100.

Enter your guess: 5
Wrong guess. Try again!

Enter your guess: 2
Congratulations! You guessed it in 2 attempts.

Hints:

    Use the random module to generate a random number.
    Use a while loop to keep asking for guesses until the correct number is guessed.
    Use int() to convert input strings to numbers.
    Keep track of the number of attempts with a counter.
"""
import random

def random_guess_number():
    print("------------------------------------------")
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 10.")
    print("------------------------------------------")
    random_number = random.randint(1, 10)
    nr_of_guesses = 0 #Initialize the number of guesses
    while True:
        guess_number = int(input("Enter your guess: "))
        nr_of_guesses += 1 # Increment the guess count
        if guess_number == random_number:
            print("Congratulations! You guessed it in", nr_of_guesses, "attempts")
            break
        else:
            print("Wrong guess. Try again!")
        
random_guess_number()