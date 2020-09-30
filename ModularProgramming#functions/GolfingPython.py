def IntroMessage():
    print("This program will ask you to pick a golf club to swing with to knock a golf ball into a hole 300 yards away. The ball will go into the hole if within 20 feet.")
    print(" --------------------------------\n| Club A has a range of 200-350. |\n| Club B has a range of 110-150. |\n| Club C has a range of 30-90.   |\n| Club D has a range of 10-30.   |\n --------------------------------")

def ClubChoiceDist():
    #Declare local variables
    ClubChoice = str("")
    Flag = False
    Distance = float()
    #Get choice from user
    ClubChoice = input("Select a club for your swing (A, B, C, D): ")
    #Start loop for input validation
    while Flag == False:
        #Use procedures within the procedure for club ranges
        if ClubChoice == "A":
            Distance = ClubA()
            Flag = True
        elif ClubChoice == "B":
            Distance = ClubB()
            Flag = True
        elif ClubChoice == "C":
            Distance = ClubC()
            Flag = True
        elif ClubChoice == "D":
            Distance = ClubD()
            Flag = True
        else:
            ClubChoice = input("You did not pick a valid club (A, B, C, D), please try again: ")
    return Distance

def ClubA():
    #Locals
    Distance = 0.0
    #Import random library
    import random
    #Calculate distance
    Distance = random.randint(200,350)
    return Distance

#Club B-D are same as Club A, just with different random ranges.
def ClubB():
    Distance = 0.0
    import random
    Distance = random.randint(110,150)
    return Distance

def ClubC():
    Distance = 0.0
    import random
    Distance = random.randint(40,100)
    return Distance

def ClubD():
    Distance = 0.0
    import random
    Distance = random.randint(10,30)
    return Distance
    
def main():   
    #Local variables
    Distance = 0.0
    CurrentDist = 300
    SwingNum = 0
    #Call intro message procedure
    IntroMessage()
    #Use a loop until CurrentDist is less than or equal to 20
    while CurrentDist > 20:
        Distance = ClubChoiceDist()
        #Take absolute value in case of over-shooting.
        CurrentDist = abs(CurrentDist - Distance)
        SwingNum = SwingNum + 1
        #Print out to user
        print("Swing number: \t\t",SwingNum)
        print("Distance hit: \t\t",Distance)
        print("Distance from hole: \t",CurrentDist)
        print("")
    if SwingNum == 1:
        print("Congratulations, you got a hole in 1!")
    else:
        print("It took",SwingNum,"swings for your golf ball to reach the hole.")
        
main()
