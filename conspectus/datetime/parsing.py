from datetime import datetime

current_datetime = datetime.now()


# Parsing data from a string

"""The strftime method is used to format datetime objects into 
strings using specific format codes. This method allows you 
to present the date and time in a readable format or 
in a format that meets specific requirements.


The syntax of the strftime method is as follows:
datetime_object.strftime(format)

Where datetime_object is a datetime object and format is 
a format string that specifies how the date and time should be represented.


Each code in the format string begins with the % character and 
represents a specific component of the date or time. 

Here are some of the most used codes:

%Y is a four-digit year (for example, 2023).
%y is a two-digit year (for example, 23).
%m - month as a number (eg 03 for March).
%d is the day of the month as a number (eg 14).
%H - hour (24-hour format) (for example, 15).
%I - hour (12-hour format) (for example, 03).
%M - minutes (for example, 05).
%S - seconds (eg 09).
%A - the full name of the day of the week (for example, Tuesday).
%a - shortened name of the day of the week (for example, Tue).
%B - the full name of the month (for example, March).
%b or %h is the abbreviated name of the month (for example, Mar).
%p - AM or PM for 12-hour format."""

print("~" * 30)
formatted_date_and_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"formatted_date_and_time - {formatted_date_and_time}") # 2024-02-15 09:57:28


# formatted_date_only = current_datetime.strftime("%A, %d %B %Y") # Thursday, 15 February 2024
formatted_date_only = current_datetime.strftime("%d.%m.%Y") # 15.02.2024
print(f"formatted_date_only - {formatted_date_only}")


formatted_time_only = current_datetime.strftime("%I:%M %p")
print(f"formatted_time_only - {formatted_time_only}") # 09:57 AM
print("~" * 30)

"""The strptime method in Python is used to convert strings into datetime objects. 
This method is the opposite of strftime, which converts datetime objects to strings. 
strptime allows you to parse strings containing date and/or time and convert them 
into structured datetime objects using a specified format.


The syntax of the strptime method is as follows:
datetime_object = datetime.strptime(string, format)
where:
string - a string that contains a date and/or time.
format - a format string that specifies how to parse the string.

The formatting codes for strptime are the same as for strftime. For example, 
%Y represents a four-digit year, %m represents a two-digit month, and so on."""

# Suppose we have a date as a string
date_string = "2023.03.14"

# Convert a string into a datetime object
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(
    f"datetime_object - { datetime_object}"
)  # Prints a datetime object corresponding to the specified date and time
print("~" * 30)

print("dir(datetime)")
print(dir(datetime))
print("~" * 30)
