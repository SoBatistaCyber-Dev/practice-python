'''
    Write a Python program to hash a word. 
'''

import hashlib

def hashing_words(word):
    encode_as_bytes = bytes(word, 'utf-8') #Encodes the user input into UTF-8 bytes.
    hashed_word = hashlib.sha256(encode_as_bytes).hexdigest() # hashlib.sha256()-> Processes the bytes into a hash (raw binary representation).
    # hexdigest() -> Converts the binary hash into a hexadecimal string
    return hashed_word

print("*************************************************************")
print("* This program will take your input and hashe it as SHA-256 *")
print("*************************************************************")
word = str(input("Enter a word to tranform in a hash: "))
print(hashing_words(word))