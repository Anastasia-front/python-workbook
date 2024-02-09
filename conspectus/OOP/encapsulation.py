"""
Encapsulation in programming, in particular in object-oriented programming (OOP), 
is one of the key principles, which consists in hiding the internal structure 
of a class and protecting its data from direct access from the outside. 
This principle allows you to restrict access to certain components of a class 
(fields and methods), providing control over how this data is used and changed.

With the help of class attributes and methods, we perform encapsulation — 
we hide the implementation details under the class interface."""

# In general, encapsulation in OOP is implemented through the use of
# public, protected, and private attributes and methods.

public = "the element is available from anywhere in the program."
protected = "an element is available from the class in which it is declared, \
as well as from derived classes."
private = "an element is available only from the class in which it is declared."

# Protected attributes and methods

"""
They are indicated by a single underscore _ at the beginning of the name. 
This is just a convention, and protected attributes may still be accessible 
from the outside, but it is considered bad practice to change them from the outside.

The correct approach is to provide access to protected attributes through public methods, 
which may include additional processing or validation logic, 
thereby maintaining security and data integrity within the class.

If we want to interact with the object's protected fields from the outside, 
we need to implement a proper encapsulation approach in the Person class 
and use methods to interact with such object attributes
"""

print("~" * 30)


class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active


p = Person("Boris", 34, True)
print(p.name, p.age, p.is_active())
print(p.greeting())
print("~" * 30)

# Private attributes and methods


"""In Python, there is no true privacy for class attributes as implemented in, 
for example, Java. Python uses so-called "name mapping" to provide this level of encapsulation. 
Attributes that are considered private are denoted by two underscores __ 
and cannot be accessed directly from outside the class.
"""


class PersonTwo:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active


p = PersonTwo("Boris", 34, True, False)
# print(p.__is_admin)
print(
    """Execution of print(p.__is_admin) will be the error -
      ------------------------------------------------------
      AttributeError Traceback (most recent call last)
      Cell In[6], line 13
       9 return f"Hi {self.name}"
      12 p = Person("Boris", 34, True, False)
---> 13 print(p.__is_admin)

      AttributeError: 'Person' object has no attribute '__is_admin"""
)
print("~" * 30)
# Output
# ------------------------------------------------------
# AttributeError Traceback (most recent call last)
# Cell In[6], line 13
#        9 return f"Hi {self.name}"
#       12 p = Person("Boris", 34, True, False)
# ---> 13 print(p.__is_admin)

# AttributeError: 'Person' object has no attribute '__is_admin'


"""
There is no access using p.__is_admin.

In fact, only the name of the field was changed to prevent accidental access to it, 
but it is still accessible from outside the class. 
The modified name is formed as an underscore, a class name, and a variable name.
"""


class PersonThree:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active


p = PersonThree("Boris", 34, True, False)
print(p._PersonThree__is_admin)  # False
print("~" * 30)

"""
It's possible to get optionally access the __is_admin field 
via the p._Person__is_admin expression, which generally doesn't protect anything.

To implement access methods for the private field __is_admin in the Person class, 
we can use the same approach as for the protected field _is_active
"""


class PersonFour:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

    def get_is_admin(self):
        return self.__is_admin

    def set_is_admin(self, is_admin: bool):
        # Any validation or processing logic can be added here
        self.__is_admin = is_admin


p = PersonFour("Boris", 34, True, False)
print(p.get_is_admin())  # False
p.set_is_admin(True)
print(p.get_is_admin())  # True
print("~" * 30)

"""
In this example, the get_is_admin method allows to get the value 
of the __is_admin field, and the set_is_admin method allows to change it. 
This provides controlled access to the private field, allowing to introduce 
the necessary validation or processing logic when the value changes.
"""
