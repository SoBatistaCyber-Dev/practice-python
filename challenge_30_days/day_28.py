'''
    Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other. 
'''

def find_if_duplicates_on_inout(lst):
    if not all(i.isdigit() for i in lst): # Check if all elements are numbers
        print("That's not a number!")
    elif len(lst) != len(set(lst)):
        print("Not all the numbers are different!")
    else:
        print("All the numbers are different!")

lst = input("Enter a list of numbers (with spaces between them): ").split()
find_if_duplicates_on_inout(lst)