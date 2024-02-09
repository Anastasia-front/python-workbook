OOP = "The method of organizing programs, when combining data and functionality \
inside some object, is called an object-oriented programming paradigm."

"""OOP has four main concepts that distinguish it from other programming methodologies:

Abstraction
Encapsulation
Imitation - "Наслідування"
Polymorphism


Briefly note that abstraction is a model of some object or phenomenon from the real world, 
discarding minor details that do not play a significant role in the context of considering the OOP concept.
"""


"""In OOP, a program is considered as a set of objects that interact with each other. 
The most important units of a program are classes and objects. You write classes 
that describe real-world objects and situations, and then create objects based on 
those descriptions. Each object belongs to a certain class and stores all information 
about its own data and functionality.

Classes are a programming language structure that allows you to combine variables 
of different types (fields, attributes) and functions (methods) within the framework of one entity."""

class_attribute = """is a variable that is defined at the class level,
not at the class instance level. This means that it is shared by all instances of this class. 
Class attributes are used to store data that must be the same for all objects of the class.
"""


class MyClass:
    class_attribute = "I am a class attribute"


# All MyClass instances will have the same class_attribute value.


class_field = """(sometimes called an "instance attribute") -  is a variable that is defined 
at the level of an individual instance of a class. Each instance of a class has its own set of fields, 
which can take different values for different instances. A field can be any Python object. 
This is usually a variable or container (dictionary, list, string, etc.). 
Class fields are used to store data that is specific to each individual object.
"""


class MyClassTwo:
    def __init__(self, value):
        self.instance_field = value  # Class field


obj1 = MyClassTwo(5)
obj2 = MyClassTwo(10)


class_method = "is a function that operates on the class's fields and/or arguments passed to the method."


"""
Class methods describe the behavior of a class and how it interacts with other objects. 
In order for a class method to work with other class methods and fields, 
the first argument of any method is always the class object itself. 
Any name that doesn't cause a syntax error can be used for the first argument,
but the convention is to always use self.

Any class method must always have at least one self argument, 
this is a requirement of the Python syntax, because the interpreter 
during the method call will necessarily pass the object itself as the first argument, 
and then all the arguments that were passed during the call .
"""

print("~" * 30)


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_name(self) -> None:
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

    def set_age(self, age: int) -> None:
        self.age = age


bob = Person("Boris", 34)

bob.say_name()  # Hi, I am Boris and I am 34 years old.
bob.set_age(25)
bob.say_name()  # Hi, I am Boris and I am 25 years old.
print("~" * 30)

# Difference between a field and a class attribute


"""
In OOP, field and class attribute are two terms that are often used interchangeably. 
However, there is a subtle difference between them.



A class variable or attribute is a variable that is stored in a class
and is accessible by all instances of that class.
There is only one class variable, and any of the objects, 
when changing the class variable, changes it for the rest of the instances of the same class.



An object variable or field is a variable that is stored in an object. 
They belong to each individual instance of the class. 
In this case, each object has its own copy of the field, that is, 
it is in no way related to other same fields in other instances."""


class PersonTwo:
    count = 0

    def __init__(self, name: str):
        self.name = name
        PersonTwo.count += 1

    def how_many_persons(self):
        print(f"The number of people now is {PersonTwo.count}")


first = PersonTwo("Boris")
first.how_many_persons()  # The number of people is now 1
second = PersonTwo("Alex")
first.how_many_persons()  # The number of people is now 2
print("~" * 30)

# Here, count belongs to the Person class and is a class attribute.


class PersonThree:
    count = 0

    def __init__(self):
        self.count = 10


personThree = PersonThree()
print(personThree.count)  # 10
print(PersonThree.count)  # 0
print("~" * 30)

# Here, person.count returns 10 - the field value of the person object,
# and Person.count returns a class attribute with a value of 0.

"""
But the main difference is not how they are declared,
but how and where these variables are changed and used in the class.
"""


# EXAMPLE


class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health

    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")

    def dodge(self):
        print(f"{self.name} dodged the attack!")

    def evolve(self, new_form):
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form


# creation of object Pikachu
pikachu = Pokemon("Pikachu", "Electric", 100)

# using of methods
pikachu.attack(Pokemon("Charmander", "Fire", 100))
pikachu.dodge()
pikachu.evolve("Raichu")

print("~" * 30)
