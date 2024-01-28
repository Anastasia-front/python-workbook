syntax = "map(function, iterable, ...)"

"""
function - a function that should be applied to each element in the iterable.
iterable - an iteration object (list, tuple, etc.), 
the elements of which will be processed by the function.
"""

# Let's use map to write a generator that squares the numbers from the numbers list:


print("~" * 30)
numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x**2, numbers):
    print(i)
# 1
# 4
# 9
# 16
# 25

print("~" * 30)

"""
As the first argument to map, we passed the lambda function 
lambda x: x ** 2, which returns x to the power of 2.

As a result of the execution of the expression map(lambda x: x ** 2, numbers) 
we will get a generator that we used in the for loop and output 
the value at each iteration with the print function.
"""


# If we want to get a list, and not a generator, then the code can be written like this:

numbers = [1, 2, 3, 4, 5]

squared_nums = list(map(lambda x: x**2, numbers))
print(squared_nums)  # [1, 4, 9, 16, 25]
print("~" * 30)

# You can apply map to multiple lists:

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = map(lambda x, y: x + y, nums1, nums2)

print(list(sum_nums))  # [5, 7, 9]
print("~" * 30)

"""
But after List comprehensions appeared in Python, 
it is used for the same purpose, which provides greater readability and expressiveness.
"""


# Instead of using the map() function:

numbers = [10, 9, 8, 7, 6]

squared_nums = list(map(lambda x: x**2, numbers))
print(squared_nums)  # [100, 81, 64, 49, 36]
print("~" * 30)
# We will use list comprehensions:

nums = [11, 21, 33, 44, 55]
squared_nums = [x * x for x in nums]
print(squared_nums)  # [121, 441, 1089, 1936, 3025]
print("~" * 30)

# For two lists, we can also use list comprehensions using the zip function

nums1 = [11, 22, 33]
nums2 = [4, 5, 6]
sum_nums = [x + y for x, y in zip(nums1, nums2)]
print(sum_nums)  # [15, 27, 39]
print("~" * 30)

"""
In general, the advantages of list comprehensions 
are readability and flexibility. However, the choice between 
map() and list comprehensions depends on the specific situation 
and the preferences of the programmer.
"""
