'''
    Sum of List

    Write a function called sum_list that takes a list of numbers and returns the sum of all the numbers in the list.

    Example Input/Output:

    # Input:
    numbers = [1, 2, 3, 4, 5]
    print(sum_list(numbers))

    # Output:
    15
'''
import re
import sys

def sum_of_list(numbers):
    
    try:
        removed_commas = re.sub(",", " ", numbers)
        convert_lst = removed_commas.split()
        sum = 0
        for i in convert_lst:
            sum += int(i)
        return sum
    except ValueError:
        print("That's not a number!")
        sys.exit(1)    

numbers = input("Enter a list of numbers: ")
print(sum_of_list(numbers))





