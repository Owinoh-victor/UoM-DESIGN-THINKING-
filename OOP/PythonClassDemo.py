#Program to calculate sales commission
#Declare Variables
SalesAmount = 0.00
CommissionEarned = 0.00
CommissionRate = 0.00

#Ask the user for their Monthly Sales
SalesAmount = float(input("Enter your sales amount for this month:  "))

#Determine the commision
if SalesAmount <= 3000:
    CommissionRate = 0.03
elif SalesAmount > 3000 and SalesAmount <= 5000:
    CommissionRate = 0.05
elif SalesAmount > 5000 and SalesAmount <=10000:
    CommissionRate = 0.08
else:
    CommissionRate = 0.10

#Determine Commission Earned
CommissionEarned = SalesAmount * CommissionRate

#Output Commission
print("Your total Sales for this month was:  $", SalesAmount)
print("Your Commission Rate is:  ", CommissionRate)
print("Your Earned Commission is:  $", CommissionEarned)




