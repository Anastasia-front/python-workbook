# By default, Python instructions are executed one after the other from top to bottom.
flow_of_execution = "the sequence of execution of expressions in the program"


# In Python, there are three ways to control the flow of execution:

conditional_execution = (
    "execution of a block of instructions only under certain conditions"
)
loops = "repeating the execution of a block of instructions until some condition is met"
exceptions = "an error handling mechanism that allows you to control the flow of the program \
when exceptional situations (for example, errors or other unforeseen circumstances) occur."

"""In Python, conditional execution, loops, and exceptions form the basis of controlling
the flow of program execution, allowing the development of complex and flexible data
processing and user interaction algorithms.

A conditional statement in Python is a language construct that allows you to perform
certain actions depending on whether a certain condition is met."""

# 0,False,None and empty value casts to False
print("~" * 30)
user_name = input("Enter your name: ")

if user_name:
    print(f"Hello {user_name}")
else:
    print("Hi Anonym!")
print("~" * 30)

# identity operator
"""The is operator in Python is used to test whether
two objects point to the same area of memory,
that is, whether they are the same object.

This operator differs from the == operator,
which tests the equality of object values.

The is operator in Python is used to test the identity of objects,
that is, to determine whether two variables point to the same object in memory.
This operator, often called the identity operator, is especially important
when working with immutable data types such as numbers and strings.
In the case of immutable data types, Python can cache objects,
which sometimes causes the is operator to return True for objects
with the same values, as in the case of very small integers or short strings.
It is useful to have this information in case you 
encounter such an exception in your code."""

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False
print("~" * 30)

# In this example, b is the same object as a because they point to the same list.
# Instead, c creates a new list that contains the same values but is physically a separate object.

# However, its main use is to check if a variable is None.

my_var = None

if my_var is None:
    print("There is no value")
print("~" * 30)

# This use of is is optimal because there is only one None object in Python.

"""
Therefore, the is operator should be used to check the identity of objects
when it is important that two variables point to the same object.
And the == operator should be used to check the equality of the values of two objects.


Outputs "Fizz" if the number is a multiple of some specific number (for example, 3);
Outputs "Buzz" if the number is a multiple of some other specific number (for example, 5);
Prints "FizzBuzz" if the number is a multiple of both of these numbers;
Otherwise, it outputs the number itself."""

num = int(input("Enter number : "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
print("~" * 30)

# blocks of instructions

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))

if x >= 0:
    if y >= 0:  # x > 0, y > 0
        print("First quarter")
    else:  # x > 0, y < 0
        print("Fourth Quarter")
else:
    if y >= 0:  # x < 0, y > 0
        print("Second quarter")
    else:  # x < 0, y < 0
        print("Third quarter")
print("~" * 30)

# ternary operators
is_nice = True
state = "nice" if is_nice else "not nice"

some_data = None
msg = some_data or "Did not return of data"

# MATCH

"""match variable:
     case template1:
         # execute the code for template 1
     case template2:
         # execute the code for pattern 2
     case _:
         # execute code if no matches found"""

point = (1, 0)

match point:
    case (0, 0):
        print("Point in the center of coordinates")
    case (0, y):
        print(f"The point lies on the Y axis: y={y}")
    case (x, 0):
        print(f"The point lies on the X-axis: x={x}")
    case (x, y):
        print(f"The point has coordinates: x={x}, y={y}")
    case _:
        print("This is not a point")
print("~" * 30)

# it is possible to use the match operator with collections

plants = ["rose", "tulip", "sunflower"]

match plants:
    case ["rose", "sunflower", _]:
        # Case when there's both a rose and a sunflower
        print("There's a rose and a sunflower.")
    case ["rose", _, _]:
        # Case when there's only a rose
        print("There's a rose.")
    case _:
        # Case for other combinations
        print("No flowers.")
print("~" * 30)
