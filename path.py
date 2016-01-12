import os
import sys


def print_directory_contents(path):
    """
    This function takes the name of a directory and prints out the paths files within that
    directory as well as any files contained in contained directories.

    This function is similar to os.walk. I've built it just for learning purposes.
    """
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            print_directory_contents(child_path)
        else:
            print(child_path)


if __name__ == "__main__":

    # If the end user doesn't provide a specific path as an argument when calling the program, use the home directory
    if len(sys.argv) == 1:
        home = os.path.expanduser("~")
    else:
        home = str(sys.argv[1])
    
    print_directory_contents(home)
