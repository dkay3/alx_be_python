
# Define global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
FAHRENHEIT_OFFSET = 32


def FAHRENHEIT_TO_CELSIUS_FACTOR(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    Formula: C = (F - 32) * (5/9)
    """
    celsius = (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def CELSIUS_TO_FAHRENHEIT_FACTOR(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Formula: F = C * (9/5) + 32
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET
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
        fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR(temperature)
        print(f"{temperature}°C is {fahrenheit:.2f}°F")
    elif scale == 'F':
        # Convert Fahrenheit to Celsius
        celsius = FAHRENHEIT_TO_CELSIUS_FACTOR(temperature)
        print(f"{temperature}°F is {celsius:.2f}°C")
    else:
        print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
