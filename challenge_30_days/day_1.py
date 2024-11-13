'''
    Write a Python program that asks the user for a test grade from 0 to 100 and prints the the grade in letter form:
    A - 100-85
    B -  66-84
    C -  50-65
    D -  25-49
    E -   0-24
'''

grade = int(input("What is your grade from 0 to 100? "))

if grade in range(0, 25):
    print("This is your letter form: E")
elif grade in range(25, 50):
    print("This is your letter form: D")
elif grade in range(50, 66):
    print("This is your letter form: C")
elif grade in range(66, 85):
    print("This is your letter form: B")
elif grade in range(85, 101):
    print("This is your letter form: A")
else:
    print("That does not exist!")
