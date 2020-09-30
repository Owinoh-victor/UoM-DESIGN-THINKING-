#Ryan VanDenBerg
#12/6/13

#This program will determine what income tax they have to pay based on
#their annual income.

class DetermineTax:
    def __init__(self, NewIncome):
        #Defining attributes
        self.__Income = NewIncome
        self.__TaxPercentage = int()

    def DetermineTaxPercentage(self):
        
        if  self.__Income <= 50000:
            self.__TaxPercentage = 14
        elif self.__Income <= 100000:
            self.__TaxPercentage = 23
        else:
            self.__TaxPercentage = 30

    def ReturnTaxPercentage(self):
        return self.__TaxPercentage
#End Class

def main():
    #Declare the variables
    MainIncome = int()
    MainTaxpercentage = int()
    Continue = "yes"


    while Continue == "yes":
        #Ask the user for their income
        MainIncome = int(input("Enter in your income:  "))

        #Create the MainDetermineTax object
        MainDetermineTax = DetermineTax(MainIncome)
    
        #Determine the tax percentage
        MainDetermineTax.DetermineTaxPercentage()

        #Print the tax percentage

        print("Your tax percentage is:  ", MainDetermineTax.ReturnTaxPercentage(), "%")

        Continue = input("Do you wish to continue? Type yes or no.")

main()

    

            
            
            
              
