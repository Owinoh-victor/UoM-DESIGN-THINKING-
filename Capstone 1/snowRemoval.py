
"""
6. Challenge Exercise 4 ~ Snow Removal
Create a class called SnowRemoval. This class will utilize a constructor so that the class can obtain the size of the sidewalk that
needs to be plowed along with any driveways. The size of the sidewalk is measured in feet and needs to be saved as a float.
The number of driveways will be saved as an integer. Within your class store these values in attributes called sidewalk and driveway.
Your class will need a method to calculate how much it will cost to have the snow removed on a property.
This calculation will take the size of the sidewalk, measured in feet, and multiply it by 5.
Meaning it will cost 5 dollars a foot to have your snow shoveled.
Additionally you will include an extra cost if there is a driveway. If there is no driveway then the cost is 0.
If there is a one car driveway the price to plow the driveway is 10 dollars. If the driveway is for 2 cars,
the cost to plow the driveway is 20 dollars. If there are 3 or more cars the cost will be 30 dollars.
 Finally, if there are 4 or more driveways the cost is 50 dollars.
Store the total cost in an attribute called total. Name this method CalculateTotal.
 In order to allow the total cost to leave the class, you will need to create a second method called ReturnTotal.
  All this method does is return the total.
When creating this class start coding in VS Code or IDLE. To test your class create an object.
Send in the values 15 and 2 (15 feet and 2 car driveway). Next call your method CalculateTotal.
Finally print the method ReturnTotal to the screen. Your code should print the following:

95
"""
class SnowRemoval():
    def __init__(self, size, ways):

        self.sidewalk = size
        self.driveways = ways
        self.price = float
        self.Extra = float()
        self.Total = float()

    def Cost(self):

        self.price = self.sidewalk * 5
        return self.price

    def ExtraCost(self):

        if self.driveways == 0:
            self.Extra = 0

        elif self.driveways == 1:
            self.Extra = 10

        elif self.driveways == 2:
            self.Extra = 20

        elif self.driveways == 3:
            self.Extra = 30

        elif self.driveways >= 4:
            self.Extra = 50

        return self.Extra

    def CalculateTotal(self):

        self.Cost()
        self.ExtraCost()
        self.Total = self.price + self.Extra
        return self.Total

    def ReturnTotal(self):

        return self.CalculateTotal()


def main():
    Get = SnowRemoval(15, 2)

    # output
    print(Get.ReturnTotal())

main()






