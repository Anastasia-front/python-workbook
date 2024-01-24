from datetime import datetime, timedelta, timezone

# To display the date in UTC format, you can do this by
# adding information about the time zone to the datetime object:

local_now = datetime.now()
utc_now = datetime.now(timezone.utc)

print("~" * 30)
print(f"local_now - {local_now}")  # 2023-12-14 16:39:33.883454
print(f"utc_now - {utc_now}")  # 2023-12-14 14:39:33.883454+00:00
print("~" * 30)

""" To convert a time from UTC to another time zone, you need to 
define a timezone object with the appropriate offset. For example, 
to convert a UTC time to a time corresponding to US Eastern Time Zone 
(UTC-5 hours), you can do the following:"""


utc_time = datetime.now(timezone.utc)

# Create time zone for Eastern Time Zone (UTC-5)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Converts UTC time to Eastern Time Zone time
print(f"eastern_time - {eastern_time}")  # 2023-12-14 09:43:06.778253-05:00
print("~" * 30)

"""To convert local time to UTC time, you must first assign
local time the corresponding time zone, and then use the 
astimezone() method to convert it to UTC:"""

# Suppose the local time belongs to the UTC+2 time zone
local_timezone = timezone(timedelta(hours=2))
local_time = datetime(
    year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone
)

# Convert local time to UTC
utc_time = local_time.astimezone(timezone.utc)
print(f"utc_time - {utc_time}")  # 2023-03-14 10:30:00+00:00
print("~" * 30)

# In this example, we created a datetime object
# with time zone UTC+2 (Kyiv) and converted it to UTC time.


"""The ISO 8601 standard also supports time zones. 
In Python, this can be done by adding timezone 
information to the datetime object:"""


# Time in a specific time zone
timezone_offset = timezone(timedelta(hours=2))  # For example, UTC+2
timezone_datetime = datetime(
    year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset
)

# Conversion to ISO 8601 format
iso_format_with_timezone = timezone_datetime.isoformat()
print(
    f"iso_format_with_timezone - {iso_format_with_timezone}"
)  # 2023-03-14T12:30:00+02:00
print("~" * 30)

"""These methods in the datetime module make working
with the ISO format simple and efficient, 
allowing you to easily integrate a standardized 
representation of dates and times into Python programs."""


# Key Aspects: Methods for Working with Time Zones in Python

"""
So, we considered the following methods 
and principles of working with them:

Adding time zone information to a datetime object:
The astimezone method is used to convert a datetime object from 
one time zone to another. For example, it can be used 
to convert time from UTC to other time zones.


Convert local time to UTC time:
First, we assign the appropriate time zone to the local time.
We use astimezone to convert to UTC. This approach helps 
to conveniently work with local and world time.


Formatting in ISO 8601 format with time zone:
We use isoformat to get a string from a datetime object 
in ISO 8601 format with a time zone. 
This is useful for representing the date and time 
in a single, standardized way."""

print("dir(timezone)")
print(dir(timezone))
print("~" * 30)
