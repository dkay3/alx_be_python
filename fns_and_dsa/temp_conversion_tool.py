# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_OFFSET = 32

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Formula: F = C * (9/5) + 32
    """
    global FAHRENHEIT_OFFSET
    fahrenheit = celsius * (9 / 5) + FAHRENHEIT_OFFSET
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    Formula: C = (F - 32) * (5/9)
    """
    global FAHRENHEIT_OFFSET
    celsius = (fahrenheit - FAHRENHEIT_OFFSET) * (5 / 9)
    return celsius

def main():
    # Prompt the user to choose a conversion direction
    choice = input("Choose conversion type:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter 1 or 2: ")
    
    if choice == '1':
        # Celsius to Fahrenheit conversion
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is {fahrenheit:.2f}°F")
    elif choice == '2':
        # Fahrenheit to Celsius conversion
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius:.2f}°C")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
