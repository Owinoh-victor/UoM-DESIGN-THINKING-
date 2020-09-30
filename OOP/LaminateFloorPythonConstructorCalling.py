#This program will calculate the area needed, including waste, and rate
#necessary to install a laminate floor

#Written By:  Betsy Jenaway

class LaminateFloor:
    def __init__(self, NewLength, NewWidth, NewPrice):
        self.__length = NewLength
        self.__width = NewWidth
        self.__price = NewPrice
        self.__area = float()
        self.__waste = float()
        self.__rate = float()
        self.__totalsqfoot = float()
        self.__materialcost = float()
        self.__totalcost = float()

        #Calling the methods
        self.determineArea()
        self.determineWaste()
        self.determineTotal()
        self.determineRate()
        self.determineMaterialCost()
        self.determineTotalCost()
    def determineArea(self):
        self.__area = self.__length * self.__width
    #end determineArea

    def determineWaste(self):
        self.__waste = self.__area * 0.15
    #end determineWaste

    def determineTotal(self):
        self.__totalsqfoot = self.__area + self.__waste
    #end determineTotal

    def determineMaterialCost(self):
        self.__materialcost = self.__totalsqfoot * self.__price
    #end determineMaterialCost

    def determineRate(self):
        if self.__totalsqfoot >= 150:
            self.__rate = 200
        elif self.__totalsqfoot >= 100:
            self.__rate = 100
        else:
            self.__rate = 50
        #end if
    #end determineRate

    def determineTotalCost(self):
        self.__totalcost = self.__rate + self.__materialcost

    #Define Access Methods
    def returnTotalsqfoot(self):
        return self.__totalsqfoot
    #end returnTotalsqfoot

    def returnArea(self):
        return self.__area
    #end returnArea

    def returnWaste(self):
        return self.__waste
    #end returnWaste

    def returnRate(self):
        return self.__rate
    #end returnRate

    def returnMaterialCost(self):
        return self.__materialcost
    #end returnMaterialCost

    def returnTotalCost(self):
        return self.__totalcost
    #end returnTotalCost

def main():
    #declare variables
    UserWidth = float()
    UserLength = float()
    UserPrice = float()

    #Ask user for the length and the width
    UserLength = float(input("Enter the room's length:\t"))
    UserWidth = float(input("Enter the room's width:\t\t"))
    #Ask user for the price per square foot of material
    UserPrice = float(input("Enter the price per square foot of material:\t"))

    #Create the new class
    MyRoom = LaminateFloor(UserLength, UserWidth, UserPrice)

    #Print out totals
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Total Area:\t\t", MyRoom.returnArea())
    print("Waste:\t\t\t", MyRoom.returnWaste())
    print("Total Square Feet:\t", MyRoom.returnTotalsqfoot())
    print("Rate:\t\t\t", MyRoom.returnRate())
    print("Total Materials Cost:\t", MyRoom.returnMaterialCost())
    print("Total Cost of Project:\t", MyRoom.returnTotalCost())

main()
