from datetime import datetime

# import datetime


current_datetime = datetime.now()

print("Current time with datetime.now() method")
print(f"Year - {current_datetime.year}")
print(f"Month: {current_datetime.month}")
print(f"Day: {current_datetime.day}")
print(f"Hour: {current_datetime.hour}")
print(f"Minute: {current_datetime.minute}")
print(f"Second: {current_datetime.second}")
print(f"Microsecond: {current_datetime.microsecond}")
print(f"Timezone Info: {current_datetime.tzinfo}")
print(f"Date: {current_datetime.date()}")
print(f"Time: {current_datetime.time()}")
print("-" * 30)

# There is a callback method datetime.combine which is used to create
# a new datetime object by combining date and time objects.
# This allows you to create a precise moment by specifying
# the date and time separately and then combining them.

# Basic syntax:
# datetime.datetime.combine(date_object, time_object)

# date_object: A date object that contains year, month, and day information.
# time_object: A time object that contains information about hours,
# minutes, seconds, and microseconds.
# Creation of date and time objects


if isinstance(datetime, object):
    pass
else:
    # import datetime as module
    date_part = datetime.date(2023, 12, 14)  # 2023-12-14
    time_part = datetime.time(12, 30, 15)  # 12:30:15
    print(date_part)
    print(time_part)
    # Combining date and time into one datetime object
    combined_datetime = datetime.combine(date_part, time_part)

    print(f"Combined Datetime: {combined_datetime}")  #  "2023-12-14 12:30:15"


# Create a datetime object with a specific date
specific_date = datetime(year=2020, month=1, day=7)

print(f"Specific Date: {specific_date}")  # "2020-01-07 00:00:00"

# Creation of a datetime object with a specific date and time
specific_datetime = datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)
# specific_datetime = datetime(2020, 1, 7, 14, 30, 15)

print(f"Specific Datetime: {specific_datetime}")  # "2020-01-07 14:30:15"

# The weekday() method is used to get the day of the week number
# for the specified date. It returns the day of the week number,
#  where Monday is 0 and Sunday is 6.


day_of_week = current_datetime.weekday()

# Returns a number from 0 (Monday) to 6 (Sunday)
print(f"Today: {day_of_week}")

# To compare two datetime objects in Python, you can use standard comparison operators
# such as == (equality), != (inequality), < (less than), > (greater than),
# <= (less than or equal to), and > = (greater than or equal to).
# These operators allow you to compare dates and times to determine
# whether one datetime object precedes, follows, or is exactly the same as another.

datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Comparison of dates
print(f"Datetime1 equals Datetime2: {datetime1 == datetime2}")
print(f"Datetime1 not equals Datetime2: {datetime1 != datetime2}")
print(f"Datetime1 is earlier than Datetime2: {datetime1 < datetime2}")
print(f"Datetime1 is later than Datetime2: {datetime1 > datetime2}")

print(dir(datetime))
