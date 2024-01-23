# Collections
collection = """a program object (container variable) that stores a set of values of one or different types."""

# The main collection types in Python :

lists = """ordered collections that can contain elements of any type. 
Lists are mutable, which means you can change, add, or remove items after they are created."""

tuples = """similar to lists, but they are immutable. This means that once a tuple is created, it cannot be modified. 
Tuples are often used to store data that should not change while the program is running."""

dictionaries = """collections of key-value pairs where each key is unique. 
Dictionaries are used when quick access to elements by key is required."""

sets = """unordered collections of unique items. 
Used to remove duplicates and perform operations that are typical 
for mathematical sets, such as union, intersection, difference."""

frozen_sets = """these are invariant versions of sets. 
Such sets cannot be changed after they are created."""

# list methods

chars = ["a", "b", "c"]
numbers = [1, 2]
chars.extend(numbers)
chars.insert(1, "b")
c_ind = chars.index("b")
chars_copy = chars.copy()
copy_chars = chars[:]
count = chars.count("b")
first = chars.pop(-1)
last = chars.remove(1)
chars.sort(reverse=True)
chars.reverse()
reverse_chars = chars[::-1]
chars.clear()  # []
print(dir(list))

# dict methods

info = {"name": "Julia", "age": 14, "city": "Kharkiv", "email": "usere@example.com"}
info["number"]=483498438
print(f'This is value of number key - {info["number"]}')
print("name" in info)
del info["city"]
info.pop("email")
info.update({"color": "yellow", "number": 67})
new_info = info.copy()
# without KeyError if key is't in dict
level = info.get("level")
# caused KeyError
# level = info["level"]
info.clear()
print(dir(dict))

# set methods
lst = [1, 2, 3, 1, 2, 2, 3, 4, 1]
d_lst = set(lst)
d_lst.add(5)
d_lst.remove(3)
d_lst.discard(3)
a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # {3}
print(a & b)  # {3}
print(a.difference(b))  # {1, 2}
print(a - b)  # {1, 2}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
print(a ^ b)  # {1, 2, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}
print(dir(set))

my_frozenset = frozenset([1, 2, 3, 4, 5])
print(my_frozenset)
print(dir(frozenset))

# tuple methods
my_tuple = tuple(lst)
my_tuple.count(1)
my_tuple.index(2)
print(my_tuple)
print(dir(tuple))

# string method
s = "Responsive Mockup of an iMac with a White iPad and iPhone"
s.upper()
s.lower()
s.title()
s.capitalize()
s.isalpha()

# unpacking lists and dictionaries
my_list = [1, 2, 3]
a, b, c = my_list
a, _, c = my_list
a, *rest = my_list
print(*rest)


def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")


person_info = {"name": "Alice", "age": 25}
greet(**person_info)
