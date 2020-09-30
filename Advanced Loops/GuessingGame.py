##Guessing Game
##
##Problem Statement:  This program will allow the user 5 guesses to see if they can guess
##                    a randomly generated number.
##
##inputs:  if the user wishes to continue, guess
##outputs:  number, if they guessed the right number
##
##variables
##usercontinue	string
##userguess	int
##compnum		int
##
##30,000 foot view
##**********************************
##loop while user wants to still play
##	Generate random number
##	loop while numguess <= 5
##		Ask user for their guess
##		if userguess == compnum then
##			print "You guessed the number"
##			numguess = 6
##		else
##			if userguess > compnum then
##				print "Your guess is too high"
##			else
##				print "Your guess is too low"
##			end if
##
##			numguess = numguess + 1
##
##		end if
##	end loop
##end loop

#declare variables
usercontinue = str()
userguess = int()
compnum = int()
numguess = int()

#setting usercontinue to 'yes' so that the outer loop runs
usercontinue = "yes"
#set numguess = 1 to start counting
numguess = 1
#importing random library so that we can generate a random number
import random

#Outer loop that determines how long the program will run
while usercontinue == "yes":
    #generate random number between 1 and 100
    compnum = random.randint(1, 100)
    #Inner loop determines if the user has guessed the number correctly
##    while numguess <= 5:
##        #ask user for a guess
##        userguess = int(input("Enter your guess:  "))
##        #Determine if the user guessed correctly
##        if userguess == compnum:
##            print("You guessed the number!")
##            #force the loop to end
##            numguess = 6
##        else:
##            if userguess > compnum:
##                print("Your guess is too high")
##            else:
##                print("Your guess is too low")
##            #end if
##            numguess = numguess + 1
##        #end if
##    #end while
##    #reset numguess so that the user can guess a new number
##    numguess = 1
    for numguess in range(1,6):
        userguess = int(input("Enter your guess:  "))
        if userguess == compnum:
            print("You guessed the number!")
            break
        else:
            if userguess > compnum:
                print("Your guess is too high")
            else:
                print("Your guess is too low")
            #end if
        #end if
                
    #ask user if they want to play again
    usercontinue = input("Enter yes to continue:  ")
#end while
        








