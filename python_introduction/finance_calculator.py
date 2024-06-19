# Prompt the user for monthly income and expenses
try:
  monthly_income = float(input("Enter your monthly income: "))
  monthly_expenses = float(input("Enter your total monthly expenses: "))
except ValueError:
  print("Please enter valid numbers for your income and expenses.")
  exit()

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Assume annual interest rate of 5%
annual_interest_rate = 0.05

# Calculate projected annual savings with interest
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Print the results in a formatted way
print(f"Your monthly savings are: ${monthly_savings}")
print(f"Projected annual savings with interest: ${projected_annual_savings}")
