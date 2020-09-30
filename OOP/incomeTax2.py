## Program Created By: Yousif Alawsachi
## Student Success: Income Tax

#Define the class comission
class IncomeCalculation:

    #Create and define the constructore
    def __init__(self, NewIncome):
        self.__income = NewIncome
        self.__rate = 0.0
        self.__tax = 0.0
        self.__netpay = 0.0

#determines and define the tax based on income
    def DetermineTax(self):
        if self.__income <= 20000:
            self.__rate = 0.0
        elif self.__income >= 20000 and self.__income < 100000:
            self.__rate = 0.25
        elif self.__income >= 100000 and self.__income < 250000:
            self.__rate = 0.35
        else:
            self.__rate = 0.45

#Determine and define the tax
    def DetermineTaxTotal(self):
        self.__tax = self.__income * self.__rate

#Detemine and define the netpay
    def DetermineNetPay(self):
        self.__netpay = self.__income - self.__tax

#Allows main() to grab income, tax, netpay
    def GetIncome(self):
        return self.__income
    def GetTax(self):
        return self.__tax
    def GetNetPay(self):
        return self.__netpay


def main():
    #Declare Variables
    IncomeAmount = 0.0

    #Ask the user for their income
    IncomeAmount = float(input("Enter your income: $"))

    #Create the new TaxCalc object based of the Income Calculation Class
    TaxCalc = IncomeCalculation(IncomeAmount)

    #Run the Determine Income,Tax, NetPay in Income Calculation Class
    TaxCalc.DetermineTax()
    TaxCalc.DetermineTaxTotal()
    TaxCalc.DetermineNetPay()
    

    #Print out Income, Tax, and NetPay to User
    print("Your total income after tax is: $", TaxCalc.GetNetPay())
    print("Your total tax in dollars is: $", (IncomeAmount - TaxCalc.GetNetPay()))
    

main() #Execute main

         
