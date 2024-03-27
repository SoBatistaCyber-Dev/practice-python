### loops ###


#There are 2 types of loops:
    # 1: while loop -> a while loop will execute a block of code while a condition is true
    # 2: for loop   -> a for loop iterates over a sequence and the sequence can be contents of a collection type like: lists, tuples, dictionaries, etc.

## whie loop:
    # Example 1:
value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1

print("")

    # Example 2:
value = 1
while value <= 10:
    value += 1
    if value == 5:
        continue    # stops the current iteration and just goes to the next one in the loop
    print(value)
else:               # Only use else if not using 'break'
    print("Value is now equal to " + str(value))


print("")


## for loop:
    # Example 1:
names = ["Dave", "Sara", "John"]
for x in names: # x represents each item in the names list
    print(x)


    # Example 2:
for x in "Mississippi":
    print(x)


    # Example 3_
for x in names:
    if x == "Sara":
        break   # This will break when it encounters the word 'Sara' and will not print it
    print(x)


    # Example 4:
for x in names:
    if x == "Sara":
        continue   
    print(x)


print("")


## Ranges:
    # Example 1:
for x in range(4):
    print(x)    # The print will start at 0


    # Example 2:
for x in range(2, 4):   # This will start at 2 but stop at 3
    print(x)


    # Example 3:
for x in range(0, 100, 5):  # This code will start counting from 0 and print numbers up to 95. We specified that it should print numbers in increments of 5
    print(x)
else:
    print("Glad that\'s over!")


print("")


## Nested loops:
names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")

print("")

for action in actions:
    for name in names:
        print(name + " " + action + ".")