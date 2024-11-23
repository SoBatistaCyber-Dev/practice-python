"""

Exercise: Guess the Number Game

Objective: Practice using loops, conditionals, random numbers, and user input in Python.
Instructions:

    Write a program where the computer picks a random number between 1 and 100.
    The player has to guess the number, and the program gives hints:
        If the guess is too high, display "Too high!"
        If the guess is too low, display "Too low!"
    When the player guesses the correct number, display a congratulatory message and the number of attempts it took.
    Include error handling to ensure the user enters a valid number.

Example Output:

Welcome to the Guess the Number Game!
I'm thinking of a number between 1 and 100.

Enter your guess: 50
Too low! Try again.

Enter your guess: 75
Too high! Try again.

Enter your guess: 62
Congratulations! You guessed it in 3 attempts.

Hints:

    Use the random module to generate a random number.
    Use a while loop to keep asking for guesses until the correct number is guessed.
    Use int() to convert input strings to numbers.
    Keep track of the number of attempts with a counter.
"""