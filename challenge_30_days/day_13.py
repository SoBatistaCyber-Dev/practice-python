'''
    Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
    Sample data : 3, 5, 7, 23
    Output :
    List : ['3', ' 5', ' 7', ' 23']
    Tuple : ('3', ' 5', ' 7', ' 23')
'''
import re
import sys

def check_if_ints(lst):
    try:
        for i in lst:
            int(i)
    except ValueError:
        print("That's not a number!")
        sys.exit(1)

def lst_numbers(number):
    removed_commas = re.sub(",", " ", number)
    convert_lst = removed_commas.split()
    check_if_ints(convert_lst)

    lst_tuple = tuple(convert_lst)
    print("Tuple:", lst_tuple)

    lst = list(convert_lst)
    print("List:", lst)
    
number = input("Sample data :")
lst_numbers(number)