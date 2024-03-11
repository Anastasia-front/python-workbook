"""
This is a special type that informs static type checking so that every type is compatible with this keyword.

Consider our old calculator function, which now accepts arguments of any type.
"""

from typing import Any, TypeVar

T = TypeVar("T", int, str, float)


def calculator(x: Any, y: Any) -> T:
    return x + y


print(calculator(3, 5))
print(calculator("Hello", "World"))
print(calculator(3.5, 1.4))


"""
This is not a very "good" type and should always be used consciously
"""
