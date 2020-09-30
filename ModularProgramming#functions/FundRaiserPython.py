#Fund Raiser Program
def GetTotalAvg(Sales):
    #Declare variables local to GetTotalAvg
    #Our array Sales has to be sent in because it is a local variable to main().  Be careful not to change the contents.
    TotalSales = float()
    OneSale = float()
    Average = float()
    index = int()
    #Access Sales to find out TotalSales
    for index in range(0, 8):
        OneSale = Sales[index]
        TotalSales = TotalSales + OneSale
    #End for
    #Print out Total Sales and determine and print out average
    print("==========================================")
    Average = TotalSales/8
    print("Total Sales:\t$", format(TotalSales, ',.2f'))
    print("Average Sale:\t$", format(Average, ',.2f'))
    print("==========================================")
    #No need to include return because this function returns NOTHING

def PrintSales(Sales):
    #Local Variable declaration.  Remember not to change Sales.  Arrays in Python are sent in by Reference
    index = int()
    OneSale = float()
#Pulling each sale out of the Sales array in order to print them
    for index in range(0, 8):
        OneSale = Sales[index]
        print("One Day's Sale:\t$", format(OneSale, ',.2f'))
    #end for

def FindMaxMin(Sales):
    #Sales is a by reference pass because it is an array.  Be careful not to change anything.
    #Local Variable declaration
    maxSale = float()
    minSale = float()
    index = int()
    OneSale = float()

    #In order to utilize the sort() method to pluck the highest and lowest values out of the list, you first need to make a
    #copy of the list.  If you don't, Python will send the list in by reference rather than by value

    SortedSales = list(Sales)
    print("Print out of Sales array before sort")
    PrintSales(Sales)
    print("Print out of Sorted Sales array before sort")
    PrintSales(SortedSales)
    SortedSales.sort()
    print("Print out of Sorted Sales array after sort")
    PrintSales(SortedSales)
    print("Print out of Sales array after sort")
    PrintSales(Sales)
    maxSale = SortedSales[7]
    minSale = SortedSales[0]
    #Setting up initial values for max and min Sale
##    maxSale = Sales[0]
##    minSale = Sales[0]
##    
##    for index in range(0, 7):
##        OneSale = Sales[index]
##        if maxSale > OneSale:
##            maxSale = OneSale
##        #end if
##    #end for
##
##    for index in range(0, 7):
##        OneSale = Sales[index]
##        if minSale < OneSale:
##            minSale = OneSale
##        #end if
##    #end for

    #Print out Max and Min Sales
    print("====================================")
    print("Max Sale:\t$", format(maxSale, ',.2f'))
    print("Min Sale:\t$", format(minSale, ',.2f'))
    print("====================================")

def GetChanged(ChangeMe):
    #local variables
    ChangeMe = input("Enter another value for ChangeMe:  ")
    print()
    print()
    print("This is the value of ChangeMe inside GetChanged:  ", ChangeMe)

def main():
    #Variable Declaration for main()
    #These variables are only good in main()
    Sales = [525, 650, 1100, 335, 450, 1200, 825, 675]
    #Calling GetTotalAvg
    GetTotalAvg(Sales)
    #Calling PrintSales
    PrintSales(Sales)
    #Calling FindMaxMinSales
    FindMaxMin(Sales)
    #Proving that Sales is still OK
    PrintSales(Sales)
    #What follows here has nothing to do with this problem but good to see nonetheless.  
    #This is a good example of what happens with local variables that are not lists
    #declare a variable local to main()
    ChangeMe = str()
    #Setting up the original value of ChangeMe
    ChangeMe = input("Enter a value that you want changed:  ")

    GetChanged(ChangeMe)
    print("This is the value of ChangeMe after GetChanged:  ", ChangeMe)    
#MUST include this line or the program will not work
main()
