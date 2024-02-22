"""
Creating copies of objects in Python can be a non-trivial task, 
depending on whether you want a shallow or deep copy, 
as well as the complexity of the object's data structure.

Python tries to save memory and not copy data from one area of memory to another. 
Instead, the interpreter creates a new reference, another alias, 
to the actual object instead of copying the contents.
Such behavior may be undesirable, consider for example:
"""
print("~" * 30)

my_list = [1, 2, 3]
copy_list = my_list
copy_list.append(4)
print(my_list)  # [1, 2, 3, 4]
print("~" * 30)

"""
It turns out that copy_list is just another name for the same list my_list and when we change copy_list 
we change my_list too. This is not obvious and can be confusing.

This behavior can lead to errors when dealing with mutable types, dictionaries, lists, user classes.

Consider an example where we pass a list to the middle of a function, and it changes it:
"""

my_list = [1, 2, 3]

def square_list(x: list):
    for i, el in enumerate(x):
        x[i] = el**2
    return x


new_list = square_list(my_list)
print(new_list)  # [1, 4, 9]
print(my_list)  # [1, 4, 9]
print("~" * 30)

"""
As you can see, the list my_list has undergone changes, and perhaps this is completely 
undesirable behavior. In the example, the square_list function takes a list x as an argument 
and modifies it by squaring each element. It turns out that the function modifies the input list 
without creating a new list. So when we passed my_list to square_list, the original my_list is changed.

If we want to keep the original my_list unchanged and create a new list with boxes of elements, 
then we should create a copy of the list before modifying it, or change the function to return 
a new list with boxes of elements instead of changing the input list. 
"""

my_list = [1, 2, 3]

def square_list(x: list):
    return [el**2 for el in x]

new_list = square_list(my_list)
print(new_list)  # [1, 4, 9]
print(my_list)  # [1, 2, 3]

print("~" * 30)

"""
As you can see, the original my_list now remains unchanged.

For lists and dictionaries, you can use explicit copying:
"""

copy_list = my_list[:]
copy_list.append(4)
print(my_list, copy_list)  # [1, 2, 3] [1, 2, 3, 4]

my_dict = {1: "a"}
copy_dict = {**my_dict}
copy_dict["new_key"] = "new_value"
print(my_dict, copy_dict)  # {1: 'a'} {1: 'a', 'new_key': 'new_value'}

print("~" * 30)
"""
The statement copy_list = my_list[:] creates a new copy_list that is a shallow copy of my_list. 
Modifying copy_list like adding element 4 does not affect my_list now. When the dictionary 
copy_dict = {**my_dict} is created, the ** dictionary unpack syntax is used to create 
a new copy_dict dictionary that is a copy of my_dict.

Now, any modifications to copy_dict, such as adding a "new_key": "new_value" key-value pair, 
do not affect the original my_dict dictionary.

Both of our examples illustrate how to get a new, independent object through slice for lists 
or unpack for dictionaries. But with class objects and user types it's so easy, you can't do it. 
To solve this problem, Python has a copy mechanism, the functions from the copy package.
"""
