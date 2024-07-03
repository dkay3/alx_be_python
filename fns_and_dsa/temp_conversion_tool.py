# temp_conversion_tool.py

# Define global variables for conversion factors
CELSIUS_TO_FAHRENHEIT = 9 / 5
FAHRENHEIT_TO_CELSIUS = 5 / 9


def celsius_to_fahrenheit(celsius):
  """Converts a temperature in Celsius to Fahrenheit.

  Args:
      celsius: The temperature in degrees Celsius.

  Returns:
      The temperature converted to degrees Fahrenheit.
  """
  return celsius * CELSIUS_TO_FAHRENHEIT + 32


def fahrenheit_to_celsius(fahrenheit):
  """Converts a temperature in Fahrenheit to Celsius.

  Args:
      fahrenheit: The temperature in degrees Fahrenheit.

  Returns:
      The temperature converted to degrees Celsius.
  """
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS


# Example usage
temperature = float(input("Enter temperature: "))
scale = input("Enter scale (C or F): ").upper()

if scale == "C":
  converted_temp = celsius_to_fahrenheit(temperature)
  print(f"{temperature}°C is equivalent to {converted_temp:.2f}°F")
elif scale == "F":
  converted_temp = fahrenheit_to_celsius(temperature)
  print(f"{temperature}°F is equivalent to {converted_temp:.2f}°C")
else:
  print("Invalid scale. Please enter 'C' or 'F'.")
