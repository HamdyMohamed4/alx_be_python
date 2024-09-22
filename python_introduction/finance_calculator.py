# Prompt the user for their financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with a simple interest rate of 5%
annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Print the projected savings after one year
print(f"Your projected savings after one year is: {annual_savings:.2f}")
