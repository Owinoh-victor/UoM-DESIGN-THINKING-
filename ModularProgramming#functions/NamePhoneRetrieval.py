#Looking for Phone Numbers
#Written by:  Betsy Jenaway
#Date:  September 21, 2012

#This program will populate 2 arrays with names and phone numbers.  It will ask
#the user to input the name they are looking for.  If the name is found, both
#the name and the phone number will be printed out.

#Defining what this program will do
def main():
    #Declare variables
    searchName = "nothing"
    FoundName = "nothing"
    phone = "nothing"
    friends = ["Matt", "Susan", "Jim", "Bob"]
    numbers = ["586-224-7854", "586-478-9826", "248-741-8956", "586-214-6983"]

    #Ask user for the name they want to search for
    searchName = GetName(friends)

    #Find the name and number in the friends array
    FoundName, phone = GetPhone(searchName, friends, numbers)

    #Print Name and Phone
    PrintNamePhone(FoundName, phone)

#Get searchName and validate it
def GetName(friends):
    #Declare Local Variables
    name = "nothing"
    Flag = False
    #Ask the user for the name and make sure it is in the list
    name = input("Enter the name you wish to search for:  ")
    #Determine if that name is in the list
    while Flag == False:
        if name in friends:
            print("We found your friend!")
            Flag = True
        else:
            print("Sorry we did not find your friend.")
            name = input("Please enter another name:  ")
            Flag = False
    return name

#Find the name and phone number of the friend
def GetPhone(searchName, friends, numbers):
    #Declare local variables
    index = 0
    flag = False
    name = "nothing"
    phone = "nothing"
    while flag == False:
        name = friends[index]
        if name == searchName:
            flag = True
        else:
            flag = False
            index = index + 1
    phone = numbers[index]
    return name, phone

#Print out name and phone
def PrintNamePhone(FoundName, phone):
    print("The name of your friend is:  ", FoundName)
    print("Your friend's phone number is:  ", phone)

main()    
    
    
