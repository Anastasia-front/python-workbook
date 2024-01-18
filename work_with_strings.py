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

print("TestBridgeHook".removeprefix("Test"))  # BridgeHook
print("TestBridgeHook".removesuffix("Hook"))  # TestBridge
