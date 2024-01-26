# when importing a module, Python executes all the code contained in the module

"""What if we want to make an executable script (which can be called 
from the console with the command python [script name]), but keep t
he ability to import from this module without calling it?
"""


"""In such cases, the Python service variable: __name__ can help us. 
The thing is, if the script is called directly, then it is 
the "entry point" and __name__ == "__main__". If this module is executed 
during import, then __name__ == "mymodule" for a module called 
mymodule.py. This way we can modify our module mymodule.py:
"""

print("~" * 30)


def say_hello(name):
    print(f"Hello, {name}")


if __name__ == "__main__":
    print("You imported hello.py")
    say_hello("user")
print("~" * 30)

"""
Then, when importing the say_hello function from mymodule.py, 
the code in the if ... block will not be executed, 
but if you execute python mymodule.py in the console, it will.



For convenience, it is customary to put all the code that needs 
to be executed when the module is called from the console 
(not imported) into the main function:
"""


def say_hello(name):
    print(f"Hello {name}")


def main():
    print("You imported hello.py")
    say_hello("user")


if __name__ == "__main__":
    main()
print("~" * 30)


"""This is how the main function is called the "entry point"
 because the application starts with the call to this function. 
 You can, of course, call this function whatever you want, 
 but calling it main is considered good manners."""
