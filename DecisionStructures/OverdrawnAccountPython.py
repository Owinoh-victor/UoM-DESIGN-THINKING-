#Written by:  Betsy Jenaway
#Date:  9/10/2013
##
##Develop a program to help us determine the cost when we overdraw our account.
##The user will enter in their balance and the amount of the check.
##If the check is bigger than the balance the account is considered overdrawn.
##If the overdrawn amount is greater than $25 the fee is $10.  If the overdrawn
##amount is greater than $50 the fee is $25.  If the overdrawn amount is greater
##than $100 the fee is $40.
##
##inputs: check, balance
##Problem Statement:  Trying to figure out if there will be an overdraft fee
##Outputs: balance, check, fee
##
##Variables
##--------------------
##check		float
##balance	float
##fee		float
##overdrawn	float
##
##

#Declare Variables
check = float()
balance = float()
fee = float()
overdrawn = float()


##1. Ask the user for the amount of the check and the balance
balance = float(input("Enter in your balance:  $"))
check = float(input("Enter the amount of your check:  $"))

##2. Determine if there is a fee and if there is a fee the amount
if check > balance:
    overdrawn = check - balance
    if overdrawn >= 100:
        fee = 40
    elif overdrawn >= 50:
        fee = 25
    elif overdrawn >= 25
        fee = 10
    else:
        fee = 5
    #end if
    print("Sorry you have an overdraft fee of:  $", fee)
else:
    fee = 0
    print("You have not overdrawn your account!")
#end if

##3. Print out the balance, check and fee to the user
print()
print("Your balance:      $", balance)
print("Your check:        $", check)
print()
print("Overdrawn amount:  $", overdrawn)
print("Fee:               $", fee)






























