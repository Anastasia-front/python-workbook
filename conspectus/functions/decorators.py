from functools import wraps

"""There is such a design template — Decorator. This pattern consists 
in extending the functionality that already exists without 
making changes to the code of this functionality.

Decorators in Python are a very powerful and useful tool 
that allows you to change the behavior of functions or methods 
without changing their source code. They are an example of 
higher-order functions that take another function as an argument and return a new function.


For example, we have a very complicated and important complicated function:"""

# def complicated(x: int, y: int) -> int:
#      return x + y


"""And we don't want to change its code for any reason. 
But we need to add logging to this function, output to the console
every time it is called, what arguments it was called with, and what it returned as a result."""


def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Calling function: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Function {func.__name__} completed execution: {result}")
        return result

    return inner


@logger
def complicated(x: int, y: int) -> int:
    return x + y


print("~" * 30)
print(complicated(2, 3))
print("~" * 30)

"""
The logger function is a decorator. It takes a func function 
and returns a new inner function. The inner function performs 
additional actions (logging) before and after the execution of func. 
When declaring the complicated function, we use @logger to apply the decorator. 
Now, each time complicated is called, additional logging actions will be performed.
Now it is clearly visible in the code that complicated was decorated 
with a logger in the same place where complicated was declared.

Decorators are widely used for various purposes. The main applications are:

Logging - recording information about function calls for transparency and traceability.
Access Check - Checking user rights before executing a function to control access.
Caching - saving the results of a function to improve efficiency and reduce execution time.
Argument Validation - Analysis and modification of arguments before 
they are passed to a function to ensure the correctness of the call.


It is very important to use the functools module when creating decorators, 
it is necessary to save the metadata of the original function that we are decorating. 
The function functools.wraps helps with this by preserving information 
about the original function, such as the function name and documentation.
"""


def logger(func):
    @wraps(func)
    def inner(x: int, y: int) -> int:
        print(f"Calling function: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Function {func.__name__} completed execution: {result}")
        return result

    return inner


@logger
def complicated(x: int, y: int) -> int:
    return x + y


print(complicated(2, 3))  # The function: complicated: 2, 3 is called
# The complicated function has completed execution: 5
# 5
print(complicated.__name__)  # complicated
print("~" * 30)


"""
In this example, functools.wraps(func) is applied to the inner function. 
It "copies" metadata (function name, documentation, etc.) from func to inner. 
Because of this, when we call print(complicated.__name__), we get the metadata 
of the original complicated function, not the inner function from the logger decorator.

This is important to preserve the expected functionality of the decorated function, 
especially when working with decorators in more complex programs or libraries. 
Using functools.wraps helps avoid the confusion of losing the metadata of the original function.
"""

print("dir(wraps)")
print(dir(wraps))
print("~" * 30)
