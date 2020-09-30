
#<-=============Description Starts======================================->
# This is a salary calculator program
# It ask for the user to input shop attendant name and the total value of goods sold that month
# then calculate the commission  as a percentage  four categories of value of goods sold (below 5000, 5000-10000, 10000-20000, and above 20000)
# then gets the  gross salary as a sum of fixed salary and commission
# Tax is calculated as a 5% of the gross salary
# Net salary is Gross salary - tax
# Finally, the program displays the summary of the monthly earning.
#<-=============Description Ends======================================->
# The program has five bugs that needs to be debugged
#   Success to the debugger


#welcome message
print ("WELCOME TO iTECH ELECTRONIC SHOP")
print ("========================================")

#Decliare Variables
commission =float()
value_of_goods_sold=float()
fixed_salary=10000
tax=float()
Gross_salary= float()

#user input
user_name= str(input("Please Enter the shop attendant Name: "))
value_of_goods_sold=float(input("Enter the total Value of goods sold this month: $ "))

# calculating commission based on value of goods sold
if value_of_goods_sold>=20000:
    commission=10/100 * value_of_goods_sold

elif value_of_goods_sold >=10000:
    commission=5/100 * value_of_goods_sold

elif value_of_goods_sold>=5000:
    commission= 3/100 * value_of_goods_sold
else:
    commission= 0

# calculating thr gross salary
Gross_salary= fixed_salary + commission
# calculating tax
tax = 5/100 * Gross_salary
# calculating Net Salary
Net_salary= Gross_salary - tax

#Display the output
print("SUMMARY OF MONTHLY EARNINGS")
print ("===========================================")
print("Shop Attendant Name: Mr./Mrs. ", user_name)
print ("Value of goods sold is: $", value_of_goods_sold)
print("Commission on Value of goods sold:$", commission)
print("Gross Salary:$ " ,Gross_salary)
print(" Tax: $", tax)
print("Net Salary: $", Net_salary)
print (" =========copyright @ iTECH Electronic Shop 2020============= ")