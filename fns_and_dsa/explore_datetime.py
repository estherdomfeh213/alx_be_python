from datetime import datetime, timedelta

# Part 1: Display the current date and time  
def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date

# Store the current date and time as a string
current_date_str = display_current_datetime()
print(f"Current date and time: {current_date_str}")

# Part 2: Calculate a future date
number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(current_date_str, number_of_days):
    # Convert the string current_date to a datetime object
    current_date = datetime.strptime(current_date_str, "%Y-%m-%d %H:%M:%S")
    
    # Add the timedelta
    future_date = current_date + timedelta(days=number_of_days)
    
    # Return the future date in string format
    return future_date.strftime("%Y-%m-%d %H:%M:%S")

# Calculate and print the future date
future_date_str = calculate_future_date(current_date_str, number_of_days)
print(f"Future date and time: {future_date_str}")
