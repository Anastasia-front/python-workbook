"""We can annotate a function to specify its return type and the types of its parameters.
"""


def my_mul(data: list) -> float:
    result = 1
    for num in data:
        result = result * num
    return result


"""
This tells the type checker that we have a mul function that will take data as an argument and return a float

We call our function with an incorrect data parameter
"""

my_mul(1)


"""
For example, in the PyCharm IDE this will result in a warning that the types of the parameter 
being passed and expected do not match Expected type 'list', got 'int' instead

This triggers the built-in type checking inside the PyCharm IDE.

And the function call with the list will be correct, because it completely matches the description.
"""


my_mul([1, 2, 3])

"""
One of the most widely used type checkers is the mypy package. Unless you're using VSCode or PyCharm, 
for example, or you need to check typing in the console.

The package can be installed as follows:
"""

# pip install mypy

"""You can then run any Python file to check if the types match."""

# mypy main.py

"""After debugging, you can run the program in normal mode."""
