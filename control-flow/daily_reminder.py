# daily_reminder.py

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
    match time_bound, priority:
        case ('yes', 'high'):
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        case ('yes', 'medium'):
            print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
        case ('yes', 'low'):
            print(f"Reminder: '{task}' is a low priority task. Consider completing it today if possible.")
        case ('no', 'high'):
            print(f"Note: '{task}' is a high priority task. Consider completing it soon.")
        case ('no', 'medium'):
            print(f"Note: '{task}' is a medium priority task. Consider completing it when you have some free time.")
        case ('no', 'low'):
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have ample free time.")

if __name__ == "__main__":
    main()
