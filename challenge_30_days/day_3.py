"""
    Write a Python program to test whether a passed letter is a vowel or not. 
    
"""

def vowel(letter):
    if letter == "a":
        print("That's a vowel!")
    elif letter == "e":
        print("That's a vowel!")
    elif letter == "i":
        print("That's a vowel!")
    elif letter == "o":
        print("That's a vowel!")
    elif letter == "u":
        print("That's a vowel!")
    else:
        print("That's not a vowel!")

letter = str(input("Enter a letter to see if it's a vowel or not: "))
vowel(letter)