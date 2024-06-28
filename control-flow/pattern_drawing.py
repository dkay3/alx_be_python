# pattern_drawing.py

def main():
    # Ask the user to enter a positive integer
    size = int(input("Enter the size of the pattern: "))

    # Check if size is positive
    if size <= 0:
        print("Please enter a positive integer.")
        return
    
    # Print the square pattern using a while loop and nested for loop
    # print(f"Square pattern of size {size}:")
    i = 0
    while i < size:
        j = 0
        while j < size:
            print("*", end=" ")
            j += 1
        print()  # Move to the next line after completing the row
        i += 1

if __name__ == "__main__":
    main()
