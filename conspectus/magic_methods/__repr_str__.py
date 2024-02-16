"""
The magic methods __str__ and __repr__ in Python play a key role 
in representing objects as strings. Knowing and using these methods correctly 
allows you to control how the objects of your class are displayed and used,
which is an important part of developing Python programs.

When we want to see the contents of some object in the interactive mode 
of working with Python, we simply write its name in the console and the interpreter 
displays the representation of this object as a string.


The __repr__ method is designed to create a formal string representation of an object. 
Developers use it to uniquely identify an object, or even to reproduce the object 
elsewhere in the code. This view can be extremely useful during debugging because 
it allows developers to get an accurate view of the object's state.

Therefore, when we want to display some useful information in cases where the application 
must display the object, we must modify this method. For example, the class of a point 
on a plane in Cartesian coordinates:
"""

print("~" * 30)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


point = Point(2, 3)
print(repr(point))  # Outputs: Point(x=2, y=3)
print("~" * 30)

"""
But the main purpose of __repr__ is to create a formal string representation of the object 
that can be used to restore the object. The __repr__ method should return a string that, 
ideally, could be used in code to reproduce the object with the same data.

Using __repr__ allows developers to obtain a detailed representation of an object 
that can be used to accurately reproduce the object or to debug the application, 
helping to identify and fix errors.


This means that you can use the expression returned by the __repr__ method as a Python command 
to create a new object that will have the same characteristics as the original object. 
This feature is especially useful for debugging where you can easily reproduce objects 
based on their __repr__ representation.
"""


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


original_point = Point(5, 6)
print(repr(original_point))  # Point(x=2, y=3)

# Using the string returned by __repr__ to create a new object
new_point = eval(repr(original_point))
print(new_point)  # Point(x=2, y=3)
print("~" * 30)
"""
The eval() function is used to execute a string expression as code. 
It takes a string and executes it as a Python expression, returning the result 
of executing that expression. When the __repr__ method of a class returns a string, 
it can be passed to eval(). The idea is that calling eval() with the result __repr__ 
creates a new object identical to the original.

It is important to remember to use eval() carefully, as executing code 
obtained from untrusted sources can lead to serious security issues.



Very similar to the __repr__ method, which is responsible for how the object 
is converted to a string, is the __str__ method. When you call the str function 
and pass it some object, that object is actually called by the magic method __str__.

The __str__ method is designed to return a string representation of an object that should 
be human-readable and understandable. When you call the str() function on an object 
or print an object using print(), Python automatically uses the __str__ method of your class. 
This gives you, as a developer, the ability to define how the object should be presented in an understandable way.



That's why it's important to define a __str__ method in your classes: 
to provide an intuitive and readable representation of your objects.
"""


class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Human named {self.name} who is {self.age} years old"

    def __repr__(self):
        return f"Human({self.name}, {self.age})"


human = Human("Alice", 30)
print(human)  # Human named Alice who is 30 years old
print("~" * 30)
"""
Our __str__ method is designed to return a string that is understandable to the end user.
 If this method is not defined, Python will use the __repr__ method as a fallback to convert the object to a string.


In conclusion, the magic methods __str__ and __repr__ are important tools in a Python developer's arsenal. 
They allow not only better control over how objects of the class are presented, 
but also improve the user experience and simplify the debugging process. 
Learning and using these techniques will ensure that you take full advantage 
of the possibilities of object-oriented programming in Python.
"""
