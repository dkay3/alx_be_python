# multiplication_table.py

def main():
    # Ask the user to enter a number
    num = int(input("Enter a number: "))

    # Print the multiplication table using a for loop
    print(f"Multiplication Table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

if __name__ == "__main__":
    main()
