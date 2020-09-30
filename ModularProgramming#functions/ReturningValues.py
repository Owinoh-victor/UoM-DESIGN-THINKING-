#Example of how to return value(s) from a function

import random


def GenerateRandomNums():
    #local variables to GenerateRandomNums
    num1 = int()
    num2 = int()

    #notice the variable names.  they are not the same as in main()
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    #return both values
    #notice the order -- VERY important
    return num1, num2

def PrintNumbers(rand1, rand2):  #notice the name of the parameters
                                  #and that they don't match the variables
                                  #in main()
    print()
    print("Value of Random Number 1:  ", rand1)
    print("Value of Random Number 2:  ", rand2)
    print()

    #notice no return -- Why?  This function doesn't return anything

def GetTotal(rand1, rand2):
    #declare local variables
    SumNum = int()

    SumNum = rand1 + rand2

    return SumNum

def main():
    #local variables to main
    randomNum1 = int()
    randomNum2 = int()
    total = int()

    #Call GenerateRandomNums
    #notice the order and how -- using the comma to seperate
    #   also notice the order
    randomNum1, randomNum2 = GenerateRandomNums()
    PrintNumbers(randomNum1, randomNum2)

    #Call GetTotal
    total = GetTotal(randomNum1, randomNum2)
    print("The total of both numbers is:  ", total)

    #lets do this again
    randomNum1, randomNum2 = GenerateRandomNums()
    PrintNumbers(randomNum1, randomNum2)
    total = GetTotal(randomNum1, randomNum2)
    print("The total of both numbers is:  ", total)

main()
