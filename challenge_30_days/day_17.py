'''
    Write a Python program to check whether a file exists. 
'''

from pathlib import Path

def check_if_file(current_file, given_file):
    try:
        return str(given_file) == str(current_file)
    except PermissionError:
        return False
    
def iterate_directory(given_file):
    base_dir = Path('/')
    for path in base_dir.rglob('*'):
        try:
            if path.is_file() and check_if_file(path, given_file):
                return f"File found: {path}"
        except PermissionError:
            continue

    return "File does not exist in the system"

print(iterate_directory('your-files-goes-here'))