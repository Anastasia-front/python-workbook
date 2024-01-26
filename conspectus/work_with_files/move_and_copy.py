import shutil
import time
from pathlib import Path

"""The pathlib module integrates well with the shutil 
module for copying and moving files. The shutil.copy() 
or shutil.copy2() function is used to copy files.
"""


# Example of copying a file:

# Source and destination files
source = Path("./example/pathlib.txt")
destination = Path("./example/copy/pathlib.txt")

# Copying the file
print("~" * 30)
shutil.copy(source, destination)
print(f"File from '{source.parent}' folder copy into '{destination.parent}' folder")
print("~" * 30)


"""The shutil.copy() function copies the contents 
of a file but not the metadata, while shutil.copy2() 
copies both the contents and the metadata.

The shutil.move() function is used to move files."""


# Example of moving a file:

# Source and destination paths
source = Path("./example/example.txt")
destination = Path("./example/move/example.txt")

# create file in advance
folder_path = "example"
file_path = f"{folder_path}/example.txt"
with open(file_path, "w") as file:
    file.write("This is some content for the file.")

# Move the file
shutil.move(source, destination)
print(f"File from '{source.parent}' folder move into '{destination.parent}' folder")
print("~" * 30)

"""The stat() method returns information about a file, including its size.
"""

# Getting the file size

file_path = Path("./example/picture/bot.png")

# Getting the file size

size = file_path.stat().st_size
print(f"File size: {size} bytes")  # File size: 13694 bytes
print("~" * 30)


"""The stat() method also provides the creation time, 
the st_ctime attribute, and the file's last modification time, 
the st_mtime attribute.
"""

file_path = Path("./example/picture/bot.png")

# Creation and modification time
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime

print(
    f"Creation time: {time.ctime(creation_time)}"
)  # Creation time: Fri Dec 29 04:43:16 2023
print(
    f"Modification time: {time.ctime(modification_time)}"
)  # Modification time: Thu May 17 19:59:44 2018
print("~" * 30)


"""And the last necessary information for working with 
files is deletion. The unlink() method is used to delete 
a file. It deletes the file pointed to by the Path object.
"""


syntax = "Path.unlink(missing_ok=False)"

"""If the missing_ok parameter is set to True, 
no exception will be thrown if the file does not exist.
The default is False, which means that a FileNotFoundError 
exception will be thrown if the file does not exist.
"""

# Creating a Path object for the file
file_path = Path("./example/move/example.txt")

# Check if the file exists before deleting
if file_path.exists():
    file_path.unlink()
    print(f"File {file_path} has been deleted")
else:
    print(f"The file {file_path} does not exist")
print("~" * 30)


"""
In this example, before deleting the file, 
we check if it exists to avoid throwing a FileNotFoundError.

It is also possible to delete a file without 
first checking for its existence using the missing_ok option."""


file_path = Path("./example/move/example.txt")
file_path.unlink(missing_ok=True)


"""In this case, if the file does not exist, 
no exception will be thrown."""
