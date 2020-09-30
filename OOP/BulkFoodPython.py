##Input:	Name of item, Price of item, weight in Pounds, weight ounces
##Problem Statement:	Determine the price per ounce a particular item costs
##                      and what the total price is
##Output:	Item Name, Unit price and total cost
##
##
##Variable Name	Datatype
##ItemName	String
##PoundPrice	Float
##WeightPounds	Integer
##WeightOunces	Integer
##UnitPrice	Float
##TotalPrice	Float
##
##
##30,000 foot view
##Get Inputs
##Determine Unit Price
##Determine Total Price
##Display Item Name, Unit Price and Total Price

class BulkFood:
    def __init__(self, NewItemName, NewPrice, NewPounds, NewOunces):
        #Defining attributes
        self.__ItemName = NewItemName
        self.__Price = NewPrice
        self.__WeightPounds = NewPounds
        self.__WeightOunces = NewOunces
        self.__UnitPrice = float()
        self.__TotalCost = float()

    def DetermineUnitPrice(self):
        #Calculate the Unit Price for an item
        self.__UnitPrice = self.__Price/16

    def DetermineTotalCost(self):
        #Calculate the total cost for an item
        self.__TotalCost = self.__Price * (self.__WeightPounds + self.__WeightOunces/16)

    def ReturnItemName(self):
        return self.__ItemName

    def ReturnUnitPrice(self):
        return self.__UnitPrice

    def ReturnTotalCost(self):
        return self.__TotalCost

#End class

def main():
    #declare variables
    MainItemName = str()
    MainPrice = float()
    MainWeightPounds = float()
    MainWeightOunces = float()
    UserContinue = "yes"

    while UserContinue == "yes":
        #Ask user for the name of the item, price, pounds and ounces
        MainItemName = input("Enter the name of your item:  ")
        MainPrice = float(input("Enter the price per pound:  "))
        MainWeightPounds = float(input("Enter the pound weight:  "))
        MainWeightOunces = float(input("Enter the ounces weight:  "))

        #Create the MainBulkFood object off of the Bulk Food class
        MainBulkFood = BulkFood(MainItemName, MainPrice, MainWeightPounds, MainWeightOunces)

        #Calculate the Unit Price
        MainBulkFood.DetermineUnitPrice()

        #Calculate the Total Cost
        MainBulkFood.DetermineTotalCost()

        #Print out the ItemName, UnitPrice and TotalCost
        print("Item:\t\t\t", MainBulkFood.ReturnItemName())
        print("Unit Price:\t\t\t$", format(MainBulkFood.ReturnUnitPrice(), '.2f'))
        print("Total Cost:\t\t\t$", format(MainBulkFood.ReturnTotalCost(), '.2f'))
        print()

        #Ask user if they want to enter another item
        UserContinue = input("Do you want to enter another item, enter yes or no ==>  ")

main()













































    
        
