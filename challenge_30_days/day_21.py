'''
    Write a python program that does the same as ls and lists all the contents of the current folder
'''

from pathlib import Path

def iterate_directory(directory):
    if directory.is_dir():
        for file in directory.iterdir():
            print(file.name, end="  ")
    else:
        print(f"{directory} invalid")

current_directory = Path.cwd()
iterate_directory(current_directory)
