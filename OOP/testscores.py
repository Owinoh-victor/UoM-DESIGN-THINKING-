class TestScores:
    def __init__(self, newName, newTestScore1, newTestScore2):
        #defining attributes
        self.__Name = newName
        self.__TestScore1 = newTestScore1
        self.__TestScore2 = newTestScore2
        self.__TestTotal = float()

#Determine the test total
    def DetermineTestTotal(self):
        self.__TestTotal = self.__TestScore1 + self.__TestScore2

#Return Name
    def ReturnName(self):
        return self.__Name

#Return TestScore1
    def ReturnTestScore1(self):
        return self.__TestScore1

#Return TestScore2
    def ReturnTestScore2(self):
        return self.__TestScore2

#Return TestTotal
    def ReturnTestTotal(self):
        return self.__TestTotal

#End Class

def main():
    #declare variables
    MainName = str()
    MainTestScore1 = int()
    MainTestScore2 = int()
    Continue = "yes"

    while Continue == "yes":
        #input questions to the user
        MainName = input("Please enter in your name: ")
        MainTestScore1 = int(input("Please enter in your first testscore: "))
        MainTestScore2 = int(input("Please enter in your second testscore: "))

        #Create new object
        Item = TestScores(MainName, MainTestScore1, MainTestScore2)

        #call determine test total
        Item.DetermineTestTotal()

        #Output to the user
        print("Name: ",Item.ReturnName())
        print("TestScore1: ",Item.ReturnTestScore1())
        print("TestScore2: ",Item.ReturnTestScore2())
        print("TestTotal: ",Item.ReturnTestTotal())

        #ask the user if they want to continue
        Continue = input("Do you wish to continue? ")

#End loop


main()
