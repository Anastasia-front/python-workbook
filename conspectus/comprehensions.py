"""Comprehensions in Python are a way to compactly create collections 
based on existing collections. Python supports several types of comprehensions: 
for lists (list comprehensions), sets (set comprehensions), 
and dictionaries (dictionary comprehensions). They allow you to write expressions 
to create new collections with less code than using loops.
"""


# List Comprehensions
syntax = "[new_item for item in iterable if condition]"

print("~" * 30)
sq = [x**2 for x in range(1, 6)]
print(sq)  # [1, 4, 9, 16, 25]
print("~" * 30)

"""A condition in the syntax allows us to create lists based on some condition. 
Let's create a list of squares of even numbers from 1 to 9:
"""


even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64]
print("~" * 30)

# Set Comprehensions

syntax = "{new_item for item in iterable if condition}"

# Let's save the sets of squares of numbers from the list:

numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i**2 for i in numbers}
print(sq)  # {1, 4, 36, 9, 16, 25}
print("~" * 30)

"""Set Comprehensions also support conditions. 
Let's create a set of squares of odd numbers from 1 to 9:
"""

odd_squares = {x**2 for x in range(1, 10) if x % 2 != 0}
print(odd_squares)  # {1, 9, 81, 49, 25}
print("~" * 30)


# Dictionary Comprehensions

"""Dictionary comprehensions are used to create new dictionaries. 
For dictionaries, the comprehension syntax is slightly different, 
as you need to explicitly specify the key and value
"""

syntax = "{key: value for item in iterable if condition}"


"""Let's create a dictionary where the key is a number, and the value is its square.
"""


sq = {x: x**2 for x in range(1, 10)}
print(sq)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print("~" * 30)

"""Let's create a dictionary where the keys are numbers, 
and the values are their squares, but only for numbers greater than 5:
"""


sq_dict = {x: x**2 for x in range(1, 10) if x > 5}
print(sq_dict)  #  {6: 36, 7: 49, 8: 64, 9: 81}
print("~" * 30)

"""Comprehensions are ideal for simple cases where you need to transform 
the elements of a collection or filter them based on a certain condition.
They make the code more readable and reduce the need for multi-line loops 
and conditionals. However, it is important to use them with care so as not 
to overload a single line with too much complex logic."""
