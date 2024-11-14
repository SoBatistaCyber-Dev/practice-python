'''
    Write a Python program that asks the user for the number of seconds and converts it into the number of days corresponding to those seconds:

    Example:
    Write a number of seconds:
    ? 65432998
    The corresponding number of days is 757.3263657407407
'''

def number_of_seconds(seconds):
    number_of_days = seconds / 86400
    print(number_of_days)
seconds = int(input("Enter a number of seconds to see its corresponding days: "))

number_of_seconds(seconds)
