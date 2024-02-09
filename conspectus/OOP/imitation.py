"""''Inheritance is an OOP mechanism that allows one class 
to inherit the properties and methods of another class. 
In Python, this is done by declaring a class that "inherits" from another class.

A base or parent class (superclass) is a class from which properties and methods are inherited.

A derived "похідний" or child class (subclass) is a class 
that inherits properties and methods from a base class."""

print("~" * 30)


class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"


class Dog(Animal):

    def __init__(self, nickname: str, age: int, breed: str):
        super().__init__(nickname, age)  # Call the constructor of the base class
        self.breed = breed  # Add a new property

    def make_sound(self) -> str:
        return "Woof"

    def chase_tail(self) -> str:  # Add a new method
        return f"{self.nickname} is chasing its tail"


class Cow(Animal):
    def make_sound(self):
        return "Moo"


my_cat = Cat("Simon", 4)
my_cow = Cow("Bessie", 3)

print(my_cat.make_sound())  # "Meow"
print(my_cow.make_sound())  # "Moo"

my_dog = Dog("Rex", 5, "Golden Retriever")
print(my_dog.make_sound())  # "Woof"
print(my_dog.chase_tail())  # "Rex is chasing its tail"
print("~" * 30)

"""Thus, there should be only one place in the code where 
the behavior of the object is defined. And if we need to get another object 
that has this behavior and some special features, we can inherit from a class 
with the common attributes we need and add unique ones. This approach allows 
to write less code and structure data by creating models of real objects 
with their characteristics (fields) and behavior (methods)."""


# Multi-level Imitation and Method Resolution Order (MRO)

"""Multilevel inheritance is when a class inherits from another class 
that is already a derived class. This creates a "chain" of imitation 
where opportunities are passed down through multiple levels."""


class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Bird(Animal):
    def make_sound(self):
        return "Chirp"


class Parrot(Bird):
    def can_fly(self):
        return True


class TalkingParrot(Parrot):
    def say_phrase(self, phrase):
        return f"The parrot says: '{phrase}'"


my_parrot = TalkingParrot("Alice", 2)
print(my_parrot.make_sound())  # Chirp
print(my_parrot.can_fly())  # True
print(my_parrot.say_phrase("Guten Tag"))  # The parrot says: 'Guten Tag'
print("~" * 30)

"""It is possible to imitate not only one class, but several at once. 
In this way, you can get objects that combine the properties of many classes. 
What if several classes have attributes with the same name?

To answer this question, it's necessary to understand how Python looks 
for attributes (fields or methods) in objects. MRO (Method Resolution Order) in Python, 
defines the order in which classes will be looked up when searching for methods.

Python determines MRO using a linear ordering algorithm.

The main idea behind this algorithm is to preserve the order of class definitions 
while ensuring that base classes are checked after all their derived classes.
"""

# MRO in Python works like this:

"""
1. Searches for an attribute among the attributes of the class itself. 
It is thanks to this that you can "override" parent attributes.
2. Searches for an attribute in the first parent (the one specified first in the list of parents).
3. Searches for the attribute in the next parent in the list of parents, as long as there are any.
4. Searches for the attribute in the parents of the first parent.
5. Repeats step 4 for all parents.
6. Throws an attribute not found exception.

Searches end as soon as the attribute is found.

You can view the MRO for any class using the mro() method or the __mro__ attribute.
"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro())  # Print the method resolution order for class D
print("~" * 30)


# Note that the call is made on the class itself, not the instance of the class. In this example, the output would be:

# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


"""This is the MRO order for class D, which means that Python will first look 
for methods in D, then in B, then in C, then in A, and finally 
in the built-in base object class, which is the ancestor of all classes."""
