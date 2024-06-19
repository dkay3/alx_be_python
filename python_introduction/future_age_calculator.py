current_year = 2023

# Prompt the user for their current age
try:
  current_age = int(input("How old are you? "))
except ValueError:
  print("Please enter a valid integer for your age.")
  exit()

# Calculate age in the target year (2050)
age_in_2050 = current_age + (2050 - current_year)

# Print the result in a formatted way
print(f"In {2050}, you will be {age_in_2050} years old.")