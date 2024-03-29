### Functions ###

def hello():
    print("Hello world!")

hello()

print("")

def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

total = sum(7, 2)
print(total)


print("")


def multiple_items(*args):  # Here, since we don't know how many arguments will be passed, we use the symbol '*'.
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Sara")


print("")


def mult_named_items(**kwargs):      # kwargs stands for 'key word arguments'
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Dave", last = "Sara")
        