'''
    Exercise: Reverse a Number
    Description:

    Write a Python program that takes a positive integer as input from the user and returns the number in reverse order. The program should handle numbers of any length.
    Task:

        Prompt the user to enter a positive integer.
        Reverse the digits of the number and display the reversed number.

    Example Input/Output:

        Input:

    Enter a number: 12345

    Output:

    Reversed number: 54321
'''

def reverse_number(number_being_reversed):
    print("Reversed number:", number_being_reversed)

number = int(input("Enter a positive integer: "))
number_being_reversed = str(number)[::-1]
# This converts the number to a string and reverses it.
reverse_number(number_being_reversed)