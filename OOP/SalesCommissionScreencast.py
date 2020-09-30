class Commission:
    #constructor
    def __init__(self, NewSales):
        self.sales = NewSales
        self.rate = 0.0
        self.commission = 0.00

#determines the commission rate based on sales
    def DetermineRate(self):
        if self.sales <= 3000:
            self.rate = 0.03
        elif self.sales <= 5000:
            self.rate = 0.05
        elif self.sales <= 10000:
            self.rate = 0.08
        else:
            self.rate = 0.10

#Calcualtes the commission
    def DetermineCommission(self):
        self.commission = self.sales * self.rate

    def GetRate(self):
        return self.rate
    def GetCommission(self):
        return self.commission
    def GetSales(self):
        return self.sales
def main():
    #declare variables
    SalesAmount = 0.0

    #Ask the user for their monthly sales
    SalesAmount = float(input("Enter your sales amount for this month:  $"))

    #Create the new CommCalc object based off of the Commission class
    CommCalc = Commission(SalesAmount)

    #Run the Determine Rate and Determine Commission methods in Commission
    CommCalc.DetermineRate()
    CommCalc.DetermineCommission()

    #Print out Sales, Rate and Commission to the user
    print("Your total Sales for this month was:  $", format(CommCalc.GetSales(), ',.2f'))
    print("Your Commission Rate is:  ", (CommCalc.GetRate() * 100), "%")
    print("Your Earned Commission is:  $", format(CommCalc.GetCommission(), ',.2f'))
    
#Call main
main()
