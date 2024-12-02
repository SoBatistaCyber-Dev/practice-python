'''
    Exercise: Count the Vowels
    Description:

    Write a Python program that takes a string as input and counts the number of vowels (a, e, i, o, u) in the string, regardless of their case. The program should output the total number of vowels found.
    Task:

        Prompt the user to enter a string.
        Count the vowels in the string, ignoring whether they are uppercase or lowercase.
        Print the total number of vowels in the string.

    Example Input/Output:

        Input:

    Enter a string: Hello World

    Output:

    Number of vowels: 3
'''
import re

def count_the_vowels(user_string):
    vowels = '[aeiouAEIOU]' # Matches any single vowel, case-insensitive
    count_vowels = len(re.findall(vowels, user_string))            
    return count_vowels

user_string = input("Enter a sting: ")
print("Number of vowels:", count_the_vowels(user_string))
