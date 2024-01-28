"""
The all() function is a built-in function that returns True 
if all the elements in the iteration object passed to it are true 
- that is, not False, 0, "", None, or any other value that Python 
evaluates to false. But be careful, if the iteration object 
is empty, the all() function returns True.
"""

print("~" * 30)
nums = [1, 2, 3, 4]
result = all(nums)
print(result)
# The code will return True because all the numbers are true.
print("~" * 30)


# Let's consider more complex examples and check the list for some condition.

nums = [1, 2, 3, 4]
is_all_even = all(x % 2 == 0 for x in nums)
print(is_all_even)
# The code will output False because not all numbers in the nums list are even.
print("~" * 30)

words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case)
# Here, the code will return True because all words start with an uppercase letter.
print("~" * 30)

"""
The all() function is a useful tool when you want to check that 
the entire collection of data meets certain requirements or conditions, 
such as all elements are true, all numbers are even, all strings follow 
a certain format, and so on. This provides an elegant way to test conditions 
that apply to all elements of an iteration object, 
instead of using loops or more complex constructs.




In general, using the any(), all(), map(), filter(), and comprehensions 
techniques provides cleaner, more concise, and more efficient code, 
especially when working with data and collections.
"""
