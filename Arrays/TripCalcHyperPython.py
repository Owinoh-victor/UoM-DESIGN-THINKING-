#Trip Calculater on Hyper drive
##30,000 foot view
##*****************************************
##Ask the user the destination, car mpg and fuel cost
##Determine cost of the trip
##Output total cost

#Declare variables
destination = str()
mpg = float()
StringMPG = str()
fuelCost = float()
StringfuelCost = str()
paths = 1
NumStops = 0
StringNumStops = str()
stops = 1
miles = float()
Stringmiles = str()
flag = False
gallons = float()
stopCost = float()
TotalOneWayGallons = float()
TotalOneWayCost = float()
TotalTripCost = float()
TotalTripGallons = float()

#Ask the user the destination, car mpg and fuel cost
destination = input("Enter the trip destination ==>  ")
StringMPG = input("Enter your car's mpg ==>  ")
#Validate StringMPG to make sure we have a number
while flag == False:
    if StringMPG.isdigit():
        mpg = int(StringMPG)
        flag = True
    else:
        StringMPG = input("Sorry you did not enter a positive number, please try again:  ")
     #end if
#end loop
flag = False
 
StringfuelCost = input("Enter the cost for a gallon of gas ==>  ")
while flag == False:
    try:
        fuelCost = float(StringfuelCost)
        if fuelCost > 0:
            flag = True
        else:
            StringfuelCost = input("Sorry you did not enter a positive number, please try again:  ")
         #end if
    except ValueError:
        StringfuelCost = input("Sorry you did not enter a number, please try again:  ")
     #end Try
#end loop
flag = False

#Determine cost of the trip
for paths in range(1, 3):
    #Ask user for the number of stops
    StringNumStops = input("Enter the number of stops ==>  ")
    while flag == False:
        if StringNumStops.isdigit():
            NumStops = int(StringNumStops)
            flag = True
        else:
            StringNumStops = input("Sorry you did not enter a positive number, please try again:  ")
         #end if
    #end loop
    flag = False
    
    for stops in range(0, NumStops):
        Stringmiles = input("Enter the number of miles ==>  ")

        while flag == False:
            try:
                miles = float(Stringmiles)
                if miles > 0:
                    flag = True
                else:
                    Stringmiles = input("Sorry you did not enter a positive number, please try again:  ")
                 #end if
            except ValueError:
                Stringmiles = input("Sorry you did not enter a number, please try again:  ")
             #end Try
        #end loop
        flag = False
        
        gallons = miles/mpg
        stopCost = gallons * fuelCost
        TotalOneWayGallons = TotalOneWayGallons + gallons
        TotalOneWayCost = TotalOneWayCost + stopCost
        print("The number of gallons:\t", format(gallons, ',.2f'))
        print("The cost:\t\t$", format(stopCost, ',.2f'))
    #end for
    print("The number of gallons for this trip:\t", format(TotalOneWayGallons, ',.2f'))
    print("The cost for this trip:\t\t", format(TotalOneWayCost, ',.2f'))
    TotalTripGallons = TotalTripGallons + TotalOneWayGallons
    TotalTripCost = TotalTripCost + TotalOneWayCost
    TotalOneWayGallons = 0
    TotalOneWayCost = 0
#end For
#Print out the total cost of the trip to the user
print("****************************************************************")
print("The total cost of this trip is:\t", format(TotalTripCost, ',.2f'))
print("The total number of gallons:\t", format(TotalTripGallons, ',.2f'))
