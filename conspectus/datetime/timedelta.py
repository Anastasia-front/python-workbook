from datetime import datetime, timedelta

current_datetime = datetime.now()

# A timedelta object can be created specifying
# weeks, days, hours, minutes, seconds, milliseconds,
# and microseconds by passing one or more of the following parameters:
# days, seconds, microseconds, milliseconds, minutes, hours, weeks.
# If any parameter is not specified, it is equal to 0 by default.
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2,
)
print(f"Timedelta: {delta}")  # 64 days, 8:05:56.000010

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(f"Difference: {difference}")  # 365 days, 0:00:00
print(f"Total Seconds in Difference: {difference.total_seconds()}")  # 31536000.0

#  Timedelta objects can be created to get a date/time that is far from the original
future_date = current_datetime + timedelta(days=10)  # Add 10 days to the current date
print(f"Future_date - {future_date}")  # 2023-12-28 14:08:46.342976

# Or from some specific date
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(
    f"Seventh_day_2020 + four_weeks_interval : {seventh_day_2020 + four_weeks_interval}"
)  # 2020-02-04 14:00:00
print(
    f"Seventh_day_2020 - four_weeks_interval : {seventh_day_2020 - four_weeks_interval}"
)  # 2019-12-10 14:00:00

# But if you need to do calculations or comparisons based on
# a sequence of dates, for example to determine the number
# of days between two dates.

# We can use the toordinal() method, which returns the
# ordinal number of the day, taking into account the number
# of days since January 1 of the year 1 AD (that is, since
# the beginning of the Christian calendar).
# This method converts a datetime object to an integer
# representing the sequence number of the given day.

date = datetime(year=2023, month=12, day=18)

# Obtaining the serial number
ordinal_number = date.toordinal()
print(
    f"Ordinal number of {date} is {ordinal_number}"
)  # The serial number of the date 2023-12-18 00:00:00 is 738872


print(dir(timedelta))
