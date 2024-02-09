from dataclasses import dataclass

"""
The dataclasses module in Python provides a means to declaratively define classes 
that are primarily used to store data. This module was introduced in Python 3.7 
to simplify the creation of such classes without the need to manually write 
the boilerplate code that is often repeated in traditional classes.

The module provides a class decorator @dataclass that simplifies the creation of classes for data storage. 
Traditionally, when we create a class to store data, we need to manually define a method like __init__() 
to initialize attributes, magic methods to represent an object in an understandable format, or to compare objects. 
The @dataclass decorator automates this process by allowing us to declare class attributes and automatically 
generate those methods. This makes the code cleaner, less prone to errors, and easier to maintain. 

Using @dataclass allows to reduce the amount of code needed to create classes that primarily store data. 
This makes the code more readable and easier to understand, and it automatically creates a constructor for the __init__ class.
"""

# A basic example of @dataclass syntax is as follows:

# @dataclass
# class ExampleClass:
#      attribute1: type
#      attribute2: type = default_value


@dataclass
class Person:
    name: str
    age: int


"""
In this example, @dataclass automatically generates the __init__ method 
and other magic methods based on the declared attributes. 

The advantage of using @dataclass is that it automates many of the routine tasks 
involved in creating classes that store data.

In the following example, the Article class contains attributes with default values. 
This is useful when some fields have common values that do not require specifying each time the object is created:
"""


@dataclass
class Article:
    title: str
    author: str
    views: int = 0


"""
Consider the following problem to demonstrate the use of @dataclass 
in Python with a concrete example. We'll create a Rectangle class 
that will calculate and output the area of various user-specified rectangles.
"""


@dataclass
class Rectangle:
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height


rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
rect3 = Rectangle(8, 6)

print(f"Area of rectangle 1: {rect1.area()}")  # The area of the rectangle is 1:50
print(f"Area of rectangle 2: {rect2.area()}")  # Area of rectangle 2: 21
print(f"Area of rectangle 3: {rect3.area()}")  # The area of the rectangle is 3: 48

"""In conclusion, we can see that the @dataclass decorator is used 
when you create classes that serve to store data and do not require complex processing logic. 
For example, classes representing entities in the database, configuration objects, 
data transfer objects between system components, etc."""
