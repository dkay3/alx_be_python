# multiplication_table.py

def main():
    # Ask the user to enter a number
    number = int(input("Enter a number to see its multiplication table: "))

    # Print the multiplication table using a for loop
    # print(num)
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

if __name__ == "__main__":
    main()
