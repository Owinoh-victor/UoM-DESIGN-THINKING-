# Variables
inflated_price = float()
price = float()
years = int()
# Setting the inflation rate
inflation = 0.0229
# Getting inputs
price = float(input("Enter price: "))
years = int(input("Enter years: "))

# Your code goes here
for years in range(0,years + 1):
    inflated_price= (price * inflation) + inflated_price



# Print out the inflated price
print(inflated_price)