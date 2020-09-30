
#declare variables
flavor = str()
scoops_sold= int()
total_sales = float()

#constant variables
price_per_scoop= 2.5
total_scoops= 96

#ask user for Input
flavor = str(input("Enter the ice cream flavor:  "))
scoops_sold = int(input("Enter the number of scoops sold: "))

#Determine total sales and stock balance
total_sales= price_per_scoop * scoops_sold
scoops_left= total_scoops - scoops_sold

 #Display output
print("Ice Cream Flavor:  " , flavor)
print("Total Sales: $ " , total_sales)
print("Number of scoops left: " , scoops_left)
