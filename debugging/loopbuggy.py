#------------------------------------------------------------------------------
# Shungloon Wong
# This program will act as a casino, with the user having a passive income
# of $50 a day for a week. The user may choose to gamble to double his worth
# or lose it all to chance (or the system clock).
#------------------------------------------------------------------------------

#importing 
import random

# Assigning variables
dailyIncome = 50.00
chance = int()
totalMoney = float() #bug 1: Expected parenthesis for a float type
moneyLost = float()
days = 0
gamble = str()

# Introduction
print("This program will have you gamble money you earn passively, each day\
 you will gain $50 passively, to which you will gamble to double or\
 lose its entirety. You may gamble or conserve your money for a total of\
 seven days.")
print()

# While loop
while days != 7: # redundant parenthesis: This code works well without the parenthesis. PEP8 don't need it.
    totalMoney = totalMoney + dailyIncome
    gamble = input("You've earned $ 50. Do you gamble, or conserve?\
    \n\n Type either \"Yes\" or \"No\" to proceed:").lower()

# If loop    
    if gamble == "yes": # bug 3: we use  == to assign a string value: syntax error
        chance = random.randint(1, 10)      
# Nested if loop
        if chance > 5: # bug4:  colon is expected
            print("You've doubled your money!")
            totalMoney = totalMoney * 2
            print("You now have $", totalMoney, "dollars!")
            days = days + 1 #bug5: logic error. We are supposed to increase the day counter and not decrease
        else:
            print("You've lost all of your money!")
            moneyLost = totalMoney + moneyLost
            totalMoney = totalMoney * 0
            print("You now have $", totalMoney, "dollars.")
            days = days + 1
# End selection structure
    else:
        print("You conserved your money, you have ", totalMoney, "dollars total.") #Bug4: type error, we cant concatenate str and float
        days = days + 1
# End  while loop

# Finishing off        
print()
print("In these past 7 days, you have passively earned a total amount of $ 350.00\
 with gambling or conserving, you leave with a total of: $", totalMoney)
print()
print("You have lost a total of $", moneyLost)
