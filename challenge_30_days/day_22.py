'''
    Write a Python program to convert height (in feet and inches) to centimeters. 
'''

def height_converter_into_cm():
    if choose == 1:
        feet = int(input("Enter the height in feet: "))
        cm = feet * 30.48
        print("The height is", cm, "cm")
    elif choose == 2:
        inches = int(input("Enter the height in inches: "))
        cm = inches * 2.54
        print("The height is", cm, "cm")
    else:
        print("That's not an option!")

print("From this menu choose an option to convert into cm: ")
print("Choose 1 for Feet")
print("Choose 2 for Inches")
print("")
choose = int(input("What's your answer? "))
print("")
height_converter_into_cm()
