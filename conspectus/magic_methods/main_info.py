# https://minhhh.github.io/posts/a-guide-to-pythons-magic-methods

"""
Magic methods are simply the means that the Python programming language 
provides developers to implement operator overloading and other powerful mechanisms.

That's why the expression a + b is transformed at a low level into a call to a.__add__(b), 
turning the standard addition operation into a method call that can be overridden 
at the developer's discretion. This possibility gives great freedom in customizing 
the behavior of objects, allowing, for example, to create complex numeric types 
or implement operators to work with your own data classes.


It is important to remember that the names of all magic methods in Python 
follow a strict nomenclature: they consist of lowercase letters and underscores, 
beginning and ending with a double underscore (__). This convention not only promotes 
unity of coding style, but also makes magic methods easily recognizable among other code.

The magic method which is used most often is the __init__ method. 
This method is responsible for initializing the object. When you create an object of a class, 
you first create an empty object that contains only the required service attributes. 
After the object is created, the __init__ method is automatically called, 
which we can modify according to our needs.
"""
print("~" * 30)


class Human:
    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age

    def say_hello(self) -> str:
        return f"Hello! I am {self.name}"


bill = Human("Bill")
print(bill.say_hello())  # Hello! I am Bill
print(bill.age)  # 0

jill = Human("Jill", 20)
print(jill.say_hello())  # Hello! I am Jill
print(jill.age)  # 20
print("~" * 30)

"""
The __init__ magic method does not necessarily need to take 
arguments and only contains the creation of fields. 
This method can be used to implement any actions you need 
at the stage when the object has already been created and needs to be initialized.



Let's add an age check to determine if the person is of legal age 
and the corresponding is_adult field, and use the __init__ method
 to call another method of the class during initialization.
"""


class Human:
    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age
        # Call the method during initialization
        self.is_adult = self.__check_adulthood()

        # Example of logging
        print(f"Created by Human: {self.name}, Age: {self.age}, Adult: {self.is_adult}")

    def say_hello(self) -> str:
        return f"Hello! I am {self.name}"

    def __check_adulthood(self) -> bool:
        return self.age >= 18


bill = Human("Bill")
print(bill.say_hello())
print(f"Age: {bill.age}, Adult: {bill.is_adult}")

jill = Human("Jill", 20)
print(jill.say_hello())
print(f"Age: {jill.age}, Adult: {jill.is_adult}")
print("~" * 30)

# Created by Human: Bill, Age: 0, Adult: False
# Hello! I am Bill
# Age: 0, Adult: False
# Created by Human: Jill, Age: 20, Adult: True
# Hello! I am Jill
# Age: 20, Adult: True




