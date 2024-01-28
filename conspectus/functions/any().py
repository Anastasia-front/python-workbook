'''The any() function is a built-in function that returns True 
if at least one element of the given iteration object is true. 
If the iteration object is empty or all its elements are false, then any() returns False.
'''

print("~" * 30)
nums = [0, False, 5, 0]
result = any(nums)
print(result)
# The code will return True because 5 is a true value in the nums list
print("~" * 30)


'''
You can pass a generator or list comprehension to the function. 
For example, let's check if there are even numbers in the list?
'''


nums = [1, 3, 5, 7, 9]
result = any(x % 2 == 0 for x in nums)
print(result)
# The code will return False because there are no even numbers in the nums list
print("~" * 30)


'''
The main use of the any function is in scenarios where you need to determine 
if at least one element in a collection meets a certain condition. 
It is quite often used in combination with other functions, 
such as map() or list comprehensions, for more complex validation conditions.
'''

