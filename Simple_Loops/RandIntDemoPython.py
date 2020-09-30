#This is a demo of the rand.int function
#By Rebecca Schauer

#Import Library for random
import random
#Declare Variables
SecretNumber = 0
GuessNumber = 0
Tries = 0
#Get Secret Number using random.randint
SecretNumber = random.randint(1,10)
#Ask user to input a number between 1 and 10 untill it matches the number that was randomly generated
while GuessNumber != SecretNumber:
    GuessNumber = int(input("Guess the Secret Number!(Its a number between 1 and 10):  "))
    if GuessNumber != SecretNumber:
        print("You didnt guess the Secret Number! Try again!")
    else:
        print("You Guessed the Secret Number!")
    Tries = Tries + 1
print("The Secret Number was:  ",SecretNumber)
print("It took you", Tries,"tries to guess the Secret Number!")
            
