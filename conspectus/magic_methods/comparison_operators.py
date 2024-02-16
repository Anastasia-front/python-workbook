"""
Overriding comparison operators in Python allows objects of your classes 
to interact with comparison operators (<, <=, >, >=, ==, !=) to specify exactly 
how objects should be compared to each other. 
This is achieved by implementing custom methods in your class.

Therefore, comparison operations, like other operators, have their own "magic" methods:


__eq__(self, other) — defines behavior when checking for equality (==).
__ne__(self, other) — defines behavior when checking for mismatch. !=.
__lt__(self, other) — defines the behavior when checking for less than <.
__gt__(self, other) - defines the behavior when checking for greater than >.
__le__(self, other) — defines the behavior when checking for less-than-equal to <=.
__ge__(self, other) — defines behavior when checking for greater-than-equals >=.


If we want the object to be comparable, we can implement
 these six methods and then any comparison check will work.



Consider the Rectangle class, which represents a rectangle with two properties: width and height. 
We want to compare rectangles based on the size of their area.
"""

print("~" * 30)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


if __name__ == "__main__":
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 20)
    rect3 = Rectangle(5, 10)
    print(
        f"Area of rectangles: {rect1.area()}, {rect2.area()}, {rect3.area()}"
    )  # Area of rectangles: 50, 60, 50
    print(rect1 == rect3)  # True: the areas are equal
    print(rect1 != rect2)  # True: the areas are not equal
    print(rect1 < rect2)  # True: the area of rect1 is smaller than that of rect2
    print(rect1 <= rect3)  # True: the areas are equal, so rect1 <= rect3
    print(rect1 > rect2)  # False: the area of rect1 is smaller than that of rect2
    print(rect1 >= rect3)  # True: the areas are equal, so rect1 >= rect3

print("~" * 30)

"""
Each of the comparison methods relies on the area of the rectangle as a comparison criterion. 
The __eq__ method checks for equality of areas, and the __lt__ and __gt__ methods compare 
whether the area of one rectangle is smaller or larger than the area of another. 
Other methods build on these basic comparisons, providing a complete set of comparison operations.

Using NotImplemented in comparison methods is an accepted and recommended practice 
when you encounter a situation where your method does not know how to compare an object 
to another type of object. When a comparison method returns NotImplemented, Python understands 
that the current method cannot perform the comparison and will try to find another way to compare, 
for example, by calling the corresponding method on a second object or resorting to other comparison mechanisms. 
If no method can compare the objects, then the interpreter will throw a TypeError exception. 
For example, the comparison operation rect1 > 10 will result in a TypeError: 
'>' not supported between instances of 'Rectangle' and 'int' .

We implement the Point class, which represents a point in two-dimensional space with x and y coordinates. 
The main purpose of the example is to show the possibility of comparing points by their coordinates 
using standard comparison operators (==, !=, <, >, <=, >=).
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x > other.x and self.y > other.y

    def __le__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x >= other.x and self.y >= other.y


if __name__ == "__main__":
    print(Point(0, 0) == Point(0, 0))  # True
    print(Point(0, 0) != Point(0, 0))  # False
    print(Point(0, 0) < Point(1, 0))  # False
    print(Point(0, 0) > Point(0, 1))  # False
    print(Point(0, 2) >= Point(0, 1))  # True
    print(Point(0, 0) <= Point(0, 0))  # True

print("~" * 30)

"""
Our example demonstrates how the class can intuitively integrate with Python's 
comparison operators, making code that uses these objects more readable and natural.
"""
