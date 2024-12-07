'''
    Write a Python program to retrieve the path and name of the file currently being executed. 
'''

from pathlib import Path
import os

print("Your current working directory is:", Path.cwd())
print("The file being executed is:", os.path.basename(__file__))