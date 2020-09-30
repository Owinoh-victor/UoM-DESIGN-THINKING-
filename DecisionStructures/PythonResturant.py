##SS Project
##If Structure Python Program
##You are at a resturant and want to know the price
##of your food order before and after taxes
##This program will give a menu of food options
##then print the total cost of the food after taxes
##it will also display the tax on your order


##VARIBLES

choice = int()
price = float()
total = float()
tax = float()


##MENU

print("Plese Select A Number...")
print("-------------------------------------")
print()
print(" 1. Hamburger ....  $9.99")
print(" 2. Cobb Salad ...  $5.99")
print(" 3. Steak ........  $12.99")
print(" 4. BBQ Wings ....  $11.99")
print(" 5. Club Sammy ...  $8.99")
print(" 6. Fries ........  $5.99")
print(" 7. END PROGRAM ")
print()
print("------------------------------------")
print("Select as many items as you please")

##IF STRUCTURE AND LOOP


while choice != 7:
    
    choice = int(input("please select an item: "))

    price = 0

    if (choice == 1):
        price = 9.99
        print("COST: ",price)
    elif (choice == 2):
        price = 5.99
        print("COST: ",price)
    elif (choice == 3):
        price = 12.99
        print("COST: ",price)
    elif (choice == 4):
        price = 11.99
        print("COST: ",price)
    elif (choice == 5):
        price = 8.99
        print("COST: ",price)
    elif (choice == 6):
        price = 5.99
        print("COST: ",price)
    elif (choice > 7) or (choice < 0):
        print("OPTION NOT FOUND")

    total = total + price

##TAXES

tax = total *.06
total = total + tax

##END SCREEN

print()
print("----------------------------")
print("your tax total was ",format(tax, ',.2f'))
print("TOTAL COST: ",format(total, ',.2f'))




        
