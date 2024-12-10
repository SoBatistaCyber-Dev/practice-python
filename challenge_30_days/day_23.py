'''
    Write a python program that looks into the system file structure & tries to find the given keyword in the file name

    Expected Output:
        Keyword: flag
        /etc/flag.txt
        /home/user/temos_uma_flag.txt
        ...
'''

from pathlib import Path

# Checks if the given word exists in the specified file (case-insensitive) and returns True if found, otherwise False.
def find_word(word, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if word.lower() in line.lower():
                    return True
    except (UnicodeDecodeError, PermissionError, Exception): # Handle various errors
        pass
    return False

# Searches all accessible files from the root directory for the given word, excluding certain system directories.
def find_word_in_file_system(word):
    base_dir = Path("/") # Set the base directory to the root directory '/'
    found_files = []
    excluded_dirs = ["/proc", "/sys", "/dev", "/run", "/tmp"] # Directories to exclude from the search

    try:
        # Recursively iterate through all files and directories starting from base_dir
        for path in base_dir.rglob('*'):
            try:
                # Skip excluded directories
                if any(str(path).startswith(excluded_dir) for excluded_dir in excluded_dirs):
                    continue
                # Skip symbolic links
                if path.is_symlink():
                    continue
                # Check if the path is a file
                if path.is_file():
                    if find_word(word, path):
                        found_files.append(str(path))
            except PermissionError:
                continue
    except PermissionError:
        pass

    # Print results
    if found_files:
        print(f"The word '{word}' was found in the following files:")
        for file_path in found_files:
            print(file_path)
    else:
        print(f"There is no file with the word '{word}'.")

word = input("Enter a word to search for: ").strip()
find_word_in_file_system(word)

