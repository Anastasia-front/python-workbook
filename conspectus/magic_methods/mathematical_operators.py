from collections import UserDict, UserList

"""Overriding mathematical operators in Python allows classes to change 
the default behavior of arithmetic operations. This is known as operator overloading. 
Using special methods, you can define or override the behavior of operators 
such as +, -, *, /, and many others for objects of your classes.

Here are some of the more common special methods for overriding mathematical operators:

__add__(self, other) for the + operator
__sub__(self, other) for operator -
__mul__(self, other) for operator *
__truediv__(self, other) for operator /
__floordiv__(self, other) for the integer division operator //
__mod__(self, other) for the remainder operator from division %
__pow__(self, other) for the * exponentiation operator


Overriding mathematical operators can be a handy tool. For example, 
let's create a class of dictionaries that support addition and subtraction operations:
"""
print("~" * 30)


class MyDict(UserDict):
    def __add__(self, other):
        temp_dict = self.data.copy()
        temp_dict.update(other)
        return MyDict(temp_dict)

    def __sub__(self, other):
        temp_dict = self.data.copy()
        for key in other:
            if key in temp_dict:
                temp_dict.pop(key)
        return MyDict(temp_dict)


if __name__ == "__main__":
    d1 = MyDict({1: "a", 2: "b"})
    d2 = MyDict({3: "c", 4: "d"})

    d3 = d1 + d2
    print(d3)  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

    d4 = d3 - d2
    print(d4)  # {1: 'a', 2: 'b'}

print("~" * 30)

"""
The syntax is simple and the code is quite expressive.

The __add__ method defines the behavior for the + operator. 
It allows you to combine two objects of the MyDict class by adding all elements 
from the second dictionary other to the first (self). First, a copy of the self.data
internal dictionary is created to avoid changing the original dictionary. 
All elements from the second dictionary are added to the temporary dictionary. 
If the keys already exist, their values will be updated to the values from other. 
The magic method returns a new MyDict instance initialized from the merged dictionary.

The __sub__ method defines the behavior for the - operator. It allows you to delete keys 
from the first dictionary self that are present in the second other. Similar to the __add__ method, 
a copy of the internal temp_dict dictionary is first created. Next, the for loop iterates 
over all the keys in the second dictionary other. The if key in temp_dict condition checks 
whether the key is present in the temp_dict dictionary. If so, we delete the key and its value 
from the temporary dictionary, if such a key exists. 
We return a new instance of MyDict initialized after removing the keys.

Let's consider another example and create a ComplexNumber class 
to represent complex numbers, overriding some arithmetic operators:
"""


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


if __name__ == "__main__":
    num1 = ComplexNumber(1, 2)
    num2 = ComplexNumber(3, 4)
    print(f"Sum: {num1 + num2}")  # Sum: 4 + 6i
    print(f"Difference: {num1 - num2}")  # The difference is -2 + -2i
    print(f"Product: {num1 * num2}")  # Product: -5 + 10i

print("~" * 30)

"""
Our example shows how you can redefine arithmetic operators to implement 
addition, subtraction, and multiplication of complex numbers. 
The use of special methods makes it possible to use common mathematical operators 
with objects, creating a readable and intuitive interface.

Overriding mathematical operators provides significant opportunities to create 
expressive and powerful abstractions that can mimic the behavior of Python's built-in types 
or create new ways to interact with objects in your classes. For example, we implement 
vector multiplication, where the result is a scalar product of vectors.
"""


class MulArray(UserList):
    def __init__(self, *args):
        self.data = list(args)

    def __mul__(self, other):
        return self.__scalar_mul(other)

    def __rmul__(self, other):
        return self.__scalar_mul(other)

    def __scalar_mul(self, other):
        result = 0
        for i in range(min(len(self.data), len(other))):
            result += self.data[i] * other[i]
        return result


if __name__ == "__main__":
    vec1 = MulArray(1, 2, 3)
    vec2 = MulArray(3, 4, 5)

    print(vec1 * vec2)  # 26
    print(vec1 * [1, 2, 3])  # 14
    print([1, 1, 1] * vec2)  # 12

print("~" * 30)

"""
The __mul__ magic method defines the behavior of a multiplication operation * 
between a MulArray instance and another object. It performs a dot product 
between self.data and the second list, limiting the multiplication to the minimum length 
of both lists. The result is the sum of the products of the corresponding elements of the lists. 
Here we have a new magic method __rmul__ that defines the behavior of the multiplication operation 
when the MulArray instance is located to the right of the multiplication operator. 
This provides commutativity of the multiplication operation, allowing multiplication to be performed on both sides. 
It is required so that we can perform the [1, 1, 1] * vec2 operation when 
the MulArray instance is to the right of the multiplication operator. 
The implementation is identical to __mul__, so the result will be the same.
"""
