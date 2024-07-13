# main.py

import sys
from robust_division_calculator import safe_divide

def print_usage():
    print("Usage:")
    print("  main.py <numerator> <denominator>")

def main():
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)
    
    try:
        dividend = float(sys.argv[1])
        divisor = float(sys.argv[2])
    except ValueError:
        print("Error: Please provide valid numbers.")
        sys.exit(1)
    
    result = safe_divide(dividend, divisor)
    print(f"The result of the division is {result}")

if __name__ == "__main__":
    main()


