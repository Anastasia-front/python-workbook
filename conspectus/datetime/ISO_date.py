from datetime import datetime

current_datetime = datetime.now()

# Working with ISO date format


"""The ISO date format refers to the international standard
for the representation of dates and times known as ISO 8601.
   This standard was created by the International Organization
for Standardization (ISO) and is used to unify
the representation of dates and times around the world.

The date format in ISO 8601 looks like "YYYY-MM-DD" where:
YYYY is the year (eg 2023),
MM is the month (for example, 01 for January),
DD is the day (for example, 31).


The time format in ISO 8601 looks like "HH:MM:SS", where:
HH - hours (from 00 to 23),
MM - minutes (from 00 to 59),
SS - seconds (from 00 to 59, sometimes with additional decimals for microseconds).

The full datetime representation in ISO 8601 combines these
two formats with a "T" in between, such as "YYYY-MM-DDTHH:MM:SS".
This separates the date from the time and the format
is easily distinguished from other views.


ISO 8601 also supports the representation of time zones.
For example, a "Z" at the end stands for UTC (Coordinated Universal Time),
and the deviation from UTC can be represented as "+HH:MM" or "-HH:MM".
The term UTC, which stands for Coordinated Universal Time,
is the main time system from which all time zones in the world are regulated.
It is used as the world time standard. It does not change with the seasons
and is not subject to daylight saving time, unlike many local time zones."""

# A datetime object can easily be converted
# to an ISO 8601 format string using the isoformat() method:

print("~" * 30)
iso_format = current_datetime.isoformat()
print(f"iso_format - {iso_format}")  # for example, 2023-12-14T15:43:42.651309
print("~" * 30)

# For reverse conversion of a string in ISO 8601 format
# to a datetime object, you can use the fromisoformat() method:


iso_date_string = "2023-03-14T12:39:29.992996"

date_from_iso = datetime.fromisoformat(iso_date_string)
print(f"date_from_iso - {date_from_iso}")  # for example, 2023-03-14 12:39:29.992996
print("~" * 30)

"""The isoweekday() method on a datetime object is used to get
the day of the week according to ISO 8601. According to this standard,
the week starts with Monday, which has a value of 1,
and ends with Sunday, which has a value of 7."""


day_of_week = current_datetime.isoweekday()

print(
    f"Today: {day_of_week}"
)  # Return a number from 1 to 7 corresponding to the day of the week
print("~" * 30)

"""Useful isocalendar() method, which is used to get a tuple containing the ISO year,
the week number of the year, and the day of the week number according to ISO 8601.

The output of isocalendar() is a tuple (ISO_year, ISO_week, ISO_day_week) where:

ISO_year is the year in ISO format.
ISO_week - number of the week of the year according to ISO 8601 (from 1 to 53).
ISO_day_of_the_week is the day of the week according to ISO 8601,
where 1 means Monday and 7 means Sunday."""


iso_calendar = current_datetime.isocalendar()

print(
    f"ISO year: {iso_calendar[0]}, \
ISO week: {iso_calendar[1]}, \
ISO day of the week: {iso_calendar[2]}"
)
print("~" * 30)

"""Summary
The isoformat() method is used to convert a datetime object to a string in ISO 8601 format.
The fromisoformat() method is used to convert a string in ISO 8601 format to a datetime object.
The isoweekday() method is used to obtain the day of the week according to ISO 8601.
The isocalendar() method is used to get a tuple containing the ISO year, week number of the year,
and day of the week number according to ISO 8601."""

print("dir(datetime)")
print(dir(datetime))
print("~" * 30)
