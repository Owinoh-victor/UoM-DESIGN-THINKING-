#This program will ask the user to enter a number.  It will then print out
#the value of that number squared.
#To exit the loop the user will enter a 0

#Declare variables
Number = 0
NumberSquared = 0

#Ask user for the number they wish to see squared
Number = int(input("Enter a number or 0 to quit:  "))

#Square the number and ask for another number
while Number > 0:
    NumberSquared = Number**2
    print("User Number:  ", Number, "     ",\
          "Number Squared:  ", NumberSquared)
    Number = int(input("Enter a number or 0 to quit:  "))
    
print("All Done!")
