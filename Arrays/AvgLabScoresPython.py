#Write a program that allows the user to determine their
#lab average grade.  Allow the user to enter in the number
#of labs.

##inputs:  score, Number of labs
##outputs:  average
##
##30,000 foot view
##******************************************
##Ask how many labs
##Fill the scores array
##Determine the average
##Output the average

#Declare Variables

NumLabs = 0
index = 0
labscore = 0
onescore = 0
totalscores = 0
average = 0
HighScore = 0
LowScore = 0

#Ask user for the number of labs and declare the array
NumLabs = int(input("Enter the number of labs:  "))

scores = [0] * NumLabs

#Fill the scores array with lab scores
for index in range(NumLabs):
    #Ask user for one lab score
    labscore = float(input("Enter a lab score:  "))
    #Take the one score and put it in the array
    scores[index] = labscore
#end for

#Determine the total scores and average
for index in range(NumLabs):
    #Remove one score from the scores array
    onescore = scores[index]
    #Add one score to the total
    totalscores = totalscores + onescore
#end for
#Determine Average
average = totalscores/NumLabs
#print out average
print("Your average is:\t", format(average, '.2f'))

#Determine the highest and lowest scores
#Set up initial values for High and Low score
HighScore = scores[0]
LowScore = scores[0]
for index in range(NumLabs):
    onescore = scores[index]
    if HighScore < onescore:
        HighScore = onescore
    #end if
    if onescore < LowScore:
        LowScore = onescore
    #end if
#end for

#Print out the high and low score
print("Your highest score is:\t", HighScore)
print("Your lowest score is:\t", LowScore)

#Another way to do this
#Sorted the array in ascending order
#
scores.sort()
for index in range(NumLabs):
    print(scores[index])

#end for
LowScore = scores[0]
print("The easy LowScore is:\t", LowScore)

#Anoter way to get HighScore
HighScore = scores[NumLabs - 1]
print("Another way to get HighScore:\t", HighScore)

#Sort the array in descending order
scores.reverse()
for index in range(NumLabs):
    print(scores[index])
#end for
HighScore = scores[0]
print("The easy HighScore is:\t", HighScore)








































































