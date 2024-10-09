# Title: Create the Fibonacci sequence

# Statement: Create the fibonacci sequence until element 50.

'''
    Expected Output:

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377 ... until element 50.
'''

# Your solution goes here <- delete this 

previous = 1
previous_2 = 0
element = 50

for i in range(element):
    if(i == 0):
        print(0)
    elif(i == 1):
        print(previous)
    else:
        sum = previous + previous_2
        print(sum)
        previous_2 = previous
        previous = sum
