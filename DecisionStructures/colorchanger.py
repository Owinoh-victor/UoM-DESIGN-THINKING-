#Color Changer Program
#Written by:  Elizabeth Jenaway
###Dated:  1/29/2013
##Create a program that will tell the user what color they have.  The user will be asked for two primary colors and the program will tell the use what new color they created.
##
##inputs:  2 primary colors
##outputs:  new color
##
##30,000 foot view
##Ask the user for the primary colors
##Determine the new color
##Output the new color

#Declare Variables
firstcolor = str()
secondcolor = str()
newcolor = str()

#Ask the user for the primary colors
firstcolor = input("Enter red, yellow or blue:  ")
secondcolor = input("Enter red, yellow or blue:  ")

#Determine the new color
if firstcolor == "yellow":
    if secondcolor == "blue":
        newcolor = "green"
    elif secondcolor == "red":
        newcolor = "orange"
    else:
        newcolor = firstcolor
    #end if
elif firstcolor == "red":
    if secondcolor == "blue":
        newcolor = "purple"
    elif secondcolor == "yellow":
        newcolor = "orange"
    else:
        newcolor = firstcolor
    #end if
elif firstcolor == "blue":
    if secondcolor == "yellow":
        newcolor = "green"
    elif secondcolor == "red":
        newcolor = "purple"
    else:
        newcolor = firstcolor
    #endif
else:
    print("You did not enter red, blue or yellow")
#end if

#Output new color to the user
print("Your new color is:  ", newcolor)


















