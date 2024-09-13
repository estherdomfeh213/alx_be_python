# A  program for personal finance calculator 
# user input for monthly income
monthly_income = int(input("Enter your monthly income: "))
#user input for total monthly expenses
monthly_expenses = int(input("Enter your total monthly expenses: "))

#calculate monthly savings 
monthly_savings = (monthly_income - monthly_expenses)

#(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
#project annual saving using the formula above
projectedSavings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are $" + str(monthly_savings))

print("Projected savings after one year, with interest, is: $" + str(projectedSavings))