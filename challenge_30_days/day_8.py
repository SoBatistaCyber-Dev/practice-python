'''
    Check Palindrome Number

    Write a Python code to check if the given number is palindrome. A palindrome number is a number that is the same after reverse. For example, 545 is the palindrome number.

    Expected Output:

    Give me a number: 121
    Yes. given number is palindrome number

    Give me a number: 125
    No. given number is not palindrome number
'''

def check_palindrome_number(number):
    return number == number[::-1] 
    # This will print the string backwords and see if it stays the same as the original. 
    # And if it does it's because it's a palindrome number.
    
number = input("Give me a number: ")

if check_palindrome_number(number):
    #This checks if the result of calling this funtion with the 'number' statement is True or Flase.
    # If it's True it prints the string below. 
    print("Yes. The given number is palindrome number!")
else:
    print("No. The given number is not a palindrome number!")
    # If it's False prints this one.


check_palindrome_number(number)