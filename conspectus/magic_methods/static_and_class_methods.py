"""
Static and class methods are special types of methods that can be used in classes 
for a variety of purposes. They are similar in that both are called without instantiating the class, 
but have different purposes and are used in different scenarios.

Static methods use the @staticmethod decorator and are methods that do not have access 
to the instance of the class, i.e. the self variable, from which they were called. 
This means that static methods cannot change the state of an object or class,
but they can be useful for performing some operations that do not depend on the state of the object. 
Static methods can be thought of as "helper" functions that have a logical connection to the class, 
but do not need access to its attributes or methods.

For example, if we have a class that represents geometric shapes, 
we can include a static method to calculate the area of a circle using the radius passed as an argument. 
This method does not depend on a specific instance of the class and can be called without creating an object.
"""

print("~" * 30)


class Geometry:
    PI = 3.14159

    @staticmethod
    def area_of_circle(radius):
        return Geometry.PI * radius**2


"""
In this example, area_of_circle is a static method that calculates the area of a circle 
using the passed radius. This method can be called directly from the class without having to instantiate the class.

To use this method, we call area_of_circle directly through the Geometry class, passing the radius as an argument. 
The method uses this radius to calculate and returns the area of the circle.
"""


print(Geometry.area_of_circle(5))  # 78.53975

print("~" * 30)


"""
A static method does not depend on any specific instance of Geometry and can be called without creating such an instance.

Class methods use the @classmethod decorator and, unlike static methods, access the class itself via the cls parameter, 
which is automatically passed to Python. This means that class methods can change the state of the class 
or call other class methods. Class methods are often used for factory methods that create instances of 
a class using different initialization methods than a standard constructor.

For example, if we have an Employee class, we can use a class method to create instances of the class 
based on information retrieved from a string or file.
"""


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @classmethod
    def from_string(cls, employee_info):
        name, position = employee_info.split(",")
        return cls(name, position)


"""
In our code, from_string is a class method that allows you to create instances of Employee 
by splitting a string into fields. The method uses the cls parameter to create a new instance, 
ensuring that it can be used successfully even in descendant classes. 
In our example, cls will be the Employee class itself.
"""


employee_info = "John Doe,Manager"
john_doe = Employee.from_string(employee_info)

print(john_doe.name)  # Prints: John Doe
print(john_doe.position)  # Output: Manager

print("~" * 30)

"""
We call from_string, passing in a string with employee information. 
The method parses the string using a comma as the delimiter and creates 
a new instance of the Employee class using the resulting data.
We can then use this instance as normal by referring to its name and position attributes.



The difference between static and class methods is that static methods are used for functions 
that do not require access to the attributes or methods of the class, while class methods 
have access to the class and its attributes, allowing you to change the state of the class 
or create instances of the class using alternative designers."""
