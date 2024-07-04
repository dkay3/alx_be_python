# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    Formula: C = (F - 32) * (5/9)
    """
    
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Formula: F = C * (9/5) + 32
    """
   
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
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
        fahrenheit = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit:.2f}°F")
    elif scale == 'F':
        # Convert Fahrenheit to Celsius
        celsius = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is {celsius:.2f}°C")
    else:
        print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
