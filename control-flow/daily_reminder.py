# daily_reminder.py

def main():
    # Ask the user for task details
    task = input("Enter your task: ")
    priority = input("Enter the priority level (low, medium, high): ")
    time_bound = input("Is it time-sensitive? (yes/no): ").lower()

    # Validate time_sensitive input
    while time_bound not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        time_bound = input("Is it time-sensitive? (yes/no): ").lower()

    # Provide a customized reminder based on inputs

    if time_bound == 'yes':
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    else:
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()
