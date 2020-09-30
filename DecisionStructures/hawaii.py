#Problem Statement:  Create a program that will determine the price for a trip
#to Hawaii

#inputs:  room choice, number of nights, package choice
#outputs:  room cost, package cost, subtotal, tax and total

#30,000 foot view
#********************************
#1).  Ask the user for the number of days, room choice & package choice
#2).  Determine the room cost and package cost
#3).  Determine subtotal, tax and total
#4).  Output room cost, package cost, subtotal, tax and total

#Declare Variables
roomchoice = str()
packagechoice= str()
numnights = int()
roomcost = float()
packagecost = float()
subtotal = float()
tax = float()
total = float()
#Declare taxrate as a constant
taxrate = 0.15

#1).  Ask the user for the number of days, room choice & package choice
numnights = int(input("How many nights will you be staying:  "))
roomchoice = input("Enter D for double or S for suite:  ")
packagechoice = input("Enter B for Breakfast, S for Sports, M for all Meals and E for Everything:  ")

#2).  Determine the room cost and package cost
if roomchoice == "D":
    roomcost = 150
else:
    roomcost = 185
#end if

if packagechoice == "B" or packagecost == "M":
    packagecost = 50
elif packagechoice == "S":
    packagecost = 75
elif packagechoice == "M":
    packagecost = 100
else:
    packagecost = 175
#end if

#3).  Determine subtotal, tax and total
subtotal = (numnights * roomcost) + packagecost
tax = subtotal * taxrate
total = subtotal + tax
    
#4).  Output room cost, package cost, subtotal, tax and total
print("**************************************")
print("Room Cost:\t$", roomcost)
print("Package Cost:\t$", packagecost)
print("Subtotal:\t$", subtotal)
print("Tax:\t\t$", format(tax, ',.2f'))
print("Total:\t\t$", format(total, ',.2f'))











    
    













