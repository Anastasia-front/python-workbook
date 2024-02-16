from random import randint

"""
An iterator in Python is an object that allows us to sequentially iterate 
through the elements of any iteration object (for example, list, tuple, dictionary) 
without the need to use indexes. It implements the __iter__() and __next__() methods 
and allows iterating over the elements of a sequence without loading the entire sequence into memory.

The __iter__() method returns the iterator itself, and the __next__() method 
returns the next element of the iteration object. When the iterator's elements run out, 
a StopIteration exception should be thrown, signaling the end of the iteration.

Since an iterator allows us to iterate through the elements of a container using a for-in loop, 
the basic idea is that the iterator stores the current state of the iterator, 
allowing you to retrieve the next element using the __next__() method.

When you use a for-in loop to iterate over the elements of a container, 
Python automatically calls the container's __iter__() method to get the iterator. 
Then, on each iteration of the loop, the iterator's __next__() method is called 
to retrieve the next element, until a StopIteration exception is raised, indicating the end of the iteration.

Let's create a simple iterator for demonstration.
"""
print("~" * 30)


class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 0:
            raise StopIteration
        self.current -= 1
        return self.current


if __name__ == "__main__":
    counter = CountDown(5)
    for count in counter:
        print(count)

# Output
# 4
# 3
# 2
# 1
# 0
print("~" * 30)

"""
This example creates a CountDown iterator that starts counting down from a given number 
and decrements it to 0. The __iter__() method returns an iterator object and it is self 
because our class has a __next__() method. The __next__() method returns the next container element.

self.current -= 1
return self.current

Note that the __next__ method must throw a StopIteration 
exception to indicate that the iteration is complete, 
otherwise the for loop on such an object will be infinite.

if self.current == 0:
     raise StopIteration


You can only iterate through the iterator once. 
In this sense, an iterator is a "disposable" object. 
If we need to iterate again, we have to create a new iterator.


But this can be implemented through the generator with which we have already dealt. 
A generator is a simplified way to create iterators. A function becomes a generator 
when it contains a yield expression. The generator automatically 
implements the __iter__() and __next__() methods.
"""


def count_down(start):
    current = start
    current -= 1
    while current >= 0:
        yield current
        current -= 1


# Using the generator
for count in count_down(3):
    print(count)

# Output
# 2
# 1
# 0
print("~" * 30)

"""
This generator performs the same function as the CountDown iterator, 
but with less code and more readability.

Consider the following example. Let's create the RandIterator class,
which is used to generate a limited number of random numbers in a given range. 
When we create an instance of this class, we specify the start and end values 
of the range start and end and the number of quantity numbers we want to generate.
"""

# Realization


class RandIterator:
    def __init__(self, start, end, quantity):
        self.start = start
        self.end = end
        self.quantity = quantity
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.quantity:
            raise StopIteration
        else:
            return randint(self.start, self.end)


if __name__ == "__main__":
    my_random_list = RandIterator(1, 20, 5)

    for rn in my_random_list:
        print(rn, end=" ")

print("\n")
# The output is a set of random numbers from the range [1, 20]
print("~" * 30)

"""
Our class implements two main methods that make it an iterator: __iter__() and __next__(). 
The __iter__() method simply returns the self of the class as an iterator. 
The __next__() method is used to generate the next random number each time it is called. 
It increments self.count by one on each call and generates a new random number 
using randint(self.start, self.end). As soon as the number of generated numbers 
reaches the quantity specified when creating the instance, the __next__() method 
throws a StopIteration exception, which signals the end of the iteration.

As a result, when we use our iterator in a for loop, it allows us to sequentially 
receive random numbers in the given range [start, end], 
but not more than the specified amount quantity.

To turn an iterator into a generator, we can use a function with the yield keyword 
instead of a class with __iter__() and __next__() methods. The generator automatically 
keeps track of its state at the location of each yield call 
and resumes execution from that location at the next call.
"""


def rand_generator(start, end, quantity):
    count = 0
    while count < quantity:
        yield randint(start, end)
        count += 1


if __name__ == "__main__":
    for rn in rand_generator(1, 20, 5):
        print(rn, end=" ")

print("\n")
# The output is again a set of random numbers from the range [1, 20]
print("~" * 30)
"""
In this version, the rand_generator function is a generator that takes the same arguments: 
start, end, and quantity. The generator initializes the count counter from zero and uses 
a while loop to generate random numbers in a given range. Each time the generator reaches 
the yield statement, it returns a random number and "freezes" its state until the next call.

As we can see, this approach greatly simplifies the code, while maintaining the same functionality: 
generating a limited number of random numbers in a given range. Generators are a powerful tool in Python 
for creating iterators with less effort and more readable code.



So in conclusion.



An iterator is an object that allows the user to iterate through all the elements of a container 
without needing to know the internal structure of the container. Implemented using 
the __iter__() and __next__() methods. The __iter__() method returns an iterator object, 
and the __next__() method is automatically called by the for loop or the next() function 
to retrieve the next element of the container. 
To create an iterator, you need to define a class with these two methods.

A generator is a function that allows you to declaratively create an iterator using the yield keyword. 
It automatically implements the __iter__() and __next__() methods, so you no longer need to explicitly define them. 
Creating a generator is simply writing a function that uses yield to return the next value.


Generators can be more efficient than iterators when dealing with large amounts of data 
or complex calculations because they generate values on the fly and do not store all values in memory. 
They are especially effective when you need to process large amounts of data o
r perform complex calculations with minimal memory load.
"""
