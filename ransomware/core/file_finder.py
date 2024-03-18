import os

def find_files(directory):
    """
    Recursively finds all files in a directory and its subdirectories.

    Args:
    - directory (str): The path to the directory to search.

    Returns:
    - list: A list of file paths.
    """
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

