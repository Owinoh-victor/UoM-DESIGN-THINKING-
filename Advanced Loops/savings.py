""""
Problem
Create a program in Python that allows you to save money over a 3 week period for 5 months. The weekly prompt needs to read:
Weekly Savings:
At the end of each month, your program needs to print out the total saved for that month and the total saved for all of
 the months at that point. The prompts should look like the following:
Monthly Savings
Total Savings:
For all input and output prompts, there are no spaces after the colons.
"""
# Variables
weekly_savings = float()
monthly_savings = float()
total_savings = float()

# Outer loop keeping track of number of months
for months in range(0, 5):
    # Inner loop keeps track of weeks
    for weeks in range(0, 3):
        weekly_savings = float(input("Weekly Savings:"))
        monthly_savings = monthly_savings + weekly_savings

    # end loop
    print("Monthly Savings:", monthly_savings)
    total_savings = total_savings + monthly_savings
    print("Total Savings:", total_savings)
    print("************************************************")
    monthly_savings = 0
    # end outer loop
