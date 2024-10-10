'''
    Remove first n characters from a string

    Write a Python code to remove characters from a string from 0 to n and return a new string.

    For Example:

        remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
        remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.

    Note: n must be less than the length of the string.
'''

# Your solution goes here <- delete this 

def remove_chars(word, remove_characters):
    return word[int(remove_characters):]

print("Your words will be:", remove_chars("PYnative", 4))
print("Your words will be:", remove_chars("PYnative", 2))

word_1 = input(str("Enter a word: "))
remove_characters_1 = input(str("How many characters do you want to remove from the begining of your first word? "))

print("Your words will be:", remove_chars(word_1, remove_characters_1))
