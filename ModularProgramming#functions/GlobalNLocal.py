globalNum1 = 1 #This our global variable


def DetermineNum(someNum):#notice how we use a different variable name

    #changing the value of globalNum1
    globalNum1 = 2
    #print it
    print("Value of global variable inside DetermineNum:  ", globalNum1)

    #changing the value of someNum
    someNum = 0
    #printing it
    print("Value of someNum(local_main1) inside DetermineNum:  ", someNum)
    

def main():  #Defines the main function which runs our program
    #Declare local variables to main
    local_main1 = int()
    local_main2 = int()

    #print("This is the value of our global variable:  ", globalNum1)

    local_main1 = 3  #Gives local_main a value
    #Call DetermineNum
    DetermineNum(local_main1)

    #print globalNum after the function call
   # print("This is the value of global Num after the function call:  ", globalNum1)

    #print local_main after the function call
    print("This is the value of local main 1 after the function call:  ", local_main1)

    #changing global num inside main
    globalNum1 = 10
    print("New value of globalNum1:  ", globalNum1)








main() #calls main().  We need this for the program to run.
