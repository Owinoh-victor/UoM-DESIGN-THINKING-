#This program will calculate the area needed, including waste, and rate
#necessary to install a laminate floor

#Written By:  Betsy Jenaway

class LaminateFloor:
    def __init__(self, NewLength, NewWidth):
        self.__length = NewLength
        self.__width = NewWidth
        self.__area = float()
        self.__waste = float()
        self.__rate = float()
        self.__totalsqfoot = float()
    def determineArea(self):
        self.__area = self.__length * self.__width
    #end determineArea

    def determineWaste(self):
        self.__waste = self.__area * 0.15
    #end determineWaste

    def determineTotal(self):
        self.__totalsqfoot = self.__area + self.__waste
    #end determineTotal

    def determineRate(self):
        if self.__totalsqfoot >= 150:
            self.__rate = 200
        elif self.__totalsqfoot >= 100:
            self.__rate = 100
        else:
            self.__rate = 50
        #end if
    #end determineRate

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

def main():
    #declare variables
    UserWidth = float()
    UserLength = float()
    price = float()
    materialcost = float()
    totalcost = float()

    #Ask user for the length and the width
    UserLength = float(input("Enter the room's length:\t"))
    UserWidth = float(input("Enter the room's width:\t\t"))

    #Create the new class
    MyRoom = LaminateFloor(UserLength, UserWidth)

    #Kicking off the calculation methods
    MyRoom.determineArea()
    MyRoom.determineWaste()
    MyRoom.determineTotal()
    MyRoom.determineRate()

    #Ask user for the price per square foot of material
    price = float(input("Enter the price per square foot of material:\t"))

    #Determine material cost and total cost
    materialcost = price * MyRoom.returnTotalsqfoot()
    totalcost = materialcost + MyRoom.returnRate()

    #Print out totals
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Total Area:\t\t", MyRoom.returnArea())
    print("Waste:\t\t\t", MyRoom.returnWaste())
    print("Total Square Feet:\t", MyRoom.returnTotalsqfoot())
    print("Rate:\t\t\t", MyRoom.returnRate())
    print("Total Materials Cost:\t", materialcost)
    print("Total Cost of Project:\t", totalcost)

main()
