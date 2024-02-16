"""
Functors in Python are objects of classes that can be called as functions. 
This is achieved by implementing a special magic method __call__ for the class. 
When you add a __call__ method to a class, instances of that class can be called by regular functions.

Functors are objects that behave like functions in the sense that they can be called and passed arguments.

Functors can be useful for several reasons:

- Allow objects to have state. This means that the functor can save state between calls.
- Functors allow an object to have complex calling logic that may depend on the functor's internal state or other factors.
- They can be used to create parameterized, configurable, or closed functions.


For example, below implement the __call__ class method, making it a functor:
"""
print("~" * 30)

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, other):
        return self.factor * other


# Create an instance of the functor
double = Multiplier(2)
triple = Multiplier(3)

# Call the functor
print(double(5))  # Output: 10
print(triple(3))  # Output: 9
print("~" * 30)

"""
The Multiplier class takes one factor argument when initialized. 
The __call__ method allows instances of Multiplier to be called as functions 
that multiply the value passed to them by the factor specified when the instance was created. 
This is something similar to the locking mechanism that we considered earlier.

Consider a functor with a state. It will use its internal state to count the number of times it has been called.
"""


class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1


counter = Counter()
counter()
counter()
print(f"Called {counter.count} times")  # Called 2 times
print("~" * 30)
"""
A functor can contain rather complex logic. Consider a functor that uses internal state 
and additional parameters to decide what action to perform when called. This functor 
takes parameters on initialization, which are then used to configure its behavior.
"""


class SmartCalculator:
    def __init__(self, operation="add"):
        self.operation = operation

    def __call__(self, a, b):
        if self.operation == "add":
            return a + b
        elif self.operation == "subtract":
            return a - b
        else:
            raise ValueError("Unknown operation")


add = SmartCalculator("add")
print(add(5, 3))  # 8

subtract = SmartCalculator("subtract")
print(subtract(10, 7))  # 3

print("~" * 30)
"""
Our SmartCalculator class creates closed functions with given parameters. 
The object add is a functor for adding numbers, and subtract is a subtraction.

Functors in Python are a powerful tool that allow classes to mimic the behavior 
of functions while still having their own internal state and logic. They can make code 
more flexible by adding object-oriented capabilities to a functional programming style.
"""
