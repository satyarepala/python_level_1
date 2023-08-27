import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

# Extract date and time components
current_date = current_datetime.date()
current_time = current_datetime.time()
print("Current Date:", current_date)
print("Current Time:", current_time)

# Create a custom date
custom_date = datetime.date(2023, 8, 15)
print("Custom Date:", custom_date)

# Create a custom time
custom_time = datetime.time(14, 30, 0)
print("Custom Time:", custom_time)

# Format dates and times as strings
formatted_date = current_date.strftime("%Y-%m-%d")
formatted_time = current_time.strftime("%H:%M:%S")
print("Formatted Date:", formatted_date)
print("Formatted Time:", formatted_time)

# Parse date and time from strings
date_str = "2023-08-15"
parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
time_str = "14:30:00"
parsed_time = datetime.datetime.strptime(time_str, "%H:%M:%S").time()
print("Parsed Date:", parsed_date)
print("Parsed Time:", parsed_time)

# Calculate the difference between two dates
date1 = datetime.date(2023, 8, 20)
date2 = datetime.date(2023, 8, 15)
date_difference = date1 - date2
print("Date Difference:", date_difference)

# Perform arithmetic operations on dates
new_date = custom_date + datetime.timedelta(days=7)
print("New Date (One Week Later):", new_date)

# Perform arithmetic operations on times
current_datetime = datetime.datetime.now()
new_time = current_datetime + datetime.timedelta(hours=3, minutes=45)
print("New Time (3 hours 45 minutes later):", new_time.time())
