#Familly Coffee Store 

#welcome message
print ("Welcome to Family Store")
print ("=======================")
print ("In our store we sale different kinds of products but we are known by our coffee. We export our coffee from three different countries which are Brazil, colombia, and turkey. The prices are different as the taxes are different. This program is made to calculate the amount of money of each brand of coffee and determine the tax amount of it")

#Decliare Variables
brand = ""
quantity = 0.00
brazil = 4.99
colombia = 5.49
turkey = 4.49
totall = 0.00
totalwithtax = 0.00

brand = input (print ("Enter the brabd of coffee imported. B for Brazil, C for colombia, T for turkey  (ALL CAPITAL LETTER)"))
quantity = input (print ("Enter how many pounds the store is importing this time  "))
if brand == "B":
    total = brazil * float(quantity)
    totalwithtax = total + (total*0.1)
    print ("Your total cost without taxes is:  $", total)
    print ("Your Total Cost With The Taxes imposed by the State of Brazil (0.1) is:  $", totalwithtax)
elif brand == "C":
    total = colombia * float(quantity)
    totalwithtax = total + (total*0.12)
    print ("Your total cost without taxes is:  $", total)
    print ("Your Total Cost With The Taxes imposed by the State of Colombia (0.12) is:  $", totalwithtax)
elif brand == "T":
    total = turkey * float(quantity)
    totalwithtax = total + (total*0.08)
    print ("Your total cost without taxes is:  $", total)
    print ("Your Total Cost With The Taxes imposed by the State of Turkey (0.08) is:  $", totalwithtax)
print ()
print (" [[ copyright @ Diena Sabieh 2012 :D ]]")
    
