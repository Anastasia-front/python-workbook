"""One way to create a generator in Python is to create 
a custom function with multiple entry points. 
For this, the keyword yield is used.

The yield operator behaves in a similar way to return, 
it returns control of the flow of program execution 
from the body of the function. But, unlike return, 
yield does not start the execution of the function 
from the beginning at the next call, but continues 
from the point where the function stopped.

Of course, this behavior assumes that somewhere in 
the memory of the program should be stored information 
about what the execution of the function stopped at 
and about the state of the local namespace of the function. """

# Consider the following example:


def generator():
    yield 1
    yield 2
    yield 3


gen = generator()

print("~" * 30)
# Using next()
print(next(gen))  # Print 1
print(next(gen))  # Print 2
print(next(gen))  # Print 3
print("~" * 30)

"""
This code demonstrates the basic principles of how a generator works in Python. 
The function generator is defined as a generator. It uses the yield keyword, 
which indicates that this function will return a generator. When a function calls yield, 
it "returns" the value that follows yield and "freezes" its current state. 
The execution of the function will continue from this point on the next call. 
When we assign gen = generator(), the variable gen is now the generator 
returned by the generator function.

Next comes the use of next(). Each time next(gen) is called, the generator 
continues execution from where it last stopped (after yield). On the first call to next(gen), 
the generator is executed from the beginning to the first yield, i.e. returns 1. 
On the second call to next(gen), it continues from the second yield and returns 2. 
On the third call to next(gen), it continues to the third yield and returns 3. 
The code print(next(gen)) prints the value returned by the generator at each step.

After the generator has returned all its values, if we call next(gen),
we will throw a StopIteration exception because there are no more values to return. 
This exception signals that the iteration has finished.

In order not to use try except every time to control the StopIteration exception, 
generators are often used directly in for ... loops, which will do it for us:
"""


def count_down(start):
    while start > 0:
        yield start
        start -= 1


for number in count_down(5):
    print(number)
print("~" * 30)
# The result of executing this code will be
# 5
# 4
# 3
# 2
# 1

"""
One of the useful cases of using a generator is iterating over a file. 
The generator allows us to process very large files and at the same time save memory.
"""

folder_path = "example"
file_path = f"{folder_path}/example.txt"


def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()


# Using a generator to read lines from a file
for line in read_lines(file_path):
    print(line)
print("~" * 30)

"""
In the middle of the read_lines function, the for loop iterates over each line in the file. 
The yield keyword is used to return each line of the file. Each line is pre-processed 
with the strip() method to remove spaces and newline characters from the edges. 
This is a common data cleansing practice.

Next, we simply use the generator to work directly with the strings of the file.

The advantage of this approach is that thanks to lazy processing, 
the generator reads lines one by one without loading the entire file into memory. 
This is especially useful when working with large files.


So let's make a summary:

A generator in Python is an object that is used for lazy (on-demand) 
data generation and allows us to declare a function that can be used in a loop.

A generator is created using a function that returns a sequence 
of elements one by one using yield instead of return.

The generator produces elements "on the fly" and processes one element at a time. 
This is very efficient in terms of memory usage, especially for large data. 
When a generator produces a value, its state is "frozen" 
and execution can continue from that point on the next call.

Generators can be iterated in a for loop or manually using the next() function."""
