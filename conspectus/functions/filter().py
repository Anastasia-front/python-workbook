"""
The filter() function is used to filter iteration objects, 
such as lists or tuples, using a given function. It creates
an iterator that contains only those elements of the iteration 
object for which the filter function returns True.

Recall that in Python, any type can be converted to a boolean. 
0, None, and empty containers are set to False. 
Strings, lists, dictionaries, sets, tuples, all other cases evaluate to True.
"""


syntax = "filter(function, iterable)"

"""
function - a function that determines whether an element 
should be included in the result. This function must 
take one argument and return a Boolean value of True or False.

iterable - an iteration object (for example, a list, a tuple), 
the elements of which will be checked by the function function.
"""

# For example, let's display a list of numbers that are even in the interval from 1 to 10:
print("~" * 30)
even_nums = filter(lambda x: x % 2 == 0, range(1, 11))
print(list(even_nums))  # [2, 4, 6, 8, 10]
print("~" * 30)

# It is not necessary to use the lambda function.


def is_positive(x):
    return x > 0


nums = [-2, -1, 0, 1, 2]
positive_nums = filter(is_positive, nums)
print(list(positive_nums))  # [1, 2]
print("~" * 30)

# Another example, let's filter out letters from a string so that only lowercase letters remain:

some_str = "Publisher A-BA-BA-HA-LA-MA-HA"

new_str = "".join(list(filter(lambda x: x.islower(), some_str)))
print(new_str)  # ublisher
print("~" * 30)

"""
While filter() can be useful for many scenarios, 
in some cases list comprehensions can provide a more 
readable and efficient way to achieve the same goals.
"""


# Consider how you can replace filter() with list comprehensions:

nums = [1, 2, 3, 4, 5, 6]
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums)  # [2, 4, 6]
print("~" * 30)

# For a string of letters:

some_str = "Publisher A-BA-BA-HA-LA-MA-HA"

new_str = "".join([x for x in some_str if x.islower()])
print(new_str)  # ublisher
print("~" * 30)

"""
However, in general, the choice between using filter() 
and list comprehensions depends on the specific case 
and the personal preferences of the programmer."""
