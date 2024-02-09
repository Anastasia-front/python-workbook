import re

useful_link = "https://www.programiz.com/python-programming/regex"

# The main components of regular expressions include:

literally = "direct display of characters (eg a, B, 1)."
metaCharacter = "Characters that have special meaning in regular expressions \
    (for example, . (period) matches any character)."
quantifiers = "Determines how many times the element should match \
    (for example, * means 0 or more occurrences)."
character_classes = "Define groups of characters \
    (for example, [a-z] matches any lowercase letter)."
groups_and_ranges = "Used to group parts of an expression \
    (for example, (abc) defines a group of characters)."
alternations = "Matches one of several patterns \
    (for example, a|b matches a or b)."
anchors = "Define positions in the text \
    (for example, ^ for the beginning of a line, $ for the end of a line)."


# The main functions of the re module, which we will consider further, are:

search = "re.search(pattern, string) - searches for the first occurrence of a pattern in a string."
findall = "re.findall(pattern, string) - \
        finds all occurrences of a pattern in a string."
sub = "re.sub(pattern, repl, string) - replaces occurrences of the pattern with another string."
split = "re.split(pattern, string) splits a string by pattern."

# Regular expressions use special characters to create patterns.
"""They consist of blocks and modifiers.

An example of a block can be:

\w - any number or letter [a-zA-Z0-9_] (\W - everything except letter or number [^a-za-z0-9_])
\d - any number [0-9] (\D - everything except the number [^0-9])
\s - any whitespace character [\t\n\r\f\v] (\S - everything except the non-whitespace character [^\t\n\r\f\v])
\b is a word boundary
[...] is one of the characters in brackets ([^ ] is any character except those in brackets)
^ and $ are the beginning and end of the line, respectively
( ) — groups the expression and returns the found text
\t, \n, \r — tab, newline, and carriage return characters


Modifiers can indicate the number of repetitions of a block in an expression, for example:

. — one any character except the string \n
? — 0 or 1 occurrence of the pattern on the left
+ — 1 or more occurrences of the pattern on the left
* — 0 or more occurrences of the pattern on the left
\ — escape of special characters (example: \. — means a dot or \+ — a "plus" sign)
{n} strictly n times (n is an integer)
{n,m} — from n to m occurrences (example: {,m} — from 0 to m)
a|b — corresponds to a or b. The very symbol | means "or" between two patterns
( ) — groups the expression and returns the found text"""

# EXAMPLE
print("~" * 30)
# 1 - find needed word
text = "Learning Python can be fun."
pattern = "Python"
match = re.search(pattern, text)

if match:
    print("Found:", match.group())
else:
    print("Not found.")
print("~" * 30)

# 2 - find word which start from "c" and end by "n"
pattern = r"c\w*n"
match = re.search(pattern, text, re.IGNORECASE)

if match:
    print("Found:", match.group())
print("~" * 30)

# 3 - find email
text = "My email address is example@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)

if match:
    print("Email address:", match.group())
print("~" * 30)

# 4 - remove the username and domain of this email address separately
email = "random@fix.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, email)

if match:
    user_name = match.group(1)
    domain_name = match.group(2)
    print("User name:", user_name) # random
    print("Domain:", domain_name) # fix.com
print("~" * 30)

# 5 - find all the numbers in the string
text = "I like number 777, but 28654323 more"
pattern = r"\d+"
matches = re.findall(pattern, text)

print(matches)
print("~" * 30)

# 6 - we need words that have at least one letter
text = "Elements in a string can be accessed by using indices."
pattern = r"\w+"
matches = re.findall(pattern, text)

print(matches)
print("~" * 30)

# 7 - find all emails
text = "Contacts: example1@example.com, example2@sample.org"
pattern = r"\w+@\w+\.\w+"
matches = re.findall(pattern, text)

print(matches)
print("~" * 30)

# 8 - replace all whitespace characters with underscores.
file_name = "My file Python.txt"
pattern = r"\s"
replacement = "_"
formatted_name = re.sub(pattern, replacement, file_name)

print(formatted_name)
print("~" * 30)

# 9 - remove all punctuation marks from the line
text = "The very first - index is 0, not 1... \
    Therefore, if a string! has 10 elements, :the very last; index will be 9."
pattern = r"[;,\-:!\.]"
replacement = ""
modified_text = re.sub(pattern, replacement, text)

print(modified_text)
print("~" * 30)

# 10 - formatting phone numbers
phone = """
        Kate Ross: 987-171-1634
        George Bush: 345-134-1729
        Rodger Samuel: 678-234-5612
        """
pattern = r"(\d{3})-(\d{3})-(\d{4})"
replacement = r"(\1) \2-\3"
formatted_phone = re.sub(pattern, replacement, phone)

print(formatted_phone)
print("~" * 30)

# 11 - divide the line into words using spaces as separators
text = "Surprisingly the country that has won the majority of the \
    Nobel prizes is the USA, even if the first winners were all Europeans."
pattern = r"\s+"
words = re.split(pattern, text)

print(words)
print("~" * 30)

# 12 - split a string into parts using punctuation marks as separators
text = "{'N': 2; 'o': 7! 'w': 9& 'p': 26? 'e': 17$ 'k': 1% \
    'n':  7; 'g': 3, ':': 1, 'b': 1, 'l': 5, 'u': 1, '.': 2}"
pattern = r"[;$%&?,\-:!\s]+"
elements = re.split(pattern, text)

print(elements)
print("~" * 30)

print("dir(re)")
print(dir(re))
print("~" * 30)
