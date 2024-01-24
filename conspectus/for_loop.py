# zip method
colors = ["green", "ripe", "red"]
fruits = ["apple", "cherry", "tomato"]

print("~" * 30)
for color, fruit in zip(colors, fruits):
    print(color, fruit)
# green apple
# ripe cherry
# red tomato
print("~" * 30)

"""When the collections passed to zip are of different lengths,
zip processes the elements until it runs out of elements in the shortest collection.
This means that the iteration stops as soon as the end of one of the collections
is reached, and any additional elements in the other, longer collections are ignored."""

numbers = [1, 2, 3]
letters = ["a", "b", "c", "d", "e"]

for number, letter in zip(numbers, letters):
    print(number, letter)
# 1 a
# 2 b
# 3 c
print("~" * 30)


text = "Now we know how we can create a string: both single and multiline.\
      Now we need to learn how can we access certain elements in the string."
alphabet = "abcdefghijklmnopqrstuvwxyz"

# list - enumerate method
words = []
start = 0

for index, char in enumerate(text):
    if char.lower() not in alphabet:
        word = text[start:index]
        words.append(word.strip())
        start = index
print(words)
print("~" * 30)

# dict - get method
dict_counter = {}

for char in text:
    count = dict_counter.get(char, 0)
    count += 1
    dict_counter[char] = count

print(dict_counter)
print("~" * 30)

sorted_data = sorted(dict_counter.items(), key=lambda x: (x[1], x[0]))

sorted_dict = dict(sorted_data)

print(sorted_dict)
print("~" * 30)

"""It's important to remember what you can't do while iterating over the dictionary:
you can't remove elements from the dictionary, you can't add elements to the dictionary.
But you can overwrite the values if you iterate over the keys.
The same applies to the list - it is not possible to delete elements of the list
and it is not possible to add elements to the list during iterations in the loop."""

# set - add method
char_set = set()
symbol_set = set()


for el in text:
    if el.lower() in alphabet:
        char_set.add(el)
    else:
        symbol_set.add(el)

print(f"Chars {char_set}")
print(f"Symbols {symbol_set}")
print("~" * 30)
# range(start, stop, step)
