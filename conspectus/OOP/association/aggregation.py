"""
Aggregation is a type of relationship between objects that also represents 
a "whole" to "part" relationship, but in this case the "parts" can exist 
independently of the "whole". This means that if the "whole" is destroyed, 
the "parts" can continue to exist independently. Aggregation indicates a looser 
relationship between objects and is often used when objects may belong to different 
groups or collections. For example, a library (whole) can contain books (parts) 
through aggregation; if the library closes, the books will still remain and can be moved to another library.

Consider an example that illustrates why imitation is not the best solution, 
and how association between these classes through aggregation is a more appropriate approach.

First, consider a situation where we might wrongly decide to use imitation. 
We have an Owner class for the owner of the cat and a Cat class for the cat itself.
"""


class Owner:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"


class Cat(Owner):
    def __init__(self, nickname, age, name, phone):
        super().__init__(name, phone)
        self.nickname = nickname
        self.age = age

    def cat_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"


print("~" * 30)
cat = Cat("Simon", 4, "Boris", "+380503002010")
print("not right")
print("cat.info()")
print(cat.info())  # Boris: +380503002010
print("cat.cat_info()")
print(cat.cat_info())  # Cat Name: Simon, Age: 4
print("~" * 30)
"""
It may seem like a good idea to make the cat "part" of the owner 
by using imitation. It would be as if we were saying,
"The cat is the master." But that doesn't make sense, does it? 
A cat and an owner are two different things.

A cat cannot be a master. It just has a master.

Instead, we must show that the cat "has" an owner. 
This does not make the cat the master. It simply means that 
there is a connection between a cat and a person. 
A person is the owner of a cat, and a cat is a pet of this person.
"""


class Owner:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"


class Cat(Owner):
    def __init__(self, nickname: str, age: int, owner: Owner):
        self.nickname = nickname
        self.age = age
        self.owner = owner

    def get_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"

    def sound(self):
        return "Meow"


owner = Owner("Boris", "+380503002010")
cat = Cat("Simon", 4, owner)
print("right")
print("cat.owner.info()")
print(cat.owner.info())  # Boris: +380503002010
print("cat.get_info()")
print(cat.get_info())  # Cat Name: Simon, Age: 4
print("~" * 30)

"""
In this example, Cat and Owner are associated through an aggregation 
where Cat has a reference to Owner, but Owner objects can exist independently of Cat. 
Here we say: "The cat has a master", which is more logical and correct from the point 
of view of our program. This reflects the real relationship between cats and their owners 
more accurately and allows cats to have or not have an owner without breaking logic.

Aggregation allows the "part" to exist independently of the "whole". 
In example, this means that the master can exist separately from the pet. 
An instance of the host is created independently and only then is associated 
with the animal, being passed to the pet's constructor as a parameter."""
