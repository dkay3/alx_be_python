# explore_datetime.py

import datetime

def display_current_datetime():
    # Save the current date and time
    current_datetime = datetime.datetime.now()
    # Save the current date
    current_date = current_datetime.date()
    
    # Format and print the current date and time
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    
    return current_date

def calculate_future_date(current_date, days_to_add):
    # Calculate the future date
    future_date = current_date + datetime.timedelta(days=days_to_add)
    
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date after adding {days_to_add} days: {formatted_future_date}")

def main():
    # Display the current date and time
    current_date = display_current_datetime()
    
    # Prompt the user to enter a number of days
    days_to_add = int(input("Enter the number of days to add: "))
    
    # Calculate and display the future date
    calculate_future_date(current_date, days_to_add)

if __name__ == "__main__":
    main()
