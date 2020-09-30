#Looking For Someone Program
#Written by:  Betsy Jenaway
#Date:  July 31, 2012

#This program will load an array of names.  It will then ask the user for a name.
#If the name is found in the list the user will get a message telling them
#the name was found.  Otherwise they will get a message telling them the name
#was not found.

#Declare Variables
#Loading the array with names
Friends = ["Matt", "Susan", "Jim", "Bob"]
SearchItem = "nothing"

#Ask the user for the name to search for
SearchItem = input("What is the name you are looking for?     ")

#Look for the name and tell the user if the program found it
if SearchItem in Friends:
    print("We found your name!")
else:
    print("Sorry we did not find your name")
