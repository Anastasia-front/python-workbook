useful_link = (
    "https://docs.python.org/3/library/string.html#format-specification-mini-language"
)

# Control characters (control characters) are special characters
# used to control and format text in lines. They are often represented
# as escaped sequences starting with a backslash character (\).
# Some of the most common control characters in Python include:

# \n: New line (LF - Line Feed). Used to move to a new line.

# \r: Carriage Return (CR - Carriage Return). Used to move the cursor to the beginning of the line.

# \t: Horizontal Tab (HT - Horizontal Tab). Inserts a tab.

# \b: Slaughter (BS - Backspace). Used to delete the previous character.

# \f: Page feed (FF - Form Feed). Used to go to a new page.

print(dir(str))

s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end))  # 5
print(s.find("q"))  # -1
print(s.rfind("e"))  # 7
print(s.rindex("e"))  # 7
print(s.index("i"))
# s.index('o') #ValueError

# str.split(separator=None, maxSplit=-1)
result = s.split()
print(result)  # ['Hi', 'there!']
# string.join(iterable)
result = " ".join(result)
print(result)  # Hi there!

# str.replace(old, new, count=-1)
new_s = s.replace("there", "PythonPythonPython")
print(new_s)  # Hi PythonPythonPython!
new_text = new_s.replace("Python", "-", 2)
print(new_text)  # Hi --Python!
topic = "Data Visualization in R?"
new_topic = (
    topic.replace("Visualization", "Manipulation")
    .replace("R", "Python")
    .replace("?", "!")
)
print(new_topic)

print("TestBridgeHook".removeprefix("Test"))  # BridgeHook
print("TestBridgeHook".removesuffix("Hook"))  # TestBridge

# processing request parameters - split method
url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split("?")

obj_query = {}
for el in query.split("&"):
    key, value = el.split("=")
    obj_query.update({key: value.replace("+", " ")})
print(obj_query)


# a program that converts an input text string into the appropriate Morse code - translate method
morze_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}

# Conversion of dictionary keys to Unicode codes
table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v

string = "function is used with a key function that returns a tuple"

result = ""

for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(result)

print(dir(string))