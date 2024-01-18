text = "Now we know how we can create a string: both single and multiline.\
      Now we need to learn how can we access certain elements in the string."
alphabet = "abcdefghijklmnopqrstuvwxyz"

# list
words = []
start = 0

for index, char in enumerate(text):
    if char.lower() not in alphabet:
        word = text[start:index]
        words.append(word.strip())
        start = index
print(words)

# dict
dict_counter = {}

for char in text:
    count = dict_counter.get(char, 0)
    count += 1
    dict_counter[char] = count

print(dict_counter)

sorted_data = sorted(dict_counter.items(), key=lambda x: (x[1], x[0]))

sorted_dict = dict(sorted_data)

print(sorted_dict)

# set
char_set = set()
symbol_set = set()
    

for el in text:
    if el.lower() in alphabet:
        char_set.add(el)
    else:
        symbol_set.add(el)

print(f'Chars {char_set}')
print(f'Symbols {symbol_set}')