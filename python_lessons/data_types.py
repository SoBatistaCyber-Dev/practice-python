import math 
# String data type

# Literal assignament
first = "Solange"
last = "Batista"
print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Constructor functions
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1998)
print(type(decade))
print(decade)

satatement = "I like rock music from the " + decade + "s."
print(satatement)

# Multiple lines
multiline = '''
Hey, how are you?

I was just chacking in.

                        All good?

'''
print(multiline)

#Escaping special characthers
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?' #\t-> indicates a space tab and the \n--> indicates a new line
print(sentence)

# String Methods
print(first)         
print(first.lower()) # Prints the value of "first" in lower cases
print(first.upper()) # Prints the value of "first" in upper cases
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                                              "
multiline = "                                                               " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("") # Prints an empty line

# Build a menu
title = "menu".upper()
print(title.center(20, "=")) 
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# String index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("S"))
print(first.endswith("y"))


# Bollean data type
myvalue = True 
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))


# Numeric data types
    # Integer type:
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

    # Float type:
gpa = 3.28
y = float(1.14)
print(type(gpa))

    # Complex type:
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1))


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))


# You will have an error if you attempt to cast incorrect data
zip_value = int("New York") # Python does not like this and will print you an error

