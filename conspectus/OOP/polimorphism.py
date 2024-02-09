from typing import Protocol

"""
Polymorphism is one of the key concepts of OOP, which allows objects 
to have different forms or behaviors based on their types.

Polymorphism comes from the Greek words "polys" (many) and "morph" (form). 
In the context of OOP, this refers to the ability of different classes to use 
methods with the same name but with different implementations. 
This allows one interface to be used for different data types.

When we looked at imitation in the animal example, we already saw dynamic polymorphism:
"""

print("~" * 30)


class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "Meow"


class Dog(Animal):
    def make_sound(self):
        return "Woof"


def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat("Simon", 4), Dog("Rex", 5)]
animal_sounds(animals)

print("~" * 30)

"""
Therefore,polymorphism allows to process objects of different classes, 
which are derived from the same base class, through a common interface (that is, through the same methods).

Thus, polymorphism allows the animal_sounds function to interact with Cat and Dog objects 
as if they were Animal objects, using their common interfaces, regardless of the difference 
in their internal implementation. This makes the code more flexible and more adaptable to changes, 
as we can add new classes that inherit from Animal without having to change the animal_sounds function.
"""

# The concept of duck typing is closely related to polymorphism.


duck_typing = '''is a programming concept that plays an important role 
in dynamically typed languages such as Python. The name comes from the English expression 
"If it walks like a duck and quacks like a duck, it's probably a duck."'''

"""
In a programming context, duck typing means that instead of checking the type 
of an object before using it, it is more important to focus on whether the object 
has the necessary methods or properties required to perform a certain function or operation.

The Python mechanism allows any objects to be used interchangeably, 
so that both have the required methods and fields. The interpreter does not check 
that an object of the required or child class was passed to the function or method, 
it is enough that the object has the required methods and everything will work.
"""


class Duck:
    def quack(self):
        print("Quack, quack!")


class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")


def make_it_quack(duck):
    duck.quack()


duck = Duck()
person = Person()

make_it_quack(duck)  # Quack, quack!
make_it_quack(person)  # I'm Quacking Like a Duck!

print("~" * 30)


"""
In Python, you can use static typing to annotate types 
while relying on duck typing for polymorphism and flexible object behavior.


To annotate the type of the parameter of the speaker function, we can use typing.Protocol, 
which defines a set of methods that this parameter should perform without being bound to a specific class.



Let's create an interface using typing.Protocol for objects that can "speak". 
We want any object that has a speak method to be considered compatible with this interface.
"""


class Speaker(Protocol):
    def speak(self) -> str:
        pass


class Dog:
    def speak(self) -> str:
        return "Woof"


class Cat:
    def speak(self) -> str:
        return "Meow"


class Robot:
    def speak(self) -> str:
        return "Beep boop"


def make_it_speak(speaker: Speaker) -> None:
    print(speaker.speak())


dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  #  Woof
make_it_speak(cat)  # Meow
make_it_speak(robot)  #  Beep boop

print("~" * 30)

"""
Thus, static typing helps to ensure that types are correct at design time,
while duck typing provides implementation flexibility by allowing objects 
of different classes to share a common interface."""
