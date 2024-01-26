from calculations import salary_calculations

"""For example, all functions that have a general purpose 
can be put into a separate file "entry point", which is 
a script called by the user to start work, and auxiliary 
functions and settings can be put into separate files and 
named accordingly. As a result, we will receive several 
relatively small files, the code in which will be intended 
for a single task (setting up the application, starting 
the application, basic logic). Such files with code in Python are called modules.

With the growth of the project, the number of modules, 
and we remind you that it is recommended not to let 
the modules "bloat" too much, grows, and the search 
for the right module begins to cause difficulties. 
In such a situation, Python packages come to the rescue."""

package = "is a directory containing Python modules"

"""By placing the modules in directories, you can 
structure the modules according to their purpose, 
and finding the right module will be much easier.

Working with packages is similar to working with modules, 
you can import the entity you need (for example a function) 
by importing the module from the package.

The import instruction is used when importing an entire package. 
This method is most often used by code developers because it saves 
time and requires only one line of code. On the other hand, this approach 
requires more memory than the approach involving selective import of attributes.


The from ... import instruction is used when you need 
to selectively import individual package attributes.
This makes it possible to save resources, but in itself 
this method is more difficult. Also, if you try to use 
an attribute that has not been imported, Python will 
throw an error. Yes, the package contains the attribute, 
but Python doesn't see it because it wasn't imported.



Suppose that you placed the salary_calculations.py module 
in the calculations directory next to main.py.
"""


def add_bonus(salary: int, bonus: int) -> int:
    return salary + bonus


# You needed the add_bonus function from salary_calculations.py
# in the middle of main.py. The directory structure should be as follows:

# from calculations import salary_calculations

salary = 1000
bonus = 15
salary_with_bonus = salary_calculations.add_bonus(salary, bonus)
print(salary_with_bonus)  # 1015


# Or we can import just the function:

"""
from calculations.salary_calculations import add_bonus

salary = 1000
bonus = 15
salary_with_bonus = add_bonus(salary, bonus)
print(salary_with_bonus) # 1015"""


"""The division into packages and modules can last as long as 
you consider necessary and convenient. Any package can contain 
packages within itself, and those packages can contain packages, 
and so on. The rule of thumb is to name packages and modules 
in the same way as Python variables (only letters, numbers and _, 
the name does not start with a number). It is also very important 
to think over the structure of the project so that it is convenient 
for you to search for the necessary modules in it later."""
