#This example creates a two-dimensional list that holds quarterly sales figures

#Declare Variables
SalesPerson = 0
Quarter = 0
Sales = 0
#Declares the list with open spots
SalesFigures = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

#Fill the array
for SalesPerson in range(5):
    print("Enter Salesperson ", SalesPerson +1, " sales.")
    for Quarter in range(4):
        Sales = input("Enter the quarterly sales:  ")
        SalesFigures[SalesPerson][Quarter]=Sales

#Print out the sales figures
for SalesPerson in range(5):
    print("==========================================")
    print("Sales figures for Salesperson ", SalesPerson +1)
    print("==========================================")
    for Quarter in range(4):
        print("\t", SalesFigures[SalesPerson][Quarter])
    
