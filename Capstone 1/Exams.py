

def PrintSales(owner_sales):
    index=0
    sales=float
    print ("Sales By Owner")
    print("*******************")
    #getting the sales from the list and printing them out
    for sales in owner_sales:
        print(sales)

#methord to find the lowest sales
def FindLowest(owner_sales):
    lowest = 0.0
    #this loop iterates through the lists and finds the lowest sales
    for i in range(0, len(owner_sales)):
        lowest = min(owner_sales)
        #returint the lowest sales to the main function where it is called
    return lowest

def DeterminePayout(owner_sales):
    checkamount=float
    print(" Owner Check Amounts")
    print("*************************")
    for sales in owner_sales:
        # checks for each sales, and multiply the by 0.75 (100 - 25 % )
        #Also use the round function to round the sales to 2 dpl
        checkamount=  round(sales * 75/100,2)
        #print out the owner check amounts
        print(checkamount)
def main():
    #initializing and assigning  my list of sales
    owner_sales = [201.45, 550.00, 117.65, 55.25, 5.95, 365.54]
    #Methord invocation / function calls
    PrintSales(owner_sales)
    print ("Lowest Sales is : ", FindLowest(owner_sales))
    DeterminePayout(owner_sales)
#call the main function
main()