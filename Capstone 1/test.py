#Variables
guess = int()
randomNum = int()
chances = int()
UserContinue = str()

#Generate the random number
while UserContinue =="yes": #error1: == is used to check variables
    randomNum = random.randint(1, 100)
    guess = int(input("Enter your guess ==>  "))
    while chances <=6:
        if guess == randomNum:
            print("You Win!")
            chances = chances + 1  #increment i9s expected
        elif guess > randomNum: #greater than expected
            print("Your guess is higher than the chosen number.")
            guess = int(input("Please enter another number ==>  "))
            chances = chances + 1
        else:
            print("your guess is lower than the chosen number.")
            guess = int(input("Please enter another number ==>  "))
            chances = chances + 1
        #end if
    #end loop
    #Ask the user if they want to continue
    UserContinue = input("Do you want to play again?  Enter yes or no ==>  ")
#End loop 