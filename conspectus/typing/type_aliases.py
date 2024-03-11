"""
Because objects such as lists, dictionaries, and tuples contain other objects, 
we sometimes need to introduce hints to indicate what types of objects they contain. 
To do this, we need to refer to the typing module, which provides tools for describing types.
"""

from typing import Dict, List

Data = List[float | int]


def my_mul(data: Data) -> float:
    result = 1
    for num in data:
        result = result * num
    return result


my_mul([1, 2, 3])

"""
In the above fragment, there is an alias Data, which is decoded as 
a list of values of integer values of int or floating point float.

You can describe dictionary types by providing them as a list:
"""

dict_of_users: Dict[int, str] = {1: "Jane", 2: "John"}
