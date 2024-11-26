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

def reverse_number(number):
    # This will try to take the user input and reverse it if it's an integer.
    try:
        # First it attempts to convert the input to an integer
        number = int(number)
        # Then reverses the integer and prints it
        number_being_reversed = int(str(number)[::-1])
        print("Reversed number:", number_being_reversed)

    # This exist for the case the user inserts a string instead of an integer.
    except:
        print("Invalid input!")

number = input("Enter a positive integer: ")
reverse_number(number)