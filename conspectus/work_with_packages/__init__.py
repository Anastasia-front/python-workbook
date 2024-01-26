"""In versions of Python prior to 3.3, it was necessary to place 
the helper file __init__.py in packages. If this is not done, 
then Python did not perceive the directory as a package and 
could not import anything from such a directory. There is no need 
for this now, but often such files are created for backward compatibility with older versions.



The __init__.py file is a service file that the interpreter 
must execute the first time a package is imported. That way, 
if you need to do something while importing a package, you can write it in __init__.py.



Normally __init__.py is empty and does nothing. But when the package structure 
is not too simple and there are many modules and/or packages that the user 
doesn't need to know about, you can import what the user needs in __init__.py. 
In this case, the user will be able to write abbreviated variants of imports in his code.



For example, the utility package has two packages: useful and dummy. 
Each of them has a functions.py module (each has its own). And these 
modules already have nice_function and not_bad functions, respectively.
"""


def nice_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


def not_bad(s: str) -> str:
    if s.find("not") == -1 or s.find("bad") == -1:
        return s
    else:
        return s.replace("not bad", "good")


# The structure of the project will look like this:

#   📦example_init
#   ┣ 📂utility
#   ┃ ┣ no_params
#   ┃ ┃ ┗ 📜functions.py
#   ┃ ┣ str_param
#   ┃ ┃ ┗ 📜functions.py
#   ┃ ┗ 📜__init__.py
#   ┗ 📜main.py

"""
For the user of the utility package, it is not necessary 
to know about the internal structure of the package, 
because it is made for the convenience of the developer 
of the package. The developer wrote the utility to give 
the user access to nice_function and not_bad.



If you leave the __init__.py file empty, using the 
nice_function and not_bad functions will look something like this:
"""

# import utility

# utility.useful.functions.nice_function()
# utility.dummy.functions.not_bad("Test string")

"""
This is very inconvenient and the user of the package 
will need to understand where and what is there.

If the developer thought about the user, then __init__.py should look like this:

"""


# from utility.useful.functions import nice_function
# from utility.dummy.functions import not_bad

# __all__ = ['nice_function', 'not_bad']

"""
Note that the __all__ constant is a list of modules 
or packages that are imported if the from ... import * 
expression ends with a * character.

Now you can use the following import of functions from the package:"""


# from utility import nice_function, not_bad

# nice_function()
# not_bad("Test string")


"""or like this:"""


# from utility import *

# nice_function()
# not_bad("Test string")


"""Everything should work without errors."""
