"""
We can also use Union types. For example, a function can return only one of the types integer or float:
"""

from typing import Union

Number = Union[float, int]


def add(x: Number, y: Number) -> Number:
    return x + y
