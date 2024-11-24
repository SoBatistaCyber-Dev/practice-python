'''
    Find the number of occurrences of a substring in a string

        Write a Python code to find how often a substring appears in the given string.

    Example:

    Expected Output:

        $ Give me a string: Emma is good developer. Emma is a writer.
        What is the keyword you are looking to find: Emma
        Emma appeared 2 times
'''

import re
def looking_for_key(word_to_search, words):
    nr_of_times_word_appeared = 0
    for word in words:
        if word == word_to_search:
            nr_of_times_word_appeared += 1
    print(word_to_search, "appeared", nr_of_times_word_appeared, "times")        

string = input("Give me a string: ")
cleaned_text = re.sub(r'[^a-zA-Z0-9 ]', ' ', string) 
#This will remove everything except letters, numbers, and spaces 
# by replacing unwanted characters with spaces in the 'string' variable.

splited_string = cleaned_text.split()
word = input("What is the keyword you are looking to find: ")
looking_for_key(word, splited_string)