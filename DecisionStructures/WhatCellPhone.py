##Write a program to help a user to decide what phone they want to purchase.
##The program will ask the user for the type of phone, i.e. operating system
##and then how much money they wish to spend.  The program will print out the
##phone selection and type.
##
##inputs:  How much money, operating system
##problem statement:  Help the user pick a phone.
##outputs:  choice of phone and options
##
##Variables
##----------------------------------
##phoneType	string
##money		float
##options	string
##
##30,000 foot view
##----------------------------------
##1.  Get amount of money and OS from user
##2.  Determine phone type and options
##3.  Output phone type and options to the user
##

##Declare variables
phoneType = str()
money = float()
option = str()

##1.  Get amount of money and OS from user
phoneType = input("Enter the type of phone you want, either iPhone or Droid:  ")
money = float(input("Enter in the amount of money you wish to spend:  $"))

##2.  Determine phone type and options
if phoneType == "iPhone":
    if money >= 399:
        option = "iPhone 5, 64GB"
    elif money >= 299:
        option = "iPhone 5, 32 GB"
    elif money >= 199:
        option = "iPhone 5, 16 GB"
    else:
        option = "No Phone, not enough money"
else:
    if money >= 299:
        option = "Samsung Galaxy Note II"
    elif money >= 140:
        option = "Samsung Galaxy S4"
    elif money >= 100:
        option = "Samsung Galaxy S3"
    else:
        option = "No phone, not enough money"
#End if

print(option)
print(money)


##3.  Output phone type and options to the user
print ("You selected:  ", phoneType)
print ("With the following option:  ", option)       
              









              


