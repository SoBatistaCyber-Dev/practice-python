'''
    Implement the bubble sort algorithm (read it from the book Algorithms)
'''

def bubble_sort(lst_numbers):
    length = len(lst_numbers)
    for i in range(length):
        for n in range(0, length - i - 1): #This loop is used to compare two numbers in the list, one at a time
            if lst_numbers[n] > lst_numbers[n + 1]: #This checks if a number is bigger than the one right next to it
                lst_numbers[n], lst_numbers[n + 1] = lst_numbers[n + 1], lst_numbers[n] #If the number on the left is bigger than the one on the right, they switch places
    print("Your sorted list is:", lst_numbers)

try:
    # Get input from the user and converts it to a list of numbers
    lst_numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    bubble_sort(lst_numbers)
    
except ValueError:
    print("Those are not numbers!")

bubble_sort([2, 3, 8])