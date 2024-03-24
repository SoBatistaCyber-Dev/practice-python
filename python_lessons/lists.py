### Lists ###

# How you can create lists:
users = ['Sun', 'Sea', 'Star']

data = ['Sun','Sea', True]

mylist = list([1, "Sol", True])
print(mylist)

emptylist = []


print("Sun" in emptylist) # This will say if the value sol exists on our list called emptylist. Because it doesn't exists it will print False.

print(users[0]) # prints the first value of the list called users
print(users[-1]) # prints the last value of the list called users

print(users.index('Sea'))
print(users[0:2]) 
print(users[1:]) 
print(users[-3:-1])

print(len(data)) # says how much items we have on our list data

users.append('Water') # appends water to the list users
print(users)

# How to merge lists:
    # 1º way:
users += ['Hearth'] # This will

# How you can create a list:
users.extend(['Planet', 'Air'])
print(users)

    # 3º way (this passes a pre-existing list):
users.extend(data)
print(users)

# Add items to certein positions on our list:
users.insert(0, 'Gravity') # this will add 'Gravity' to the 0 position of our list (so it will be printed at the top of the list)
print(users)

users[2:2] = ['Inertia', 'Animals']
print(users)

# Replace values without eliminating them:
users[1:3] = ['Inertia', 'People'] # replaces the first position of our list with 'Inertia' and the second with 'People'
print(users)

# Remove values:
users.remove('Inertia')
print(users)

print(users.pop()) # eliminates the last value of the list. However, the value will be printed anyway but this time out of the list. if you print the list afterwords you'll se that the value will not exist anymore.
print(users)

del users[-1] # delete the last position
print(users)

# del data # deteletes our list called data completly. If you print it afterwords it will give an error since we deleted the list.
data.clear()
(print(data))

# Sort lists:
users[1:2] = ['inercia'] # This will be added to the list but will come in at the end of the list
users.sort()
print(users)

users.sort(key=str.lower) # This will sort the list in the alphabet order even if the word "inercia" is in lower case.
print(users)


# See how it works with numbers:

nums = [4,42,78,1,5] # This does not sort the numbers. It flips them.
nums.reverse()
print(nums)

# Ways to sort numbers:
    # 1º way:
# nums.sort(reverse=True) # This sorts the list and will keep it that way
# print(nums)

    # 2º way:
print(sorted(nums, reverse=True)) # This just sorts the list 1 time, then the list gets back to the normal.
print(nums)

# Create copys of the original list:
    # 1º way:
numscopy = nums.copy()

    # 2º way:
mynums = list(nums)

    # 3º way:
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy)
print(nums)


# How to check the type of lists:
print(type(nums))


### Tuples ###

mytuple = tuple(('so', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))


newlist = list(mytuple)
newlist.append('sol')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple # This will print the 1º item on the "anothertuple" list. Then will print the second item, and then, will print the rest of the items becuase it has the * character
print(one)
print(two)
print(hey)

print(anothertuple.count(2)) # It says how many occurrences of the number 2 are inside of anothertuple