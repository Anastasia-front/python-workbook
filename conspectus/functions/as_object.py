from typing import Callable, Dict

# Functions as an object of the first class

# functions as arguments
"""Functions can be arguments to other functions. 
Suppose we have several functions to calculate various mathematical operations. 
We can create a function apply_operation that takes another function 
as an argument and uses it to calculate the result.
"""


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)


# Usage
result_add = apply_operation(5, 3, add)
result_multiply = apply_operation(5, 3, multiply)

print(result_add, result_multiply)  # 8 15
print("~" * 30)

"""When we add a function as an argument to add typing 
to these functions in Python, the type annotations from 
the typing module are used. The apply_operation function
has the already familiar type annotations for a and b, 
but the operation parameter is annotated as Callable[[int, int], int]. 
This means that the operation parameter is a function 
that takes two integers and returns an integer."""

# functions can return other functions
"""Functions as an object of the first class can return other functions.
For example, we can create a function that generates 
another function to raise a number to a given power.
"""


def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base**exponent

    return inner


# Usage
square = power(2)
cube = power(3)

print(square(4))  # 16
print(cube(4))  # 64
print("~" * 30)

"""The power function takes one exponent argument and returns 
the inner function. The inner function inner takes a base 
and uses the stored exponent to calculate the base ** exponent.

When we call power(2), we actually create a new square function 
with an exponent of 2. Similarly, power(3) creates a cube function with an exponent of 3.

When square(4) is ''called, the inner function evaluates to 4 ** 2, which returns 16. 
Similarly, cube(4) evaluates to 4 ** 3, which returns 64."""

# storing functions in data structures
"""And last but not least: this is storing functions in data structures. 
For example, let's create a dictionary where the keys are the names of operations, 
and the values are the corresponding functions.
"""


# Definition of functions
def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base**exponent

    return inner


# Using power to create square and cube functions
square = power(2)
cube = power(3)

# Dictionary of operations
operations: Dict[str, Callable] = {
    "add": add,
    "multiply": multiply,
    "square": square,
    "cube": cube,
}

# Using operations
result_add = operations["add"](10, 20)  # 30
result_square = operations["square"](5)  # 25

print(result_add)  # 30
print(result_square)  # 25
print("~" * 30)

"""Our operations dictionary contains references to all four of our functions. 
And now, through operations, add or square operations are performed with 
the appropriate arguments. Where the dictionary key is the name of our functions.

Note that the type Dict[str, Callable] means a dictionary where the keys 
are strings and the values are callable objects. In the context of operations: 
Dict[str, Callable], this means that the dictionary contains the names of operations 
and references to functions that perform those operations.



Thus, you can work with functions in Python in the same way as with any other objects. 
"""
