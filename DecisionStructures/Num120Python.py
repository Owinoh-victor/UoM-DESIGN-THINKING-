#Declare variables
Index = 0
Player1Name = str()
Player2Name = str()
Player1Num = int()
Player2Num = int()
P1Status = str()
P2Status = str()
RandomNum = int()

#Load the random library
import random

#Use random to pick the number
RandomNum = random.randint(1,20)

#Get inputs from user
Player1Name = input("Enter Player 1's name: ")
Player2Name = input("Enter Player 2's name: ")
Player1Num = int(input("Player 1, pick a number 1-20: "))
Player2Num = int(input("Player 2, pick an umber 1-20: "))

#Set up decision structures
#Use if/else statements for player 1/2 number flags to determine if either or
#both have numbers under or equal to the random number given.
if Player1Num <= RandomNum:
    P1Status = True
else:
    P1Status = False

if Player2Num <= RandomNum:
    P2Status = True
else:
    P2Status = False

#if/else statements to determine which winner.
#If a status is false, it means the player's number was over RandomNum, and
#therefore does not need to be compared with the other's to see which is closer.
if P1Status == True and P2Status == False:
    print("The winner is: ",Player1Name)
elif P1Status == False and P2Status == True:
    print("The winner is: ",Player2Name)
#If both player are under 10, must determine which is closer to the final number.
elif P1Status == True and P2Status == True:
    if Player1Num > Player2Num:
        print("The winner is: ",Player1Name)
    elif Player2Num > Player1Num:
        print("The winner is: ",Player2Name)
    else:
        print("There was a draw!")
#If both statuses false, both went over RandomNum, and there is a draw.
else:
    print("There was a draw!")

print("The number was: ",RandomNum)
