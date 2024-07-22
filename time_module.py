import time
import datetime
import os

# Get the current time in seconds since the epoch
seconds = time.time()
print("Current time in seconds since the epoch:", seconds)

# Convert the time in seconds to a datetime object
print("Datetime object from seconds:", datetime.datetime.fromtimestamp(seconds))

# Get the local time as a string
local_time = time.ctime(seconds)
print("Local time:", local_time)

# Get the current time in UTC
print("Current UTC time:", time.gmtime())

# Get the current local time as a tuple
tuple1 = time.localtime()
print("Current local time as a tuple:", tuple1)

# Get the current local time as a formatted string
time_str = time.strftime('%Y-%m-%d, %H:%M:%S')
print("Formatted local time:", time_str)

# Sample print statements with time delays
print('This is sample line 1')
print('This is sample line 2')
time.sleep(2)  # Pause for 2 seconds
print('This is sample line 3')
time.sleep(10)  # Pause for 10 seconds
print('This is sample line 4')

# Prompt the user to enter a file name to search for
find_file = input('Please enter your file name: ')

# Search for the file in the current directory and its subdirectories
file_found = False
for root, dirs, files in os.walk('.'):  # Use '.' to start from the current directory
    if find_file in files:
        print("Yes, your file found in:", os.path.join(root, find_file))
        file_found = True
        break

if not file_found:
    print('Your file not found')