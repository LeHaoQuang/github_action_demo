import datetime

# Get the current system time
current_time = datetime.datetime.now()

# Format the time
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Print the current system time
print("Current system time:", formatted_time)
