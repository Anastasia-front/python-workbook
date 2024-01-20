from datetime import datetime

current_datetime = datetime.now()

"""Timestamp is used to indicate a specific moment in time.
This is usually represented as the number of seconds
(or milliseconds/microseconds in some systems) since
some starting date, most commonly since
January 1, 1970 UTC, which is the Greenwich Mean Time.

In Python, you can convert a datetime object to a timestamp and vice versa."""

# Datetime to timestamp conversion
timestamp = datetime.timestamp(current_datetime)
print(f"timestamp - {timestamp}")

# Conversion of a timestamp into a datetime object
timestamp = 1617183600

dt_object = datetime.fromtimestamp(timestamp)
print(f"dt_object - {dt_object}")

print(dir(datetime))
