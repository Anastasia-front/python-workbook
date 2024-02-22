import csv

"""
Another format of information exchange that is very often used is a tabular representation. 
An open format for storing tabular data, which is supported by any editor, is the CSV format.

CSV (Comma-Separated Values) is a file format used to store tabular data. 
Its name comes from the main idea - the use of a comma to separate values in the middle of a line. 
However, in practice, other characters can be used as a separator, such as a semicolon; or a tab character. 
A CSV file is easy to read and create by both humans and programs, making it a popular choice for data exchange.


A CSV file consists of rows, and each row represents one record. Entries are divided into fields, 
which are usually separated by commas. The first line in the file is often used for headers 
that describe the contents of each field in the records.

Suppose we have a table with data about students, which contains name, age and major. In CSV format, this table might look like this:

name, age, specialty
Julia, 30, Mathematics
Maria, 22, Physics
Ross, 20, Informatics

Here, a comma is used as a separator, and the first line contains the field headers.

CSV files are widely used to exchange data between different programs and systems. 
For example, data tables can be exported from databases or spreadsheets in CSV format for further use in other applications. 
Since CSV is a text format, it can be easily created, edited or viewed using simple text editors. 
You can easily download this file to Google Excel and work with it like a regular table.


In Python, working with CSV files is greatly simplified thanks to the built-in csv module. 
This module provides functionality for reading from and writing to CSV files.

To read data from a CSV file, you can use the csv.reader function, 
which returns an object that iterates over the lines of the file.
"""
print("~" * 30)

folder_path = "example"
file_path = f"{folder_path}/students.csv"
# # Open the CSV file
# with open(file_path, newline="", encoding="utf-8") as csvfile:
#     # Create a reader object
#     reader = csv.reader(csvfile, delimiter=",")
#     # We go through each line in the file
#     for row in reader:
#         print(", ".join(row))

# print("~" * 30)

"""When opening the file, we used the newline='' parameter to correctly handle lines regardless of the operating system. 
The parameter encoding='utf-8' guarantees correct reading of the file with Cyrillic.

The parameter newline='' is new for us here. Different operating systems use different characters 
to mark the end of a line in text files: Windows uses carriage return and line feed \r\n, 
Linux and MacOS use only line feed \n, older versions of MacOS, up to version 10 used carriage return \r altogether.

When we open a file for reading or writing, the newline='' parameter instructs Python not to do any special handling 
of end-of-line characters. Our CSV file can be created or used in different operating systems and improper handling 
of line ends can lead to concatenation of lines or incorrect separation of them, which will break the structure 
of the data in the file. Therefore, using newline='' ensures that the csv module correctly interprets line ends 
regardless of the operating system on which the code is executed.

You can use the csv.writer function to write data to a CSV file. It allows you to easily write data lines to a file.
"""


# Data to record
rows = [
    ["name", "age", "specialty"],
    ["Julia", 30, "Mathematics"],
    ["Maria", 22, "Physics"],
    ["Ross", 20, "Informatics"],
]

# Open the file for recording
with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
    # We create the writer object
    writer = csv.writer(csvfile, delimiter=",")
    # We record lines of data
    writer.writerows(rows)

with open(file_path, newline="", encoding="utf-8") as csvfile:
    # Create a reader object
    reader = csv.reader(csvfile, delimiter=",")
    # We go through each line in the file
    for row in reader:
        print(", ".join(row))

print("~" * 30)

"""
With the help of writer.writerows(rows), you can write several lines at once. 
If you want to write one row, you can use writer.writerow(row).

The csv module also provides the csv.DictReader and csv.DictWriter classes, 
which allow you to work with strings like dictionaries. This is useful when the CSV file has column headers.

Let's consider a couple of examples to understand how it works. 
Because using DictReader and DictWriter facilitates access to fields
 by their names and automates the process of writing column headers.
"""


# Recording in a CSV file from dictionaries
with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["name", "age", "specialty"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"name": "Olivia", "age": 23, "specialty": "History"})
    writer.writerow({"name": "Anna", "age": 22, "specialty": "Biology"})

# Reading from a CSV file into dictionaries
with open(file_path, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["name"], row["age"], row["specialty"])

print("~" * 30)

"""
The instruction csv.DictWriter(csvfile, fieldnames=fieldnames) creates an object for writing, 
where fieldnames is a list of field names that defines the order and column headings in the CSV file. 
As the name of the writer.writeheader() method suggests, it writes the header line to the file. 
And finally writer.writerow() is used to write each row of data to a file. The data is passed
in the form of a dictionary, where the keys correspond to the field names defined in fieldnames.

When reading a CSV file, csv.DictReader(csvfile) creates an object to iterate over the lines of the file, 
where each line is represented as a dictionary. The keys in these dictionaries correspond to the headers 
in the first line of the CSV file. In the loop for row in reader: 
each row is a dictionary where you can access field values by their names.

The following example:
"""

file_path = f"{folder_path}/users.csv"
users = [
    {"name": "Mark", "age": 22, "gender": "male"},
    {"name": "Maria", "age": 22, "gender": "female"},
    {"name": "Jacob", "age": 22, "gender": "male"},
]

with open(file_path, "w", encoding="utf-8", newline="") as f:
    columns = users[0].keys()
    writer = csv.DictWriter(f, delimiter=",", fieldnames=columns)
    writer.writeheader()
    for row in users:
        writer.writerow(row)

with open(file_path, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)

print("~" * 30)

"""
Note that here we defined the names of the columns by the keys 
of the first dictionary in the users list: columns = users[0].keys().

The approach of working with CSV files through the DictReader and DictWriter classes 
makes the code more understandable and provides ease of data manipulation, 
as it is possible to use field names instead of indexes. 
Which allows you to write lighter and more maintainable code."""
