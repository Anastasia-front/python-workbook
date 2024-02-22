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

# Control the order of copying Python objects

"""
Another problem that is solved using the copy package is copying user objects.

To create an object that will be handled correctly by the copy and deepcopy functions, 
the given class must implement two magic methods: __copy__ and __deepcopy__ for shallow and deep copying, respectively.


When we call copy.copy() or copy.deepcopy() on an object, Python automatically looks 
for and calls these magic methods in the object's class, if they are defined.



__copy__ should return a shallow copy of the object.
__deepcopy__ should return a deep copy of the object. 
It takes an additional memo argument, which is a dictionary used to avoid infinite recursion 
when copying nested objects that reference themselves.


First, consider a simple example of a class that implements both of these methods:
"""


class MyClass:
    def __init__(self, value):
        self.value = value

    def __copy__(self):
        print("Called __copy__")
        return MyClass(self.value)

    def __deepcopy__(self, memo=None):
        print("Called __deepcopy__")
        return MyClass(copy.deepcopy(self.value, memo))


# Surface copying
obj = MyClass(5)
obj_copy = copy.copy(obj)
obj_copy.value = 10

# Deep copy
obj_deepcopy = copy.deepcopy(obj)
obj_deepcopy.value = 20
print(obj.value, obj_copy.value, obj_deepcopy.value)

# Output
# Called by __copy__
# Called by __deepcopy__
# 5 10 20

print("~" * 30)

"""In our example, calling copy.copy(obj) will create a new instance of MyClass with the same value. 
Calling copy.deepcopy(obj) will also create a new instance, but using copy.deepcopy for the value, 
which enables a deep copy of any nested objects.

As you can see, everything works correctly. The only thing not covered here is that __deepcopy__ 
uses the memo dictionary. The memo dictionary is used to keep track of objects 
that have already been copied during the current deep copy operation.


When __deepcopy__ is called on an object, it checks whether a copy of that object already exists 
in the memo dictionary. If so, the method returns a reference to the already copied object 
instead of creating a new copy. This prevents multiple copies of the same object 
during deep copying and avoids infinite recursion.


In the memo dictionary, the keys are the object id identifiers, and the values are the already copied objects. 
This allows you to quickly check whether an object has already been processed during the current copy operation.


Now consider a more complex example with nested objects:
"""


class SimpleObject:
    def __init__(self, greeting: str):
        self.greeting = greeting


class ComplexObject:
    def __init__(self, value: int, nested_obj: SimpleObject):
        self.value = value
        self.nested_obj = nested_obj

    def __copy__(self):
        print("Called __copy__ for ComplexObject")
        # Shallow copy does not copy nested objects deep
        return ComplexObject(self.value, self.nested_obj)

    def __deepcopy__(self, memo=None):
        print("Called __deepcopy__ for ComplexObject")
        # Deep copy copies nested objects
        return ComplexObject(
            copy.deepcopy(self.value, memo), copy.deepcopy(self.nested_obj, memo)
        )


nested_obj = SimpleObject("Hello")
complex_obj = ComplexObject(5, nested_obj)

# We create a copy and a deep copy
complex_obj_copy = copy.copy(complex_obj)
complex_obj_deepcopy = copy.deepcopy(complex_obj)

# We change the value of the nested object nested_obj
nested_obj.greeting = "Hello"

# Let's see the changes in the objects
print(f"Copy object: {complex_obj_copy.nested_obj.greeting}")
print(f"Deepcopy object: {complex_obj_deepcopy.nested_obj.greeting}")
print("~" * 30)
# Output
# Called __copy__ on ComplexObject
# Called __deepcopy__ on ComplexObject
# Copy object: Hello
# Deepcopy object: Hello


"""
In this example, ComplexObject contains a nested object of class SimpleObject. 
When __copy__ is shallowly copied, the self.nested_obj nested object is not deeply copied, 
so when we make changes to the original nested_obj object, they will also affect the copy, 
which we see in the output. With __deepcopy__, the nested self.nested_obj is also copied deep, 
making the copy completely independent of the original.

In fact, even without the implementation of these magical methods, everything will work as it should.
"""


class SimpleObject:
    def __init__(self, greeting: str):
        self.greeting = greeting


class ComplexObject:
    def __init__(self, value, nested_obj: SimpleObject):
        self.value = value
        self.nested_obj = nested_obj


nested_obj = SimpleObject("Hello")
complex_obj = ComplexObject(5, nested_obj)

# We create a copy and a deep copy
complex_obj_copy = copy.copy(complex_obj)
complex_obj_deepcopy = copy.deepcopy(complex_obj)

# We change the value of the nested object nested_obj
nested_obj.greeting = "Hello"

# Let's see the changes in the objects
print(f"Copy object: {complex_obj_copy.nested_obj.greeting}")  # Copy object: Hello
print(
    f"Deepcopy object: {complex_obj_deepcopy.nested_obj.greeting}"
)  # Deepcopy object: Hello

print("~" * 30)

"""
The goal was to explain how Python can configure shallow and deep object copying processes 
by implementing the special __copy__ and __deepcopy__ methods. This allows you to control 
exactly how objects are cloned when using the copy() and deepcopy() functions from the copy module, 
and is important for classes that contain complex nested structures or dependencies.

For example, if our object contains large data and it should not be duplicated when copying, 
then setting __deepcopy__ allows us to control the cloning process. This helps to avoid 
unwanted duplication and ensures correct copying of complex structures.

Let's say we're working with a class that represents user settings, 
and these settings include a large data set (gigabytes of data) that doesn't need to be duplicated 
every time it's copied, but needs to be handled in an isolated environment.
"""


class UserSettings:
    def __init__(self, preferences, large_data_reference):
        self.preferences = preferences
        self.large_data_reference = large_data_reference

    def __deepcopy__(self, memo):
        print("Custom deep copy for UserSettings")
        # Assume that preferences is a small dictionary that can be safely copied,
        # and large_data_reference is a reference to a large data object that we don't want to duplicate.
        new_preferences = copy.deepcopy(self.preferences, memo)
        # Pass a reference to the same big data instead of copying it
        new_obj = UserSettings(new_preferences, self.large_data_reference)
        return new_obj


# Create an instance of UserSettings
original_settings = UserSettings({"language": "uk"}, large_data_reference="LargeDataID")

# Deep copying with customized logic
settings_copy = copy.deepcopy(original_settings)

print("~" * 30)

"""
We can configure the __deepcopy__ method in such a way that it allows for efficient 
copying of user settings without creating unnecessary copies of large data objects 
that should only be referenced. Because if we only read the data of the self.large_data_reference object, 
then there is no need to duplicate this data during deep copying. This approach allows you to optimize 
the use of memory and the execution time of the program, while maintaining 
the necessary flexibility in working with copies of objects.
"""
