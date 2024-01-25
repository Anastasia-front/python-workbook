from pathlib import Path, PurePath

pathlib = "is a Python module that provides classes \
    for handling file paths in an object-oriented style. \
    The two main classes in this module are Path and PurePath."

"""PurePath is a base class in pathlib that provides 
object-oriented methods for manipulating paths without 
accessing the file system. It can be used to work with 
paths on different operating systems. PurePath allows 
you to perform operations such as splitting a path into 
parts, checking suffixes, filenames, paths, and more.
"""

p = PurePath("/usr/bin/simple.jpg")
print("~" * 30)
print("Name:", p.name)  # Name: simple.jpg
print("Suffix:", p.suffix)  # Suffix: .jpg
print("Parent:", p.parent)  # Parent: \usr\bin
print("~" * 30)

"""PurePath has a number of useful methods and attributes:

p.parent points to the parent directory;
p.name returns only a string with the name of the directory or file pointed to by p;
p.suffix returns as a string the extension of the file pointed to by p, starting with a dot;"""


"""The Path class inherits all methods from PurePath a
nd adds methods to perform operations that require 
access to the file system, such as reading, writing 
files, checking for file existence, and so on. 
With the Path class, you can create new files, 
read and write data, check for paths, list files 
in a directory, and more.
"""


"""Basically, work with the file system is done 
through Path. Path should be taken as a pointer 
to a file or directory. To create such a Path, 
it is enough to call Path as a function and pass 
the address string in the file system as an argument:
"""


p = Path("example.txt")
p.write_text("Hello, Rob")  # Hello, Rob
print(p.read_text())
print("Exists:", p.exists())  # Exists: True
print("~" * 30)

"""This code snippet uses the pathlib module 
to create, write, read, and validate a file. 
First, a Path object is created, which points 
to the example.txt file in the directory where 
the script was launched. Using the write_text() 
method, the string "Hello, world!" is written 
to this file. Then, using the read_text() method, 
the contents of the file are read and displayed 
on the screen. Finally, the exists() method is 
used to check if the file exists, and the result 
is also displayed. All code demonstrates simple 
interaction with the file system through the 
pathlib object-oriented interface.
"""


"""The application of Path and PurePath depends on the specific needs 
of the application. For most practical purposes, Path will be the best choice,
as it provides a wider range of options for working with files and directories.
"""


# Creating Paths

"""Creating paths using the Path class in Python's pathlib module 
is a convenient way to manipulate file paths that abstracts 
from the specifics of a particular operating system.
"""


"""The Path class automatically adapts to the specifics of paths 
in different operating systems. For example, Windows uses backslashes (\), 
while Unix-like systems (Linux, macOS) use forward slashes (/).
"""


# The example of the path creation process is as follows:

# For Unix/Linux
path_unix = Path("/usr/bin/python3")

# For Windows
path_windows = Path("C:/Users/Username/Documents/file.txt")


"""Pathlib concatenation is a process by which you can create 
full paths to files or directories by adding different parts of the path together.
"""


"""The / operator is used to combine paths. This is an intuitive 
way of creating a path that abstracts from the difference 
in path syntax between different operating systems.
"""

# Initial path
base_path = Path("/usr/bin")

# Adding additional parts to the path
full_path = base_path / "subdir" / "script.py"

print(full_path)  # Output: /usr/bin/subdir/script.py
print("~" * 30)

"""In this example, additional parts are added to the initial path 
base_path - the directory "subdir" and the file "script.py". 
The / operator allows us to do this cleanly and clearly, 
and we get the path to the file:
"""
# \usr\bin\subdir\script.py


# Relative and absolute paths


"""When working with files and directories in Python, 
it's important to understand the differences between 
relative and absolute paths. The pathlib module 
provides tools to work with both types of paths.
"""


"""An absolute path is the full path to a file or directory 
from the root of the file system. It contains all 
the information needed to locate a file or directory.
"""


# Example on Unix/Linux: /home/user/documents/example.txt
# Example on Windows: C:\Users\user\documents\example.txt


"""Absolute paths are used when you need to specify 
the exact location of a file or directory, regardless 
of the current working directory of the program.
"""

"""A relative path is a file or directory path 
relative to the current working directory. 
It does not contain complete location information
 and depends on the location from which the program is executed."""

# Let's say you're working on a Windows computer, and your current
#  working directory (where you run your Python script) is, for example,
#  C:\Users\Username. Your task is to work with the file example.txt,
#  which is located in the Documents subdirectory of your home directory.


# An absolute path in Windows includes the drive letter and specifies
# the full path to the file from the root of the drive. For example,
#  the absolute path to our file might look like C:\Users\Username\Documents\example.txt.


# The relative path is defined relative to the current working directory.
#  If your current working directory is C:\Users\Username, then the
#  relative path to the file example.txt in the Documents directory
#    is simply Documents\example.txt.


# With pathlib, you can easily convert paths
# between absolute and relative formats.

# Conversion of relative path to absolute
relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()
print(absolute_path)
print("~" * 30)

