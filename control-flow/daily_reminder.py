def main():
    # Ask the user for task details
    task = input("Enter your task: ")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Validate time_bound input
    while time_bound not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        time_bound = input("Is it time-bound? (yes/no): ").lower()

    priority = input("Priority (high/medium/low): ").lower()

    # Validate priority input
    while priority not in ['high', 'medium', 'low']:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
        priority = input("Priority (high/medium/low): ").lower()

    # Provide a customized reminder based on inputs
    match priority:
        case 'high':
            reminder = f"Reminder: '{task}' is a high priority task."
        case 'medium':
            reminder = f"Reminder: '{task}' is a medium priority task."
        case 'low':
            reminder = f"Note: '{task}' is a low priority task."

    # Modify reminder based on time-bound status
    if time_bound == 'yes':
        reminder += " This task is  a high priority task that requires immediate attention today!"
    else:
        reminder += "  Consider completing it when you have free time."

    print(reminder)

if __name__ == "__main__":
    main()
