### Dictionaries ###

## How to create dictionaries:
    # 1º way:
band = {
    "vocals": "Plant",
    "guitar": "Page"
}
print(band)

    # 2º eay:
band2 = dict(vocals="Plant", guitar="Page")
print(band2)


print(type(band)) # Checks the type
print(len(band)) # Check the length of the dictionary


## How to access items in a dictionary:
    # 1º way:
print(band["vocals"]) # Prints the value paired with the key vocals

    # 2º way:
print(band.get("guitar")) # Prints the value paired with the key guitar


## How to list all keys:
print(band.keys())


## How to list all values:
print(band.values())


## List of key/value pairs as tuples:
print(band.items())


## How to verify if a key exists in a dictionary:
print("guitar" in band)
print("triangle" in band)


## How to change values in a dictionary:
    # 1º way:
band["vocals"] = "Coverdale" # Changes the value of the key 'vocals' from 'Plant' to 'Coverdale'

    # 2º way:
band.update({"bass": "JPJ"}) # This creates a new key value pair
print(band)


## How to remove items:
    # 1º way:
print(band.pop("bass")) # This removes the key 'bass' but prints its value.
print(band) # Then yout print once again the dictionary but this time the 'bass' key and its value will not exist

    # 2º way:
band["drums"] = "Bonham" # I'm adding a new key-value pair to demonstrate the next method of removing items
print(band)

print(band.popitem()) # This will remove the last key-value pair inserted on the dictionary. In this case the key-value pair 'drums': 'Bonham'
print(band) # This will print the final version of the dictionary after removing the key-value pair above


## How to delete and clear items:
band["drums"] = "Bonham" # I'm adding this so I can delete it from the dictionary
del band["drums"] # This will delete the key-value pair 'drums': 'Bonham' from the 'band' dictionary 
print(band)

band2.clear() # This will clear the 'band2' dictionary. So, it will print an empty dictionary
print(band2)

del band2 # This will delete the 'band2' dictionary 


## How to copy dictionaries:
    # 1º way:
band2 = band.copy()
band2["drums"] = "SoBatista"
print(band2)

    # 2 way:
band3 = dict(band) # This will copy the contents of the 'band' dictionary to the 'band3' dictionary
print(band)        # I will print the 'band' dictionary for you to see taht they have the same key-pair values
print(band3)


## What you shouldn't do when copy dictionaries:
# band2 = band # This operation does not copy the dictionary. Instead, it creates a reference to the 'band' dictionary. This means that any modifications made to the 'band' dictionary will automatically affect the 'band2' dictionary as well
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "SoBatista" # I'm adding the key-pair value 'drums': 'SoBatista' to the 'band2' dictionary
# print(band)                  # But in this line when you print the 'band' dictionary, you'll see that the key-pair value 'drums': 'SoBatista' was added to the 'band' dictionary as well


## Nested dictionaries:
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
   
    "memeber2": member2
}
print(band)
print(band["member1"]["name"])


## How to create sets:
    # 1º way:
nums = {1, 2, 3, 4}

    # 2º way:
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print((nums))


## No duplicates are allowed:
nums = {1, 2, 2, 3} # This will not print the number 2 twice
print(nums)


## True is a duplicate of 1, False is a duplicate of 0:
nums = {1, True, 2, False, 3, 4, 0}
print(nums)


## How to check if a value is in a set:
print(2 in nums)
    # note: You cannot refer to an element in the set with an index position or a key


## How to add a new element to a set:
nums.add(8)
print(nums)


## How to add elements from one set to another:
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)
    # Note: you can use update with lists, tuples and dictionaries


## How to merge 2 sets to create a new set:
one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
print(mynewset)


## How to merge two different sets into one while retaining only the duplicates:
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two) # This does not create a new set. The set named 'one' is the one that will be modified
print(one)


## How merge two different sets into one while retaining all unique elements and excluding duplicates:
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)