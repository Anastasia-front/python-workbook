import sys

"""The sys module provides access to variables and functions 
related to Python itself and the operating system on which 
it is installed. This module also contains a lot of 
information about Python's import system."""


# Here are some key features of the sys module:

"""sys.argv - list of command line arguments passed to the Python script. 
The argv[0] element is the name of the script, and the other 
elements are additional command line arguments.

sys.exit() - Python exit function. You can pass a numeric argument 
that will be the program's exit status. An argument of 0 is assumed 
to indicate success, and non-zero values to indicate an error.

sys.path - a list of strings that defines the search path of the interpreter 
for modules. You can modify this list to add your own paths to find modules.

sys.version - A string containing information about the version of Python being used.

sys.platform - A string indicating the name of the platform 
on which Python is running (eg 'linux' for Linux, 'win32' for Windows).

sys.modules - a dictionary that contains loaded modules.
Keys are module names and values are module objects.


First of all, let's get a list of modules imported at the moment 
using the sys.modules variable. This is a dictionary where the key is the name 
of the module you want to check and the return value is the module object.

"""

# For example, once the os module is imported, you can return its value:
print("~" * 30)
print(sys.modules["os"])
print(sys.modules["enum"])
print("~" * 30)

"""The output will be the path where the os module is located 
when the script is executed. In your case, of course, the output 
may be different, it all depends on the system, Python version, etc.:
"""

# <module 'os' from 'C:\\Users\\Krabat\\AppData\\Local\\Programs\\Python\\Python310\\lib\\os.py'>


"""The sys.modules variable is a regular Python dictionary 
that holds all the loaded modules. This means that, for example, 
a call to sys.modules.keys() will return the full list of loaded module names.
"""

print(sys.modules.keys())  # dict_keys(['...','...','...',...])
print("~" * 30)

"""You can get a list of modules built into the language using 
the sys.builtin_module_names variable. The built-in modules that 
are compiled into the interpreter will depend on the parameters 
passed when the program was compiled.
"""

print(sys.builtin_module_names)  # ('...','...','...',...)
print("~" * 30)

"""
When importing a module, Python relies on a list of paths to find it. 
search This list is stored in the sys.path variable. 
To check which paths the interpreter will search for modules, print sys.path.



You can change this list, add or remove paths as needed. 
There is no need to change the path variable for the normal 
operation of the program. Note that the search for the necessary 
module will be performed through the list, so the order of the paths 
in sys.path is important. It is convenient to place the paths that 
are more likely to contain the modules you are looking for at the 
beginning of the list to speed up the search. This also ensures that 
if there are two modules with the same name, the first one will be selected. 
The last property is especially important because of one common mistake: 
overlapping calls to Python's built-in modules with custom modules. 
At the beginning of the import, the working directory of the project is viewed, 
and then the standard library. This means that if you name your script random.py 
and try to import random, it will import your script instead of the Python built-in library.


When we run a script saved in a Python file, it is possible to pass 
some arguments to it at launch, as in a function. Then our script 
can accept these arguments and somehow change its behavior. This can be done 
using the sys package, which contains the argv list, where all 
the arguments with which the script was launched appear.
"""
"""
An interesting feature of sys.argv is that the first element 
of this list will be the name of the script file itself. 
All arguments will be in sys.argv as strings in the same order 
in which they were passed during the call. Python separates 
arguments with spaces and spaces do not enter sys.argv.

To understand how sys.argv works, you can make a simple echo.py script 
that will output to the console all the arguments passed during the call.
"""
# If you run the echo.py script with the following command:
# python3 example/sys/echo.py test --user -hello some text

# code in example/sys/echo.py

for arg in sys.argv:
    print(arg)
print("~" * 30)

print(
    "Output after run command - python3 example/sys/echo.py test --user -hello some text: \n\
            example/sys/echo.py\n\
            test\n\
            --user\n\
            -hello\n\
            some\n\
            text"
)
print("~" * 30)


"""
Let's create an arg.py script to handle the first startup argument:
"""

# When calling such a script by command
#  python3 example/sys/arg.py 123


# code in example/sys/arg.py 123
def main():
    if len(sys.argv) > 1:
        print(sys.argv[1])


if __name__ == "__main__":
    main()


print(
    "Output after run command - python3 example/sys/arg.py 123: \n\
            123"
)
print("~" * 30)


"""
You will see in the console 123. Note that all items in the sys.argv 
list are always strings. If you expect the user to enter a number 
(integer or fraction), then you need to convert the string to the 
type you want yourself. And also always check, in our example if 
len(sys.argv) > 1:, whether the required number of arguments 
were passed when the program was started.

The sys module is a very powerful tool for interacting with the system 
and the Python interpreter, which provides a lot of flexibility 
when writing scripts and programs."""
