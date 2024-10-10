'''
    Remove first n characters from a string

    Write a Python code to remove characters from a string from 0 to n and return a new string.

    For Example:

        remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
        remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.

    Note: n must be less than the length of the string.
'''

# Your solution goes here <- delete this 

word = input(str("Enter a word: "))
remove_characters = input(str("How many characters do you want to remove from the begining of your word? "))

def remove_chars(word):
    return word
print("Your word will be:", word[int(remove_characters):])


"""
word_1 = "PYnative"
word_2 = "PYnative" 

def remove_chars(word_1, word_2):
    return word_2, word_1

print(word_1[4:], word_2[2:])

"""