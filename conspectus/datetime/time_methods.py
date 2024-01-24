# Key Aspects: Basic methods of the time module in Python


"""
time.time(): Returns the current time in seconds since January 1, 1970 (epoch time).
time.sleep(seconds): Stops program execution for the specified number of seconds.
time.ctime([seconds]): Converts a timestamp to a human-readable text representation.
time.localtime([seconds]): Converts a timestamp to a struct_time in the local time zone.
time.gmtime([seconds]): Similar to localtime, but returns struct_time in UTC format.
time.perf_counter(): Returns a high-precision counter for measuring short time intervals."""

import time

print("~" * 30)
current_time = time.time()
print(f"current_time: {current_time}")
print("~" * 30)

print(f"Start of pause - {time.time()}")
time.sleep(2)
print(f"End of pause - {time.time()}")
print("~" * 30)

readable_time = time.ctime(current_time)
print(f"readable_time: {readable_time}")
print("~" * 30)

local_time = time.localtime(current_time)
print(f"local_time: {local_time}")
print("~" * 30)

"""The time.struct_time object in Python is a named tuple 
used to represent time. Each element of the tuple 
has a special value that represents a specific
component of the date and time:

tm_year - year
tm_mon - month from 1 to 12
tm_mday - day of the month from 1 to 31
tm_hour - hours from 0 to 23
tm_min - minutes from 0 to 59
tm_sec - seconds from 0 to 59
tm_wday - day of the week from 0 to 6
tm_yday - day of the year from 1 to 366
tm_isdst - summer time flag. 0 means that summer time is not valid, -1 - no information, 1 - summer time is valid


The time.gmtime([seconds]) method is similar to localtime, 
but returns a struct_time in UTC.


Quite important is the time.perf_counter() method, 
which provides access to a high-precision counter 
and is ideal for measuring short time intervals."""

# We record the time at the beginning of execution
start_time = time.perf_counter()

# We perform some operation
for _ in range(1_000):
    pass  # Just loops a million times

# We record the time after the operation
end_time = time.perf_counter()

# We calculate and display the execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
print("~" * 30)

print("dir(time)")
print(dir(time))
print("~" * 30)
