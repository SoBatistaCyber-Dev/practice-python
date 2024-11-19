"""

    Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user. 

Challenge 2: 
"""

def check_even_or_odd(x):
    if x % 2 == 0:
        print("That's a even number!")
    else:
        print("That's a odd number!")

x = int(input("Enter a number to see if it's even or odd: "))
check_even_or_odd(x)
