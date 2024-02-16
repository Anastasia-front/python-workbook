from contextlib import contextmanager
from datetime import datetime

"""A context manager in Python is a way of using resources 
that automatically ensures that a file is properly closed, 
regardless of whether an error occurred or not. 
This makes the code not only more readable, but also safer."""
print("~" * 30)

folder_path = "example"
file_path = f"{folder_path}/context_manager.txt"
# EXAMPLE 1
with open(file_path, "w") as file:
    file.write("This is some content for the file.")
# The file will automatically close after exiting the with block

# EXAMPLE 2
with open(file_path, "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open(file_path, "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)  # ['first line', 'second line', 'third line']

print("~" * 30)
# Creating your own context managers

"""
To create your own context manager, you need to implement a class 
with magic methods __enter__ and __exit__. The __enter__ method 
is called at the beginning of the 'with' block when the interpreter 
enters the context and what it returns will be written to the variable after as. 
The __exit__ method is called after the execution of the 'with' block 
has finished, whether or not an exception has been thrown.

Let's consider a rather abstract context manager to understand the principle of its operation.
"""


class MyContextManager:
    def __enter__(self):
        # Initialize the resource
        print("Enter the block")
        return self  # Can return an object

    def __exit__(self, exc_type, exc_value, traceback):
        # Freeing the resource
        print("Exit the block")
        if exc_type:
            print(f"Error detected: {exc_value}")
        # Returning False passes the exception on, True - absorbs the exception.
        return False


# Using your own context manager
with MyContextManager() as my_resource:
    print("Inside the block")
    # raise Exception("Something went wrong") - it is cause an error

# First output:
# Enter the block
# Inside the block
# Exit the block
print(
    """
    if line "raise Exception("Something went wrong")" would not be commented : \n
    Error detected: Something went wrong
Traceback (most recent call last):
   File "E:\\WebDir\\Works\\Python\\python-help-solution\\core_course\\topic7\\ex16.py", line 19, in <module>
     raise Exception("Something went wrong")
Exception: Something went wrong"""
)


"""
Now let's look carefully at the syntax of the __exit__ method. 
It takes three arguments that contain information about any 
exception that occurred inside the with block.
"""


def __exit__(self, exc_type, exc_val, exc_tb):
    # Freeing resources
    # exc_type: type of exception
    # exc_val: exclusion value
    # exc_tb: exception stack trace
    return False  # If True, the exception will be suppressed, otherwise, it will be raised further


"""
If the with block completed without an error, then the values of the variables 
exc_type , exc_val , exc_tb are None. But if there was an error, as in our example, 
the exc_type parameter will store the exception type <class 'Exception'>, 
exc_val the exception value "Something went wrong" and exc_tb the exception stack trace object 
<traceback object at 0x0000018A15310A80>. The __exit__ method should not catch exceptions, 
it is only needed to properly terminate the context 
(close open files and connections, return resources to the system, etc.).

As we can see, the creation mechanism is quite difficult. Therefore, Python allows you 
to create context managers using generators and the contextmanager decorator 
from the contextlib module. This simplifies the creation of context managers, 
especially when they are used for one-time or simple tasks.
"""


@contextmanager
def my_context_manager():
    # Initialize the resource
    print("Enter the block")
    try:
        yield  # Execution location of the `with` block
    except Exception as e:
        # Exception handling
        print(f"Error detected: {e}")
        # You can re-raise the exception or resolve it here
        raise
    finally:
        # Freeing the resource
        print("Exit the block")


print("~" * 30)
"""
The @contextmanager decorator is used to convert the my_context_manager function 
into a context manager. This allows the function to be used in the with ... as ... construct, 
making it easier to create context managers without having to define a class 
with __enter__ and __exit__ methods. The output of this code should be similar.

Let's create the FileManager class, which is designed 
to work with files and log the process of opening and closing a file.
"""


