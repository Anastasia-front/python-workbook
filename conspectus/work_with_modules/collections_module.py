from collections import Counter, defaultdict, namedtuple

"""Python has a package with additional collections that can be very 
useful for a beginner developer and greatly expand his arsenal. 
The collections module in Python is a built-in module that contains 
specialized data types that provide alternatives to standard built-in 
containers. These specialized data types are designed 
to solve specific programming problems."""


# Named tuples


"""
Using tuples in Python to pass data between handler functions 
is a good and common practice. But tuples have one inconvenience - 
we need to remember the indexing of elements in the tuple and 
not to confuse their order. It is not always convenient and for 
situations when there are quite a lot of elements in the tuple, 
this approach complicates the readability of the code.

That's why named named tuples in Python were invented. 
This is an extension of the standard tuple data type that allows 
you to access list elements by name rather than by index. 
Which makes our code easier to read and more understandable."""


named_tuple = "is created using the namedtuple \
function from the collections module."


# Create a named tuple
Point = namedtuple("Point", ["x", "y"])


"""In this example, Point is a named tuple that has fields 
named x and y. Now we can refer to an element of such a tuple by name:
"""

# Create an instance of Point
p = Point(11, y=22)
print("~" * 30)
# Access to elements
print(p.x)  # 11
print(p.y)  # 22
print("~" * 30)

"""Consider the following tuple that stores first name, 
last name, age, city of birth, and zip code:
"""


person = ("Mick", "Mitch", 35, "Boston", "01146")


"""After creating person where you use it, you need to remember
that name comes first and age comes third. In order not to get 
confused, you will have to constantly return to the code where 
person is created and check yourself. This is inconvenient 
and named tuples were added specifically for such cases.
"""


# Let's consider how they can be used.

# Create a tuple named Person
Person = namedtuple(
    "Person", ["first_name", "last_name", "age", "birth_place", "post_index"]
)

# Create an instance of Person
person = Person("Mick", "Mitch", 35, "Boston", "01146")

# Output of various attributes of the named tuple
print(person.first_name)  # Mick
print(person.post_index)  # 0 1146
print(person.age)  # 35
print(person[3])  # Boston
print("~" * 30)

"""
Now, using the named tuple Person, you can create tuples 
that must contain 5 elements and such tuples have names 
in addition to indices. Each element of a tuple can be 
obtained both by name and by index, which provides 
flexibility in data access. With this approach, you only 
need to define Person once and never have to go back to 
it to remember which element is responsible for what.

Let's consider another example of using a named tuple 
when presenting information about a cat. This code is 
a great example of using named tuples for convenient 
and easy-to-understand data management.

"""

Cat = namedtuple("Cat", ["nickname", "age", "owner"])
cat = Cat("Simon", 4, "Rabat")
print(f"This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}")

# The next line of code is much less informative in our case.
print(f"This is a cat {cat[0]}, {cat[1]} age, his owner {cat[2]}")
print("~" * 30)

"""Named tuples in Python are a powerful tool for creating 
data structures that are immutable and more understandable 
than regular tuples. They are particularly useful for applications 
that manipulate complex data sets and require a clear structure."""

print('dir(named_tuple)')
print(dir(named_tuple))
print("~" * 30)

# Counter



"""To create a Counter, simply pass it an iterable object. 
So the previous example can be rewritten as follows:
"""

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = Counter(student_marks)
print(mark_counts)  # Counter({4: 4, 6: 3, 1: 3, 2: 2, 7: 2, 3: 2, 5: 2})
print("~" * 30)

"""One of the most popular Counter methods is most_common(), 
which returns a list of elements and their frequency, 
starting with the most common. This method can be extremely 
useful for data analysis when it is important to determine 
which elements occur most often.
"""

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = Counter(student_marks)

print(
    mark_counts.most_common()
)  # [(4, 4), (6, 3), (1, 3), (2, 2), (7, 2), (3, 2), (5, 2)]
print(mark_counts.most_common(1))  # [(4, 4)]
print(mark_counts.most_common(2))  # [(4, 4), (6, 3)]
print("~" * 30)

"""For example, if you need to count the number of each letter in a string, 
just pass the string directly to Counter. Then you can easily access 
the number of each letter using keys, just like in a regular dictionary.
"""

# Creating a Counter from a string
letter_count = Counter("banana")
print(letter_count)  # Counter({'a': 3, 'n': 2, 'b': 1})
print("~" * 30)

"""Counting the words in the text also becomes a fairly simple task:
"""
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = Counter(words)

# Output of the word and its frequency
for word, count in word_count.items():
    print(f"{word}: {count}")
print("~" * 30)
# Output:
# the: 2
# quick: 1
# brown: 1
# Fox: 1
# jumps: 1
# over: 1
# lazy: 1
# dogs: 1


"""Using Counter is intuitive and at the same time extremely
 powerful for solving many tasks related to counting and data analysis.
"""
print('dir(Counter)')
print(dir(Counter))
print("~" * 30)

# defaultdict


"""
The custom dictionary defaultdict is a subclass of the Python dictionary dict, 
which is included in the collections module. This type of dictionary allows you 
to assign default values to keys that do not already exist in the dictionary.

In a regular Python dictionary, attempting to access a key that does not exist 
raises a KeyError exception. In defaultdict, if a key does not exist, it is 
automatically created with the value returned by the function passed when creating defaultdict.

When creating a defaultdict, you must pass a function that returns 
the default value for the new keys. This can be any object that 
can be called, such as an int, list, set, or even your own function.
"""

# Create defaultdict with list as default factory
d = defaultdict(list)

# Adding items to the list for each key
d["a"].append(1)
d["a"].append(2)
d["b"].append(4)

print(d)  # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})
print("~" * 30)

"""In this example, if we refer to a key that does not yet exist, 
defaultdict automatically creates a new list for it 
and this does not lead to errors in the code.
"""


# The following example where defaultdict uses int
# as the default function, which means that each new key is initialized to 0.

d = defaultdict(int)

# Increment value for each key
d["a"] += 1
d["b"] += 1
d["a"] += 1

print(d)  # defaultdict(<class 'int'>, {'a': 2, 'b': 1})
print("~" * 30)

"""Why is it needed and when can it be needed? For example, 
you have a list of words and you want to split it into 
several lists based on the first letter of the word.
"""

words = ["apple", "zoo", "lion", "lama", "bear", "bet", "wolf", "appendix"]
grouped_words = {}

for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)

print(grouped_words)
print("~" * 30)
# In the console we will see:
{
    "a": ["apple", "appendix"],
    "z": ["zoo"],
    "l": ["lion", "lama"],
    "b": ["bear", "bet"],
    "w": ["wolf"],
}


"""In this way we can get all the words from words that start with some letter. 
Such tasks are quite common. Here we always have to check if we have created 
an empty list for the char key in the grouped_words dictionary:"""


#   if char not in grouped_words:
#          grouped_words[char] = []

"""
If we do not make such a check, then the operation grouped_words[char].append(word) 
will lead to an error, because there is no empty list for the char key. 
And we are trying to add something there.



To avoid checking whether there is a list for that letter in the 
grouped_words dictionary, we can use defaultdict from collections 
and default to an empty list:"""

words = ["apple", "zoo", "lion", "llama", "bear", "bet", "wolf", "appendix"]
grouped_words = defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(dict(grouped_words))
print("~" * 30)

"""The result will be identical. defaultdict takes as an argument
 the function that will be used to create the default value. 
 We used list in this example, but you can pass any function 
 that is called with no arguments."""

print('dir(defaultdict)')
print(dir(defaultdict))
print("~" * 30)