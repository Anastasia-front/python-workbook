import copy

"""
To create a "shallow" ("поверхневу") copy of an object, the copy package has a copy function. 
This function creates a new object of the same type and then references all the contents 
of the old object to the new one. This mechanism is quite good for working with objects 
where there are no variable objects already at the first level of nesting, and it works quite quickly.
"""
print("~" * 30)

my_list = [1, 2, {"name": "Kevin"}]
copy_list = copy.copy(my_list)
copy_list.append(4)
print(my_list)  # [1, 2, {'name': 'Kevin'}]
print(copy_list)  # [1, 2, {'name': 'Kevin'}, 4]

print("~" * 30)

"""A shallow copy means that the new list copy_list will contain new references 
to the same objects as the original list and for objects with deep nesting such 
a function will still not give the desired effect. Therefore nested objects, 
such as the dictionary in the third element of the list, will be shared between the original and copied lists.
"""


my_list = [1, 2, {"name": "Kevin"}]
copy_list = copy.copy(my_list)
copy_list[2]["age"] = 30
print(my_list)  # [1, 2, {'name': 'Kevin', 'age': 30}]
print(copy_list)  # [1, 2, {'name': 'Kevin', 'age': 30}]

print("~" * 30)

""" 
From this example, it can be seen that although copy_list is already a new object, 
the dictionary nested in it with index 2 is the same dictionary in both copy_list and my_list.

Surface copy creates a new object, but does not copy nested objects. Instead, it copies only references 
to nested objects. This means that if you change nested objects in the original, 
those changes will also be reflected in the surface copy.
"""


# Creating deep copies of Python objects


""" 
A deep copy creates a new object and recursively copies all nested objects. 
As a result, you get a completely independent copy of the original object.

To create a deep copy, use the deepcopy() method of the copy module. This function recursively creates new objects.
"""


my_list = [1, 2, {"name": "Kevin"}]
copy_list = copy.deepcopy(my_list)
copy_list[2]["age"] = 30
print(my_list)  # [1, 2, {'name': 'Kevin'}]
print(copy_list)  # [1, 2, {'name': 'Kevin', 'age': 30}]

print("~" * 30)

"""
Depending on the task, it may be sufficient for you to use a shallow copy, 
or you may need a deep copy to ensure complete data independence. 
The key is to understand the structure and dependencies of the data 
in your object in order to choose the right copy method.
"""
