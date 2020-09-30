"""
4 function including the main function

GetTotal(sales)
===============
get total using a loop and return oit to main

GetAverage(sales,total)
===================
get avaerage sales and print it out
ReturnList(sales)
===================
print out my list

main()
==================
initialize my variables and call other functions

"""
def ReturnList(sales):

        print("My List",sales)

def GetTotal(sales):
    total = 0.0
    for i in range(0, len(sales)):
        total= sum(sales)
        #average= total / 7
        return total

def GetAverage(sales):
    for i in range(0, len(sales)):
        total= sum(sales)
        average= total / 7

    print("Sales Average: " , average)



def main():

    total=float()
    sales=[1524, 1647,1324,1298,1478, 1765,1725]
    average=float()
    mysales=int()

    #function calls
    ReturnList(sales)
    GetTotal(sales)
    #output
    print ("Sales Total:",GetTotal(sales) )
    GetAverage(sales)
main()
