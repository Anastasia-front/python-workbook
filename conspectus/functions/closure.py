from typing import Callable

"""Key aspects of circuits are:

- An inner function has access to variables defined in the scope of the outer function.
- The outer function returns the inner function as the result of its work.
- After the outer function completes, the inner function retains access to these variables, 
which plays an important role in certain programming patterns and algorithms.
"""
# The easiest way to explain it is with an example:

print("~" * 30)
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function


# Create a closure
my_func = outer_function("Beautiful nature")
my_func()
print("~" * 30)

"""
In this example, the outer_function function is defined 
to take an msg argument and create an internal message 
variable whose value is initialized with the passed argument. 
Inside outer_function is another function, inner_function, 
which is designed to display the value of the message variable on the screen. 
An important aspect is that inner_function uses the message 
variable that was defined in the outer lexical environment of outer_function.

After outer_function executes, instead of calling inner_function directly, 
outer_function returns it as an object. This allows the inner_function to maintain 
its connection to its lexical environment, even after the outer_function has finished executing.

When the action my_func = outer_function("Beautiful nature") is executed, 
the function my_func becomes a reference to the function inner_function. 
Why? Because when outer_function is called, it returns a reference to inner_function. 
Next, when we call my_func(), the function inner_function is actually executed, 
it successfully outputs "Beautiful nature". This is due to inner_function saving access 
to the message variable that was defined in outer_function. This behavior is a classic example 
of a closure, where an inner function stores the state of variables from its lexical context.

How can it be used practically? In fact, there are quite a few places 
where closure is used, but let's consider an example that is more understandable. 
We will create a closure that will store information 
about the number of times the function has been called.
"""


def counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        # use nonlocal to change the variable in the closure
        nonlocal count
        count += 1
        return count

    return increment


# Creating a counter
count_calls = counter()

# Counter calls
print(count_calls())  # Outputs 1
print(count_calls())  # Output 2
print(count_calls())  # Output 3
print("~" * 30)

"""This is an example of a closure where increment has locked the count variable 
within itself and has access to it even after the outer counter function completes its execution. 
Because of this, count_calls preserves state between calls. 
Every time we call count_calls, it calls increment , which wraps count in itself.

So you can create a function that can change behavior depending on how many calls have already occurred."""
