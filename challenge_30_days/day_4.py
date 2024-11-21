'''
    Exercise: Check for Value in a List
    Description:

    Write a Python program that checks if a specified value is present in a given list of numbers. The program should output True if the value is found in the list and False otherwise.
    Task:

    Take two inputs:
        A value to search for (integer or float).
        A list of numbers (integers or floats).
    Check whether the specified value is in the list.
    Print True if the value is in the list, and False otherwise.

    Example Input/Output:

        Input:

    Value to search: 3  
    List of values: [1, 5, 8, 3]

    Output:

    True

    Input:

    Value to search: -1  
    List of values: [1, 5, 8, 3]

    Output:

    False
'''

def convert_list_elements_to_float(lst):
    new_list = []
    for i in lst:
        new_list += [float(i)]
    return new_list

def check_for_a_value_in_list(value_to_search, users_list):
    if value_to_search in users_list:
        print(True)
    else:
        print(False)

value_to_search = float(input("Enter the value that you want to search for on the list: "))
list_of_values = input("Enter a list of numbers (make sure to enter a space between each number): ")

users_list = list_of_values.split()

new_list = convert_list_elements_to_float(users_list)

check_for_a_value_in_list(value_to_search, new_list)