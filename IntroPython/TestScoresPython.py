#Test Scores Program
#Created by:  Mrs. Jenaway
#Dated:  Whatever date
#This program will ask the user for 2 test scores.  It
#     will produce a total score and an average.

#Declare Variables
TestScore1 = 0.0
TestScore2 = 0.0
TestAvg = 0.0
TotalTest = 0.0

#Asking user for two test scores
TestScore1 = float(input("Enter your first test score:  "))
TestScore2 = float(input("Enter your second test score:  "))

#Calculating the total and average of both test scores
TotalTest = TestScore1 + TestScore2
TestAvg = TotalTest/2

#Outputting total and average to the user
print("The total of your test scores is:  " , TotalTest)
print("The average of your test scores is:  ", TestAvg)
