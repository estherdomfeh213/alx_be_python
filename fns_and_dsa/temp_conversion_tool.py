FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 


def convert_to_celsius(fahrenheit):
  global FAHRENHEIT_TO_CELSIUS_FACTOR
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
  global CELSIUS_TO_FAHRENHEIT_FACTOR
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# Prompt the user to enter a temperature 
temperature = float(input("Enter the temperature to convert: "))


# Ask if F or C 
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
 
if unit == "F":
  converted_temperature = convert_to_celsius(temperature)
  print(f"{temperature}°F is {converted_temperature}°C")
elif unit == "C":
  converted_temperature = convert_to_fahrenheit(temperature)
  print(f"{temperature}°C is {converted_temperature}°F")
else:
  print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")