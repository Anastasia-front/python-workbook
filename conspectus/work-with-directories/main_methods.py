"""The iterdir() method is used to get a list of all files 
and subdirectories in the specified directory. This method 
returns an iterator that produces Path objects for each file and 
subdirectory in the directory specified by the current Path object."""

import os
from pathlib import Path

# Get the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# Creating a Path object for the directory
directory = Path("./example")

# Display a list of all files and subdirectories
print("~" * 30)
for path in directory.iterdir():
    print(path)
print("~" * 30)

"""The mkdir() method is used to create a new directory.
"""
# Path.mkdir(mode=0o777, parents=False, exist_ok=False)

"""
Parameters:
mode - access rights to the directory, used for Linux and not relevant for Windows.
parents - if true, will create all missing parent directories.
exist_ok - If true, no error will be thrown if the directory already exists.

"""

directory = Path("./example/new_folder")
print(directory)
directory.mkdir(parents=True, exist_ok=True)

file_path = f"{directory}/example.txt"
# add file
with open(file_path, "w") as file:
    file.write("This is some content for the file.")

for path in directory.iterdir():
    print(path)
print("~" * 30)

"""The rmdir() method is used to delete a directory. 
It deletes the directory, but the directory must be empty.
"""

directory = Path("./example/new_folder")
file_path = Path("./example/new_folder/example.txt")

# Check if the file exists before deleting
if file_path.exists():
    file_path.unlink()
    print(f"File {file_path} has been deleted")
else:
    print(f"The file {file_path} does not exist")

directory.rmdir()
print(
    f"Delete {directory} folder -  having cleared it first\
 / the folder must be empty otherwise an error will occur"
)
print("~" * 30)

"""The pathlib module also provides several methods 
for checking the existence and type of file objects:

exists() method checks if a file or directory exists.
the is_dir() method checks whether the object is a directory.
the is_file() method checks whether the object is a file."""


path = Path("./example/picture")

# Existence check
if path.exists():
    print(f"{path} exists")  # picture exists

# Check if this is a directory
if path.is_dir():
    print(f"{path} is a directory")  # picture is a directory

# Check if this is a file
if path.is_file():
    print(f"{path} is a file")
print("~" * 30)
