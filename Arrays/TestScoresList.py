#This example program asks the user for 5 test scores.  It then produces
#an average

#Declare variables
Index = 0
OneScore = 0.0
SumScores = 0.0
AverageScore = 0.0
#Declare the list to have 5 items in it
Scores=[0,0,0,0,0]

#Load the list with scores
for Index in range(5):
    OneScore = float(input("Enter a test score:  "))
    Scores[Index] = OneScore

#Print out the list
print("Here are your test scores")
print("=========================")
for OneScore in Scores:
    print("\t",OneScore)

#Determine the Average Score
for OneScore in Scores:
    SumScores = SumScores + OneScore

AverageScore = SumScores/5

#Print the Average
print("The Average Score is:  ", AverageScore)
