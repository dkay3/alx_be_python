# pattern_drawing.py

def main():
    # Ask the user to enter a positive integer
    size = int(input("Enter the size of the pattern: "))

    # Check if size is positive
    if size <= 0:
        print("Please enter a positive integer.")
        return
    
    # Print the square pattern using nested loops
    print(f"Square pattern of size {size}:")
    for i in range(size):
        for j in range(size):
            print("* ", end="")
        print()  # Move to the next line after each row

if __name__ == "__main__":
    main()