"""Consider an example that was launched in the directory 
(current working directory) of the author of the course. 
Note that your directory may be different:
"""
# E:\WebDir\Works\Python\python-help-solution\example_for_new_core\l04


"""Then, when executing the example, we should get the following output:
"""
# E:\WebDir\Works\Python\python-help-solution\example_for_new_core\l04\documents\example.txt


"""In this example, Path("documents/example.txt") 
creates a relative path. The absolute() method converts 
it to an absolute path based on the current working directory.
"""


"""There is a method relative_to() which, on the contrary, 
is used to obtain a relative path relative to a given directory.
"""

# Conversion of relative path to absolute
relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()

current_working_directory = Path(
    "E:\WebDir\Works\Python\python-help-solution\example_for_new_core\l04"
)
relative_path = absolute_path.relative_to(current_working_directory)
print(relative_path)
print("~" * 30)


# Manipulation of path components

"""The Path class provides convenience methods for manipulating 
path components such as with_name and with_suffix. These methods 
allow you to easily change the file name or file extension in the Path object.
"""


"""The with_name method replaces the file name in the 
path with a new one. It is useful when you need to change 
only the filename while keeping the rest of the path unchanged.
"""


# Initial file path
original_path = Path("documents/example.txt")

# Change the file name
new_path = original_path.with_name("report.txt")
print(new_path)
print("~" * 30)

"""In this example, with_name("report.txt") replaces 
the file name example.txt with report.txt, while keeping 
the rest of the documents path unchanged.
"""
# documents\report.txt


"""The with_suffix method replaces or appends the file 
extension in the path. This is useful when you need 
to change the file type or add an extension to a file that doesn't have one.
"""

# Initial file path
original_path = Path("documents/example.txt")

# Change the file name
new_path = original_path.with_suffix(".md")
print(new_path)
print("~" * 30)

"""In this example, the with_suffix(".md") method adds the .md extension to the path.
"""


# documents\example.md


"""But it should be understood that the with_name and with_suffix 
methods in the Path class of the pathlib module in Python do not 
change the physical name of the file on the disk. Instead, 
they are used to create a new Path object that reflects the changed path.
"""


original_path = Path("documents/example.txt")

# Creates a new Path object with a different filename
new_path = original_path.with_name("report.txt")

print(original_path)
print(new_path)
print("~" * 30)

"""In this example, original_path remains the same, and new_path 
is a new Path object that represents the path with the new file name.
"""


# documents\example.txt
# documents\report.txt


"""To physically change the name of a file on disk, 
you need to use methods for working with the file system, 
for example, rename. This call will rename the file 
example.txt to report.txt in the documents directory on disk.
"""


original_path = Path("documents/example.txt")

# Creates a new Path object with a different filename
new_path = original_path.with_name("report.txt")
original_path.rename(new_path)
print("~" * 30)


# Reading and writing files

"""The pathlib module provides several methods for 
reading from and writing to files, which reduces the need 
to use the standard open module. But they do not replace it, 
but are an addition.
"""


"""The read_text() and write_text() methods are used to read and write text files.
"""

# Syntax of the read_text() method

Path.read_text(encoding=None, errors=None)

"""
Parameters:
encoding - optional, the name of the encoding used to decode the file. 
If not specified, the default encoding is used.
errors - optional, instructions on how to handle decoding errors.
"""

# Syntax of the write_text() method

Path.write_text("data", encoding=None, errors=None)

"""
Parameters:
data - a line that must be written to the file.
encoding - optional, the name of the encoding used to decode the file. If not specified, the default encoding is used.
errors - optional, instructions on how to handle decoding errors."""

"""
As we can see, the errors parameter, in both methods, defines how these errors should be handled.

errors='strict'. This is the default value. 
If a decoding error occurs, a UnicodeDecodeError exception will be thrown.

errors='ignore'. If we want to ignore decoding errors. 
Parts of the text that cannot be decoded will simply be skipped.

errors='replace'. If we do not want to skip, then we will 
replace impossible to decode symbols with a special 
replacement symbol, according to the documentation, the symbol '?'.

"""
# An example of writing text to a file
# Creating a Path object for the file
file_path = Path("example.txt")
# Writing text to a file
file_path.write_text("Hello world!", encoding="utf-8")


# An example of reading text from a file
# Creating a Path object for the file
file_path = Path("example.txt")
# Reading text from a file
text = file_path.read_text(encoding="utf-8")
print(text)  # Hello world!
print("~" * 30)

"""The read_bytes() and write_bytes() 
methods are used to read and write binary files.
"""
# An example of writing binary data to a file
# Create a Path object for the binary file
file_path = Path("example.bin")
# Binary data to record
data = b"Python is great!"
# Writing bytes to a file
file_path.write_bytes(data)


# An example of reading binary data from a file
# Create a Path object for the binary file
file_path = Path("example.bin")
# Reading bytes from a file
binary_data = file_path.read_bytes()
print(binary_data)  # b'Python is great!'
print("~" * 30)
