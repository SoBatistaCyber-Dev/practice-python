"""
Challenge 1: FizzBuzz

Write a program that prints the numbers from 1 to 20, but:

    For multiples of 3, print "Fizz" instead of the number.
    For multiples of 5, print "Buzz" instead of the number.
    For multiples of both 3 and 5, print "FizzBuzz".
    
    Example:
    1  
    2  
    Fizz  
    4  
    Buzz  
    Fizz  
    7  
    8  
    Fizz  
    Buzz  
    11  
    Fizz  
    13  
    14  
    FizzBuzz  
    16  
    17  
    Fizz  
    19  
    Buzz
"""

def numbers():
    for i in range(1, 21):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

numbers()