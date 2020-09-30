##Create a program that will allow the user to create a
##grocery list of items.  The program will ask the user
##for the number of items.  It will then collect these
##items.  Before printing out a list, the program will
##sort the items in the array.

##30,000 foot view
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##Ask user how many items for the list
##fill the list
##Sort the list
##print the list

def GetNumItems():
    #Declare local variables
    stringNum = str()
    GoodInt = int()
    flag = False

    #Ask user for a number and validate it
    stringNum = input("How many grocery items do you have ==>  ")

    return GoodInt

def GetGroceryItems(NumItems):
    #declare local variables
    index = int()
    oneitem = str()
    EmptyArray = []

    #Get items from user
    for index in range(0, NumItems):
        oneitem = input("Enter an item ==>  ")
        EmptyArray.append(oneitem)
    #End for

    return EmptyArray

def PrintList(List, NumItems):
    #declare local variables
    index = int()
    oneitem = str()

    #print list
    for index in range(0, NumItems):
        oneitem = List[index]
        print("Item #", index + 1, ":  ", oneitem)
    #End For

def SortList(List):
    #declare local variable
    List.sort()

    return List
   


def main():
    #Declare variables
    NumItems = int()
    List = []

    #Ask user how many items for the list
    NumItems = GetNumItems()
    #print(NumItems)
    #Fill the list
    List = GetGroceryItems(NumItems)
    #Sort the list
    List = SortList(List)
    #Print the list
    PrintList(List, NumItems)
















main()
