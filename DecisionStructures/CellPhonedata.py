#Declare variables
used_data = float()
flat_rate = float()
data_bank = float()
data_diff = float()
overage = float()
total_cost = float()

#Get flat rate, data bank and used data from user
flat_rate = float(input("Enter the amount of money you pay each month for your cell phone bill:  "))
data_bank = float(input("Enter the amount of data in GB that you have to use each month:  "))
used_date = float(input("Enter the amount of data you used this month:  "))

#calculate the difference
data_diff = data_bank - used_data

if data_diff >= 0:
    total_cost = flat_rate
    print("Here we are")
else:
    data_diff -(data_diff)
    print("Here we go")
    
