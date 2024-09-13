# A  program for personal finance calculator 
# user input for monthly income
userMonthlyIncome = float(input("Enter your monthly income: "))
#user input for total monthly expenses
userTotalExpenses = float(input("Enter your total monthly expenses: "))

#calculate monthly savings 
monthlySavings = userMonthlyIncome - userTotalExpenses

#(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
#project annual saving using the formula above
projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)

print("Your monthly savings are $" + str(monthlySavings))

print("Projected savings after one year, with interest, is: $" + str(projectedSavings))