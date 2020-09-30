#Names and Scores Example Program
#Written by:  Betsy Jenaway
#Date:  July 31, 2012

#This program demonstrates how to load 2 parallel arrays.  It will ask the
#user for the name of the student and then for their test score.

#Declare Variables
Index = 0
OneScore = 0.00
OneName = "nothing"

#Declare Arrays
Names = [" ", " ", " ", " ", " "]
Scores = [0, 0, 0, 0, 0]

#Ask the user for the names and scores
for Index in range(5):
    OneName = input("Enter a name:     ")
    OneScore = float(input("Enter a score:     "))
    #Load the name and score into the appropriate array
    Names[Index] = OneName
    Scores[Index] = OneScore

#print out the names and the scores
#reset index so we can use it again
Index = 0
for Index in range(5):
    OneName = Names[Index]
    OneScore = Scores[Index]
    print(Index + 1, ".  ", OneName, "'s Score:\t", OneScore)
