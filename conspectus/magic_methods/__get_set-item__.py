from collections import UserList

"""Square brackets allow us to access sequence elements by index 
or dictionary elements by key. The __getitem__ and __setitem__ methods in Python 
are used to configure access to the elements of an object using indexing or keys, 
similar to working with lists or dictionaries. 
These magic methods allow our classes to emulate container data types.

The __getitem__ method defines how an object of a class should behave 
when its elements are accessed by index or key. It takes a key or index 
as an argument and must return the value associated with that key or index.

The __setitem__ method defines how the object should behave when assigning 
a value to an element by a certain index or key. It takes two arguments: 
a key (or index) and a value to associate with that key.


Consider the SimpleDict class, which mimics the behavior of a dictionary:
"""
print("~" * 30)


class SimpleDict:
    def __init__(self):
        self.__data = {}

    def __getitem__(self, key):
        return self.__data.get(key, "Key not found")

    def __setitem__(self, key, value):
        self.__data[key] = value


# Using the class
simple_dict = SimpleDict()
simple_dict["name"] = "Boris"
print(simple_dict["name"])  # Boris
print(simple_dict["age"])  # Key not found
print("~" * 30)

"""In the example, SimpleDict uses an internal private dictionary __data 
to store its elements. The __getitem__ method allows you to get the value 
for a key, and the __setitem__ method allows you to set a new value for a key.

This approach makes the class more flexible and intuitive for users 
who are used to working with standard Python containers. 
Using __getitem__ and __setitem__ allows class objects to integrate 
with language functions and constructs designed to work with sequences or mappings, 
such as for loops, in statements, len() functions, and so on.

In addition, this approach increases the flexibility of the class by 
allowing additional validation or processing logic to be added when elements 
are accessed or modified. For example, you can now easily implement data type checking 
or logging without changing the class's external interface.



Let's imagine that we need to create a data structure that is similar to a list, 
but with a restriction: the elements of the list must always remain 
in a certain range of values. For example, we are working on an application 
to control the temperature in a room, where the temperature values 
must be limited by a minimum and a maximum threshold.
"""


class BoundedList:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value
        self.__data = []

    def __getitem__(self, index: int):
        return self.__data[index]

    def __setitem__(self, index: int, value: int):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(
                f"Value {value} must be between {self.min_value} and {self.max_value}"
            )
        if index >= len(self.__data):
            # Add a new element if the index is out of bounds
            self.__data.append(value)
        else:
            # Replace existing element
            self.__data[index] = value

    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"

    def __str__(self):
        return str(self.__data)


if __name__ == "__main__":
    temperatures = BoundedList(18, 26)

    for i, el in enumerate([20, 22, 25, 27]):
        try:
            temperatures[i] = el
        except ValueError as e:
            print(e)

    print(temperatures)
print("~" * 30)
# Output
# Value 27 must be between 18 and 26
# [20, 22, 25]


"""
As you can see, trying to set a value outside the allowed range results 
in the error "Value 27 must be between 18 and 26". We set temperature constraints 
on the values stored in the data structure and that they always meet certain criteria. 
We simply cannot add data to our list that does not pass the restriction.


We can combine our implementation with the capabilities of the UserList class. 
Inheriting from UserList, we get all the features of a regular list, 
but with the ability to modify the behavior by overriding methods or adding new ones.

The BoundedList class now behaves like a list, but with an additional restriction 
on the values of the elements stored in it. Using UserList as the base class simplifies 
the implementation because we don't need to redefine many of the list-specific methods; 
instead, we can focus on the data validation logic.

Note that we can or not implement the __getitem__ method. Because when we inherit from UserList, 
we get all the functionality of a standard Python list, but with the ability to override or add 
methods to customize the behavior. So __getitem__ and other item access methods are already part 
of UserList and will work as expected unless we choose to override them to change the behavior.

For example, it's possible to add logging:
"""


class BoundedList(UserList):
    def __init__(self, min_value: int, max_value: int, initial_list=None):
        super().__init__(initial_list if initial_list is not None else [])
        self.min_value = min_value
        self.max_value = max_value
        self.__validate_list()

    def __validate_list(self):
        for item in self.data:
            self.__validate_item(item)

    def __validate_item(self, item):
        if not (self.min_value <= item <= self.max_value):
            raise ValueError(
                f"Item {item} must be between {self.min_value} and {self.max_value}"
            )

    def append(self, item):
        self.__validate_item(item)
        super().append(item)

    def insert(self, i, item):
        self.__validate_item(item)
        super().insert(i, item)

    def __setitem__(self, i, item):
        self.__validate_item(item)
        super().__setitem__(i, item)

    def __getitem__(self, index):
        # Add custom logic here, such as logging or validation
        print(f"Accessing item at index {index}")
        # Call the original __getitem__ method
        return super().__getitem__(index)

    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"

    def __str__(self):
        return str(self.data)


if __name__ == "__main__":
    temperatures = BoundedList(18, 26, [19, 21, 22])
    print(temperatures)

    for el in [20, 22, 25, 27]:
        try:
            temperatures.append(el)
        except ValueError:
            print

    print(temperatures)
print("~" * 30)
# Output
# [19, 21, 22]
# Item 27 must be between 18 and 26
# [19, 21, 22, 20, 22, 25]
