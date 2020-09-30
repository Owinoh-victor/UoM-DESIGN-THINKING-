#This program will ask the user for various trips and then calculate MPG

def GetNumTrips():
    #Declare local variables
    strnumtrips = str()
    goodinteger = int()
    flag = False
    #Ask the user for a number
    strnumtrips = input("Enter the number of trips:  ")
    #Validate the number
    while flag == False:
        if strnumtrips.isdigit():
            goodinteger = int(strnumtrips)
            flag = True
        else:
            #ask the user for another integer
            strnumtrips = input("Sorry you did not enter a positive integer.  Please try again:  ")
            flag = False
    #if we are here it means we have a good integer
    return goodinteger

def GetTripNames(numtrips):
    #declare local variables
    tripname = str()
    index = 0
    emptyarray = [" "] * numtrips
    #Fill emptyarray
    for index in range(0, numtrips):
        tripname = input("Enter the name of your trip:  ")
        emptyarray[index] = tripname

    #Send empty array back
    return emptyarray

def GetTripMiles(numtrips):
    #declare local variables
    nummiles = float()
    strmiles = str()
    emptyarray = [0.0] * numtrips
    index = 0
    #fill emptyarray
    for index in range(0, numtrips):
        #ask user for number of miles
        strmiles = input("Enter the number of miles for your trip:  ")
        miles = GetGoodFloat(strmiles)
        emptyarray[index] = miles
    #return emptyarray
    return emptyarray


def GetGoodFloat(dummynumber):
    #Declare local variables
    flag = False
    goodfloat = 0.0

    #Validate dummynumber
    while flag == False:
        try:
            goodfloat = float(dummynumber)
            if goodfloat < 0:
                flag = False
                dummynumber = input("Sorry you did not enter a positive decimal.  Please try again:  ")
            else:
                flag = True
        except ValueError:
            dummynumber = input("Sorry you did not enter a positive decimal.  Please try again:  ")
            flag = False

    #If we are here it means the user gave us a positive float.  We can return it
    return goodfloat

def GetTripGallons(numtrips):
    #declare local variables
    strgallons = str()
    numgallons = float()
    emptyarray =  [0.0] * numtrips
    index = 0
    #fill empty array
    for index in range(0, numtrips):
        strgallons = input("Enter the number of gallons:  ")
        numgallons = GetGoodFloat(strgallons)
        emptyarray[index] = numgallons
    #return empty array
    return emptyarray

def CalcMPG(numtrips, miles, gallons):
    #declare local variables
    calcmpg = 0.0
    index = 0
    emptyarray = [0.0] * numtrips
    #Calculate MPG and fill the array
    for index in range(0, numtrips):
        calcmpg = miles[index] / gallons[index]
        emptyarray[index] = calcmpg
    #return empty array
    return emptyarray

def PrintTripInfo(numtrips, names, miles, gallons, mpg):
    #declare local variable
    index = 0
    #print list heading
    print("Trip Name\t\tTrip Miles\tTrip Gallons\tTrip MPG")
    print("*********\t**********\t************\t********")
    #print out contents of array
    for index in range(0, numtrips):
        print(names[index], '\t\t', miles[index], '\t\t', gallons[index], '\t\t', format(mpg[index], '.2f'))
    

def main():
    #declare local variables to main()
    numtrips = int()

    #Get Number of trips
    numtrips = GetNumTrips()
    #print(numtrips)

    #Declare our arrays
    names = [" "] * numtrips
    gallons = [0.0] * numtrips
    mpg = [0.0] * numtrips
    miles = [0.0] * numtrips

    #Fill our arrays
    names = GetTripNames(numtrips)
    miles = GetTripMiles(numtrips)
    gallons = GetTripGallons(numtrips)
    mpg = CalcMPG(numtrips, miles, gallons)

    #Print out our trip information
    PrintTripInfo(numtrips, names, miles, gallons, mpg)


 

        

    











main()
