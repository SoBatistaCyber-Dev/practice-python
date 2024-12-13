'''
    Write a Python program that inputs a number and generates an error message if it is not a number. 
'''

def check_if_is_number(text):
    try:
        float(text)
        print("That is indeed a number!")
    except ValueError:
        print("ERROR: That's not a number")


text = input("Enter the number: ")
check_if_is_number(text)