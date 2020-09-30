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
StringNumDays = str()
shells = int()
StringShells = str()
StringMoney = str()
money = float()
ChildMoney = float()
ChildTotal = 0
ChildAverage = 0.0
groupTotal = 0
groupAverage = 0.0
UserContinue = "yes"
flag = False

#Ask the user how many days they will be collecting shells
StringNumDays = input("How many days will you be collecting shells ==> ")
#Input validation on StringNum
while flag == False:
    if StringNumDays.isdigit():
        NumDays = int(StringNumDays)
        flag = True
    else:
        StringNumDays = input("Sorry you did not enter a valid positive number, please try again ==> ")
    #end if
#end if
flag = False

#Loop to get kid's names and calculate group totals
while UserContinue == "yes":
    name = input("Enter the name of the kid:  ")
    for days in range(0, NumDays):
        StringShells = input("Enter the number of shells you collected today ==> ")
        while flag == False:
            if StringShells.isdigit():
                shells = int(StringShells)
                flag = True
            else:
                StringShells = input("Sorry you did not enter a valid positive number, please try again ==> ")
            #end if
        #end if
        
        flag = False       
        
        ChildTotal = ChildTotal + shells
    #end For
    #Find out from the user how much money they want to make off of their shells
    StringMoney = input("How much money do you want to make on each shell ==> ")
    while flag == False:
        try:
            money = float(StringMoney)
            if money > 0:
                flag = True
            else:
                StringMoney = input("Sorry you did not enter a positive number, please try again ==> ")
            #end if
        except ValueError:
            StringMoney = input("Sorry you did not enter a number, please try again ==> ")
        #End try catch
    #End loop
    flag = False
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
    while flag == False:
        if UserContinue == "yes" or UserContinue == "no":
            flag = True
        else:
            UserContinue = input("Sorry you did not enter a 'yes' or 'no', please try again ==> ")
            UserContinue = UserContinue.lower()
   
    flag = False
        
#End Loop
groupAverage = groupAverage/child
print("The group collected ", groupTotal, " shells this week!")
print("The group collected ", groupAverage, " shells per day!")
    
    

