"""lambda functions, also known as anonymous functions, 
are an important part of Python and are used to create small, one-line functions.
"""

syntax = "lambda arguments: expression"

"""Here, lambda is the keyword that points to the beginning of the lambda function. 
arguments is the list of arguments that the function takes, 
and expression is the expression that will be executed and its result returned.
"""

print("~" * 30)
# add = lambda x, y: x + y
# print(add(523, 3))  # Output 526
# print("~" * 30)


"""In the example, we created a lambda function add that returns the sum of two numbers.
In fact, it is "bad tone" to store lambda functions in variables, 
they should be created where they will be used and leave no traces anywhere else in the code.
"""


print((lambda x, y: x + y)(5, 3))  # Output 8
print("~" * 30)

"""
So what we see. Lambda functions do not have a name.
 Usually used for writing short functions. Can contain 
 only one expression and cannot contain command blocks 
 such as loops or conditional constructs.

Lambda functions are often used as arguments to higher-order functions 
such as map(), filter(), or sorted(). For example, reverse sorting a list for sorted():
"""


nums = [1, 2, 3, 4, 5]
nums_sorted = sorted(nums, key=lambda x: -x)
print(nums_sorted)  # [5, 4, 3, 2, 1]
print("~" * 30)


"""Lambda functions are ideal for performing small functional operations 
that do not require writing a separate named function. They are a useful tool in Python, 
but should be used with care to keep the code readable. In cases where the logic becomes complex, 
it is better to use regular functions with a defined name."""
