# temp_conversion_tool.py

# Define global conversion factors
global FAHRENHEIT_TO_CELSIUS_FACTOR
global CELSIUS_TO_FAHRENHEIT_FACTOR
global FAHRENHEIT_OFFSET

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    Formula: C = (F - 32) * (5/9)
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FAHRENHEIT_OFFSET
    celsius = (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Formula: F = C * (9/5) + 32
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR, FAHRENHEIT_OFFSET
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FAHRENHEIT_OFFSET
    return fahrenheit

def main():
    # Prompt the user to enter a temperature
    try:
        temperature = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    # Prompt the user to specify the scale (Celsius or Fahrenheit)
    scale = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if scale == 'C':
        # Convert Celsius to Fahrenheit
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit:.2f}°F")
    elif scale == 'F':
        # Convert Fahrenheit to Celsius
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius:.2f}°C")
    else:
        print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
