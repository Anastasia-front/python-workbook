"""
Generics or universal types. Let's imagine a situation where we have a function 
that adds two parameters and returns the result - the sum of these parameters. 
These parameters can be strings, integers, or real numbers. To avoid code repetition 
and not to write a function with its own types for each case, we use generics.
"""

from typing import TypeVar

T = TypeVar("T", int, str, float)


def calculator(x: T, y: T) -> T:
    return x + y


print(calculator(3, 5))
print(calculator("Hello", "World"))
print(calculator(3.5, 1.4))

# Output
# 8
# HelloWorld
# 4.9
