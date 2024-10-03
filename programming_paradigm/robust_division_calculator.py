# Define a function that performs division and handle potential errors 
def safe_divide(numerator, denominator):
  try:
    
    numerator = float(numerator)
    denominator = float(denominator)
    result =  numerator / denominator
    
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."
  
  except ValueError:
    return "Error: Please enter numeric values only."
  
  else:
    return f"The result of the division is {result}"
  
  # finally:
  #   print("Thank you for using our division program")
