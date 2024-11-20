"""
    Write a Python program to test whether a passed letter is a vowel or not. 
    
"""

def vowel(letter):

    the_vowels = "aeiou"
    if letter == the_vowels:
        print("That's a vowel!")
    else:
        print("That's not a vowel!")

letter = str(input("Enter a letter to see if it's a vowel or not: "))
vowel(letter)