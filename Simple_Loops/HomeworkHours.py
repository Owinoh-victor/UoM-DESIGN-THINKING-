##Write a program that allows the user to calculate how much
##time they need to spend on homework in a week.  The user
##will be asked how many classes they have and the number of
##credit hours per class.  The program will tell the user
##the number of hours they need to spend doing homework and
##the total number of credit hours they are taking this term.
##Estimate 2 hours per credit hour for homework.
##
##inputs:  Number of classes, Number of credit hours per class
##
##outputs:  Time spend doing homework, Total number of credit hours
##
##Variables:
##***************************
##NumClasses	integer
##CreditHours	integer
##Count		integer
##TimeSpent	float
##TotalCredits	integer
##Hours		float  set to 2  (constant)
##
##30,000 foot view
##****************************
##Ask user how many classes they are taking
##Determine the time spent doing homework
##Output Time spent and total credit hours

#Declare Variables
NumClasses = int()
CreditHours = int()
count = 1
TimeSpent = float()
TotalCredits = int()
Hours = 2.0

##Ask user how many classes they are taking
NumClasses = int(input("Enter the number of classes you are taking:  "))
print()
##Determine the time spent doing homework
while count <= NumClasses:
    print("Enter class #", count)
    CreditHours = int(input("Enter the number of credits for this class:  "))
    print()
    count = count + 1
    TotalCredits = TotalCredits + CreditHours
    #print(TotalCredits)
#End loop

TimeSpent = TotalCredits * Hours
print("You are taking a total of ", TotalCredits, " hours.")
print("Plan on spending ", TimeSpent, " doing Homework this term :(")


