class FileManager:
    def __init__(self, filename, mode="w", encoding="utf-8"):
        self.file = None
        self.opened = False
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        self.opened = True
        print("Opening the file", self.filename)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("End of block with")
        if self.opened:
            print("Close the file", self.filename)
            self.file.close()
        self.opened = False

file_path = f"{folder_path}/new_file.txt"
if __name__ == "__main__":
    with FileManager(file_path) as f:
        f.write("Hello world!\n")
        f.write("The end\n")
print("~" * 30)

# Output :
# Open the file new_file.txt
# Completion of the with block
# Close the file new_file.txt

"""The @contextmanager decorator allows us to create a context manager 
using a generator, and simplify writing code compared to the FileManager 
class, which uses __enter__ and __exit__ methods.
"""


@contextmanager
def file_manager(filename, mode="w", encoding="utf-8"):
    print("Opening the file", filename)
    file = open(filename, mode, encoding=encoding)
    try:
        yield file
    finally:
        print("Close the file", filename)
        file.close()
        print("End of block with")


if __name__ == "__main__":
    with file_manager("new_file.txt") as f:
        f.write("Hello world!\n")
        f.write("The end\n")

print("~" * 30)
"""
In this code, the file_manager function is defined with the @contextmanager decorator.
It opens the file and prints the opening message, then uses yield to pass the file object 
to the context block. After exiting the 'with' block, the code in the finally block 
ensures that the file will be closed even if an exception occurs in the context block 
during execution, and prints a message that the file is closed and done with it.

This approach using @contextmanager makes the code more concise and readable, 
while retaining all the benefits of context managers for resource management.

Let's create a context manager that will manage the opening and closing of the file 
with additional logging. Our managed_resource context manager will measure the execution time 
of file operations and log file opening and closing actions along with their duration.
"""


@contextmanager
def managed_resource(*args, **kwargs):
    log = ""
    timestamp = datetime.now().timestamp()
    msg = f"{timestamp:<20}|{args[0]:^15}| open \n"
    log += msg
    file_handler = open(*args, **kwargs)
    try:
        yield file_handler
    finally:
        diff = datetime.now().timestamp() - timestamp
        msg = f"{timestamp:<20}|{args[0]:^15}| closed {round(diff, 6):>15}s \n"
        log += msg
        file_handler.close()
        print(log)


with managed_resource("new_file.txt", "r") as f:
    print(f.read())

# Output  :

# Hello world!
# The end

# 1707565076.245372 | new_file.txt | open
# 1707565076.245372 | new_file.txt | closed 0.004001.
print("~" * 30)

"""
In the process of work, before the file is opened, the current time is fixed, 
which allows you to generate a log message about the start of the operation with the file. 
This message contains a timestamp, the file name, and the action being performed at this stage - opening the file.



log = ''
timestamp = datetime.now().timestamp()
msg = f'{timestamp:<20}|{args[0]:^15}| open \n'
log += msg



The file is then opened using the passed parameters (filename, opening mode, encoding) 
and the file handle is returned to the with block. This allows you to perform various 
operations on the file, such as reading or writing. In our case, we simply read the lines of the file.



file_handler = open(*args, **kwargs)
try:
     yield file_handler


When exiting the 'with' block, the final part of the code is executed within the finally method. 
It includes logging about closing the file, which also records the timestamp and indicates 
the duration of operations with the file. The file is closed, and information about 
the entire process of opening, using and closing the file is displayed on the screen.

finally:
         diff = datetime.now().timestamp() - timestamp
         msg = f'{timestamp:<20}|{args[0]:^15}| closed {round(diff, 6):>15}s \n'
         log += msg
         file_handler.close()
         print(log)



Thus, our context manager not only simplifies working with files by automating 
the opening and closing processes, but also provides the additional benefit of detailed process logging 
instead of using the usual open(). This can be quite useful in diagnosing and analyzing the performance of our application.
"""
