"""
Problem
Create a program that will ask the user for number of chicken wings or wings they want to order at a restaurant.
The number of wings and the sauce will determine if there is a discount on the total wings purchased. For hot wings purchased in
a quantity of 6 or less there is no discount. Therefore the discount rate is 0.0. For hot wings and a quantity of more
than 6 but less than or equal to 12, there is a 10% discount. For hot wings purchased in the amount of greater than 12
 but less than 24 the discount is 20%. For sweet and sour wings, purchased with a quantity of 6 or less the discount is 5%.
  For sweet and sour wings and a quantity of greater than 6 but less than or equal to 12, the discount is 10%.
  For sweet and sour wings purchased with a quantity greater than 12 but less than or equal to 24, the discount is 15%.
  For all wing purchases greater than 24 wings, the discount is 25%. All wings are 50 cents each.
The program needs to ask the user for the type of wing either hot or sweet with the following prompt.
There are no spaces after the word Type:
Type:
The program also needs to ask for the quantity of wings using the following prompt. There are no spaces after the word Quantity:
Quantity:
The program needs to determine the total cost of the wings and print that out with the following prompt.
 There are no spaces after the word Total:
Total:
Finally the program needs to ask the user if they want to purchase another order of wings using the following prompt.
There are no spaces after the word Continue: The program will stop when the user enters Q to quit.
Continue:
Given that the user enters sour and 20 and also Q to end the program, your screen should read:
Type:sour
Quantity:20
Total: 8.5
Continue:Q
"""
#Declare Variables

type= str()
quantity= int()
price= 0.50
total= float()
leave= str()
# User Inputs
while leave !="Q":
    type = str(input("Type:"))
    quantity = int(input("Quantity:"))
    if type == "hot":
        if quantity <= 6:
            discount = 0
        elif quantity <= 12:
            discount = 10/100
        elif quantity < 24:
            discount = 20/100
        else:
            discount = 25 / 100
    else:
        if quantity <= 6:
            discount = 5/100
        elif quantity <= 12:
            discount = 10/100
        elif quantity <= 24:
            discount = 15/100
        else:
            discount = 25/100
# calculations
    item_price = price * quantity
    discounted= item_price * discount
    total= item_price - discounted
# Output
    print("********************order summary**************")
    print("Type:", type)
    print("Quantity:", quantity)
    print("Total:",   total)
    leave= str(input("Continue:"))






