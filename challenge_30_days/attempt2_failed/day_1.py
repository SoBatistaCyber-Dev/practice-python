'''
    Write a Python program that asks the user for a test grade from 0 to 100 and prints the the grade in letter form:
    A -  85-100
    B -  66-84
    C -  50-65
    D -  25-49
    E -   0-24
'''



def grade_number(grade):
    if grade in range(0, 25):
        print("You get an: E")
    elif grade in range(25, 50):
        print("You get an: D")
    elif grade in range(50, 66):
        print("You get an: C")
    elif grade in range(66, 85):
        print("You get an: B")
    elif grade in range(85, 101):
        print("You get an: A")
    else:
        print("Error: There is no such grade!")

grade = int(input("What is your grade from 0 to 100? "))
grade_number(grade)
