"""When exactly such a technique of string comparison is used? 
When searching or filtering data, where it is important 
to ignore the difference in case, for example, 
searching for a user by name in a database. 
In web applications, to ensure consistent comparison 
of entered data, for example, when logging in or searching the site."""

print("~" * 30)
string1 = "Hello World"
string2 = "hello world"
if string1.lower() == string2.lower():
    print("Rows are the same")
else:
    print("Rows are different")
# Output - The lines are the same
print("~" * 30)

"""But comparing strings in Python can give ambiguous 
results due to the fact that in UTF-8 encoding the same character 
can be represented by several codes, for example, 
the character 'ê' can be represented by the code U+00EA, 
or as a sequence of two codes U+0065 and U+0302. 
For this reason, a comparison of the same character 
may return False due to differences in notation.
"""


"""To solve this problem when working with non-ASCII characters 
to compare strings, they must be normalized using the casefold method, 
which returns a string where all characters are lowercase and 
without ambiguities, where any character will have only one possible writing form.
"""


"""This method is similar to lower(), but casefold() 
is more radical: it is designed to remove all case differences 
that may occur between languages, and is therefore more efficient 
for cases where you need to ensure case insensitivity across languages.
"""

text = "Python Programming"
print(text.casefold())  # python programming
print("~" * 30)

"""But the main use of casefold() is for languages 
where one letter can have different upper and 
lower case, for example, in German.
"""


"""In German, the letter "ß" (called "sharp S" or "eszett") 
is used to indicate a specific sound that approximates 
a doubled "ss". This letter has no direct equivalent in upper case. 
Traditionally, when a word containing "ß" needs 
to be capitalized, "ß" is converted to "SS".
"""


# This is where casefold() comes in handy:

german_word = "straße"  # In lower case
search_word = "STRASSE"  # In upper case

# Comparison using lower()
lower_comparison = german_word.lower() == search_word.lower()

# Comparison using casefold()
casefold_comparison = german_word.casefold() == search_word.casefold()

print(f"Comparison with lower(): {lower_comparison}")  # Comparison with lower(): False
print(
    f"Comparison with casefold(): {casefold_comparison}"
)  # Comparison with casefold(): True
print("~" * 30)

"""In this example, casefold() will correctly assume that 
the strings "straße" and "STRASSE" are equivalent because 
it takes into account the special conversion of "ß" to "ss". 
This can be important in scenarios where you need to ensure 
exact case-independent text comparisons, 
such as database searches or user input.
"""

"""This case shows that casefold() is more efficient 
for languages that have special rules for converting characters 
in different cases. In most real-life scenarios, especially 
when dealing with English text, lower() and casefold() will 
work similarly, but casefold() provides additional 
precision for specific language cases.
"""
