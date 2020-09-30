#This program will allow the user to add shells collected on the beach for each
#day during a long weekend.  The program will also tells us how many shells
#each kid collected each day along with the average.  The program will also
#allow us to find out how much money we can make if we sell our shells
#Finally it will tell us how many shells were collected in total and the
#average for the group.

#Declare variables
name = str()
child = 0
NumDays = int()
shells = int()
money = float()
ChildMoney = float()
ChildTotal = 0
ChildAverage = 0.0
groupTotal = 0
groupAverage = 0.0
UserContinue = "yes"

#Ask the user how many days they will be collecting shells
NumDays = int(input("How many days will you be collecting shells ==> "))

#Loop to get kid's names and calculate group totals
while UserContinue == "yes":
    name = input("Enter the name of the kid:  ")
    for days in range(0, NumDays):
        shells = int(input("Enter the number of shells you collected today ==> "))    
        ChildTotal = ChildTotal + shells
    #end For
    #Find out from the user how much money they want to make off of their shells
    money = float(input("How much money do you want to make on each shell ==> "))
    ChildAverage = ChildTotal/NumDays
    groupTotal = groupTotal + ChildTotal
    groupAverage = groupAverage + ChildAverage
    ChildMoney = ChildTotal * money
    child = child + 1     
    print("You collected ", ChildTotal, " shells this week!")
    print("You averaged ", ChildAverage, " shells each day!")
    print("If you sold your shells, you would make:  $", format(ChildMoney, ',.2f'))
    ChildTotal = 0
    UserContinue = input("Do you wish to add another kid?  ")
    UserContinue = UserContinue.lower()
    
#End Loop
groupAverage = groupAverage/child
print("The group collected ", groupTotal, " shells this week!")
print("The group collected ", groupAverage, " shells per day!")
    
    

