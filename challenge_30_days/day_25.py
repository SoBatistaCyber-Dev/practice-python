'''
    Write a Python program to test whether the system is a big-endian platform or a little-endian platform. 
'''

import sys

if sys.byteorder == "big": # Verifies if the system's byte order (aka endianness), is big endian
    print("The system is big-endian.")
else:
    print("The system is little-endian.")