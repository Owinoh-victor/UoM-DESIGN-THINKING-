#Looking For Dates Program
#Written by:  Betsy Jenaway
#Date:  July 31, 2012

#This program will load an array of names and an array of dates.  It will then
#ask the user for a name.  The program will then look for the user in the list.
#If the name is found in the list the user will get a message telling them
#the name was found and the person's birthdate.  Otherwise they will get a
#message telling them the name #was not found and to try again.  NOTE:  this
#program differs from the Raptor program in that it continually asks the user
#for a name until one is found in the list.

#Declare Variables
#Loading the array with names
Friends = ["Matt", "Susan", "Jim", "Bob"]
Dates = ["12/2/99", "10/15/95", "3/7/95", "6/24/93"]
SearchItem = "nothing"
FoundDate = "nothing"
FoundIndex = 0
Index = 0
Flag = False

#Look for the name and tell the user if the program found it
#Keep asking the user for a name until one is found.
while Flag == False:
    #Ask the user for the name to search for
    SearchItem = input("What is the name you are looking for?     ")
    if SearchItem in Friends:
        #Find out what the index is for the Found Name
        FoundIndex = Friends.index(SearchItem)
        FoundDate = Dates[FoundIndex]
        Flag = True
        print("We found your name!")
        print(SearchItem, "'s Birthday is:  ", FoundDate)
    else:
        print("Sorry we did not find your name.  Please try again.")
        Flag = False
