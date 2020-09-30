
print ("WELCOME TO iTECH ELECTRONIC SHOP")
print ("========================================")
# user input
user_name = str(input("Please Enter the shop attendant Name: "))
value_of_goods_sold = float(input("Enter the total Value of goods sold this month: $ "))

def commission(value_of_goods_sold):
# calculating commission based on value of goods sold
    if value_of_goods_sold>=20000:
        commission=10/100 * value_of_goods_sold

    elif value_of_goods_sold >=10000:
        commission=5/100 * value_of_goods_sold

    elif value_of_goods_sold>=5000:
        commission= 3/100 * value_of_goods_sold
    else:
        commission= 0

def salaryCulculator():
    Gross_salary= fixed_salary + commission
    # calculating tax
    tax = 5/100 * Gross_salary
    # calculating Net Salary
    Net_salary= Gross_salary - tax

#Display the output
def summary():
    print("SUMMARY OF MONTHLY EARNINGS")
    print ("===========================================")
    print("Shop Attendant Name: Mr./Mrs. ", user_name)
    print ("Value of goods sold is: $", value_of_goods_sold)
    print("Commission on Value of goods sold:$", commission)
    print("Gross Salary:$ " ,Gross_salary)
    print(" Tax: $", tax)
    print("Net Salary: $", Net_salary)
    print (" =========copyright @ iTECH Electronic Shop 2020============= ")

def main():
    #Decliare Variables
    commission = float()
    value_of_goods_sold = float()
    fixed_salary = 10000
    tax = float()
    Gross_salary = float()


main()