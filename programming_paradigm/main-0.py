# main-0.py

import sys
from bank_account import BankAccount

def print_usage():
    print("Usage:")
    print("  main-0.py deposit <amount>")
    print("  main-0.py withdraw <amount>")
    print("  main-0.py display")

def main():
    account = BankAccount()

    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    command = sys.argv[1]

    if command == "deposit":
        if len(sys.argv) != 3:
            print_usage()
            sys.exit(1)
        
        try:
            amount = float(sys.argv[2])
        except ValueError:
            print("Please provide a valid amount.")
            sys.exit(1)
        
        if account.deposit(amount):
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Failed to deposit.")
    
    elif command == "withdraw":
        if len(sys.argv) != 3:
            print_usage()
            sys.exit(1)
        
        try:
            amount = float(sys.argv[2])
        except ValueError:
            print("Please provide a valid amount.")
            sys.exit(1)
        
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Failed to withdraw.")
    
    elif command == "display":
        account.display_balance()
    
    else:
        print_usage()
        sys.exit(1)

if __name__ == "__main__":
    main()
