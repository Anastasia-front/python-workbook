"""In the Python programming language, fields are variables that store information 
about the state of an object. These fields are usually accessed and modified directly, 
but sometimes it is necessary to control this process, for example for data validation 
or encapsulation. For this, there are special methods called getters and setters. 
In Python, the @property decorator is used, which allows you to conveniently create and use them.

Getters (from the English get - to receive) are methods that allow you to get the value of a field. 
They are used when accessing a field requires some additional processing or when direct access to a field 
is not desirable for encapsulation reasons. For example, if you want to always return the value of a field 
as a string, even if it is stored as a number.

Setters (from the English set - set) are methods that allow you to set the value of a field. 
They are most often used to validate data that is trying to be assigned to a field. 
For example, if we have a field that should accept only positive numbers, you can add a check 
in the setter that will throw an exception or return an error if you try to assign a negative number to it.


Python's built-in @property decorator makes it easy to create getters. Using this decorator 
makes the class method available as a field, meaning it can be called without parentheses. 
This makes the class interface cleaner and more intuitive. To create a setter for the same field 
as the getter, the @property.setter decorator is used, which is applied to a method with the same name as the property.


Consider an example class that uses @property to create a getter and setter for the age field. 
We want age to always be a positive number. First, we'll create an age method with a @property decorator 
that will act as a getter and return the value of the __age attribute (a private version of age used internally 
by the class to store the actual value). We will then create an age method with a @property.setter decorator 
that will act as a setter and validate the input value before assigning it to __age. If the value doesn't meet 
our criteria (for example, if it's negative), we can throw an exception or take other actions to handle the error.

Let's start by declaring the Person class, which has a private attribute __age. 
Recall that we use an underscore at the beginning of an attribute name to indicate that the attribute 
is internal and should not be directly accessible from outside the class. This is standard practice 
for encapsulation to help keep the internal implementation of a class hidden from the user.
"""
print("~" * 30)

class Person:
    def __init__(self, age):
        self.__age = age  # Direct assignment of the attribute value in the constructor

    @property
    def age(self):
        return self.__age  # The getter returns the value of a private field

    @age.setter
    def age(self, value):
        if value < 0:
            # Validate the input value
            raise ValueError("Age cannot be negative")
        # Assigning a valid value to a private field
        self.__age = value


if __name__ == "__main__":
    person = Person(10)
    print(person.age)
    # person.age = -5 - it will cause an error

print("~" * 30)

"""
If we want to assign a negative value to the age field, we will receive a corresponding error. 

Traceback (most recent call last):
   File "E:\\WebDir\\Works\\Python\\python-help-solution\\core_course\\topic7\\ex25.py", line 19, in <module>
     person.age = -5
   File "E:\\WebDir\\Works\\Python\\python-help-solution\\core_course\\topic7\\ex25.py", line 12, in age
     raise ValueError("Age cannot be negative") # Validate the input value
ValueError: Age cannot be negative



In this example, when we create a new instance of the Person class, the __init__ constructor takes an age 
as an argument and assigns it to the __age private attribute. The getter for age simply returns the value 
of this private attribute, allowing external code to retrieve a person's age 
without directly accessing the internal implementation.



@property
def age(self):
     return self.__age # The getter returns the value of a private field



The age setter validates the input value before assigning it to the __age private field. 
If the specified value is negative, the setter throws a ValueError exception, thus preventing 
an incorrect age assignment. This ensures that the Person object always has a valid age.



@age.setter
def age(self, value):
     if value < 0:
         # Validate the input value
         raise ValueError("Age cannot be negative")
     # Assigning a valid value to a private field
     self.__age = value



Using getters and setters with the @property decorator allows us to provide controlled access 
to a class's fields by performing necessary checks or processing when attempting to read 
or modify their values. This improves code security and reliability by allowing developers 
to define how attributes should be used and what actions should be performed when they are changed.



Everything looks quite simple, but there is one problem. If we execute the following code

person = Person(-10)
print(person.age)

Then we will not receive any error notification, but the output will be:

-10



Let's fix this shortcoming. It is necessary to first set the __age value to None in the class constructor, 
and then set it to the passed age value through the setter. This will allow us to immediately apply 
the validation logic defined in the setter when initializing the object.
"""


class Person:
    def __init__(self, age):
        # First, set __age to None
        self.__age = None
        # We use a setter to set the age, which allows validation of the input value
        self.age = age

    @property
    def age(self):
        # The getter returns the value of the private field
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            # Validate the input value
            raise ValueError("Age cannot be negative")
        # Assigning a valid value to a private field
        self.__age = value


if __name__ == "__main__":
    # person = Person(-10) - it will cause an error
    person = Person(20)
    print(person.age)

print("~" * 30)

"""
Now the execution throws an error as it should.

Traceback (most recent call last):
   File "E:\\WebDir\\Works\\Python\\python-help-solution\\core_course\\topic7\\ex26.py", line 23, in <module>
     person = Person(-10)
   File "E:\\WebDir\\Works\\Python\\python-help-solution\\core_course\\topic7\\ex26.py", line 6, in __init__
     self.age = age
   File "E:\\WebDir\\Works\\Python\\python-help-solution\\core_course\\topic7\\ex26.py", line 17, in age
     raise ValueError("Age cannot be negative")
ValueError: Age cannot be negative


In this case, when we instantiate the Person class, the private field __age is initially set to None. 
The age setter is then called, passing it the value passed in the constructor. This allows us to use 
the validation logic defined in the setter already at the initialization stage of the object, 
ensuring that incorrect data will not be assigned to the __age attribute.

This approach improves code reliability and security because it ensures that all values assigned 
to the important age attribute of an object go through the same validation process, regardless 
of whether they are set when the object is created or are changed later.
"""


class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = None
        self.__is_admin = None
        self._is_active = is_active
        self.__is_admin = is_admin

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool):
        # Any validation or processing logic can be added here
        self._is_active = value

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value: bool):
        # Any validation or processing logic can be added here
        self.__is_admin = value

    def greeting(self):
        return f"Hi {self.name}"


if __name__ == "__main__":
    p = Person("Boris", 34, True, False)
    print(p.is_admin)  # We use the getter - False
    p.is_admin = True  # We use the setter
    print(p.is_admin)  # True

print("~" * 30)

"""
Using the @property decorator, we create getters and setters for a protected and private field. 
This allows us to control access to these attributes, providing the ability 
to validate data and encapsulate the internal implementation.
"""
