from datetime import datetime, timedelta


# Part 1: Display the current date and time  
def display_current_datetime(): 
  global current_date
  current_date = datetime.now()
  return current_date


# Store the current date 
print(f"Current date and time: {display_current_datetime()}")


# Part  : Calculate a future date 
number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
  future_date = current_date + timedelta(days=number_of_days)
  return f"Future date: {future_date}"


print(calculate_future_date())
