'''
    Create a is_prime function.
    This function works by receiving a number, and telling whether the provided number is a prime number or not.

    Expected Output:

        $: Give me a number: 12
        It is not a prime number
        Give me a number: 7
        It is a prime number
        Give me a number: ...
'''

def is_prime(number):
    if number == 2 or number == 3:
        return "It's a prime number!"
    for i in range(2, number):
        if number % i == 0:
            return "It's not a prime number!"
    return "It's a prime number!"

number = int(input("Enter a number to see if it's a prime or not: "))
print(is_prime(number))