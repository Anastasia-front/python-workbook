import shutil

shutil_package = "represents a more advanced file manager\
    and knows how to work with archives.\
    The shutil package supports zip, tar, gz archives. \
    It uses zipfile and tarfile packages for this. \
    You can use them directly if you want."


"""The shutil.make_archive() function in Python is used to 
create archives (such as ZIP or TAR files) from a given directory. 
This function is part of the shutil module, which provides 
many convenient operations for working with files, 
including copying and archiving.
"""


syntax = "shutil.make_archive(base_name, format, root_dir=None, base_dir=None)"
parameters = """
base_name - the path to the file where 
you want to save the archive, without the extension.

format - the format of the archive, 
for example 'zip', 'tar', 'gztar', 'bztar' or 'xztar'.

root_dir - the directory from which the archive will be created. 
If not specified, the current directory is used.

base_dir - the directory inside the archive from which the archiving will start.
"""

# creates the archive in the current working directory
# move the archive from the current working directory 
# to the desired destination inside the source directory
def create_and_move_archive(base_name, format, source_dir):
    # Create the archive in the current working directory
    archive_path = shutil.make_archive(base_name, format, root_dir=source_dir)

    # Move the archive to the source directory
    destination_path = f"{source_dir}/{base_name}.{format}"
    shutil.move(archive_path, destination_path)

print("~" * 30)
# Creating a ZIP archive with the contents of the directory 'my_folder'
print("shutil.make_archive('example', 'zip', root_dir='example')")
create_and_move_archive("example", "zip", "example")
# shutil.make_archive("example", "zip", root_dir="example")
print("~" * 30)

"""This code will create a zip archive named example.zip 
containing all the files and subdirectories 
found in the my_folder directory."""


# Creating a TAR.GZ archive
print("shutil.make_archive('example', 'gztar', root_dir='example')")
create_and_move_archive("example", "gztar", "example")
# shutil.make_archive("example", "gztar", root_dir="example")
print("~" * 30)

"""In this case, a TAR archive
 with GZIP compression is created.
"""


"""Why do we need archiving? 
This is the automation of the process of creating backup 
copies of files and directories. Creating archives of software code, 
resources or documentation for further distribution.
Archiving to reduce the amount of disk space used or 
to simplify the transfer of files over the network.
"""


"""Of course, the shutil package supports unpacking archives. 
The shutil.unpack_archive() function is used to unpack archive 
files such as ZIP or TAR to the specified directory. 
This is a convenient way to automate the unpacking 
process without having to manually use archive tools.
"""


syntax = "shutil.unpack_archive(filename, extract_dir=None, format=None)"
parameters = """
filename - the path to the archive file to be unpacked.

extract_dir - the directory where the contents of the archive will be extracted. 
If not specified, the current directory is used.

format - archive format, for example, zip, tar, gztar, bztar, or xztar. 
If no parameter is specified, Python tries to determine the format automatically.
"""


# Unpacking the zip archive:
# Extracting the ZIP archive to a specific directory
print("shutil.unpack_archive('example.zip', 'example')")
shutil.unpack_archive("example.zip", "example")
print("~" * 30)

"""This code will extract the contents of 
example.zip into the destination_folder directory."""
