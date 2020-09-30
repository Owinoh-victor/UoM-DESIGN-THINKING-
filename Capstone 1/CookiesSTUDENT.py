#This program will determine if a user has hit their goal of selling cookies.
#It will also calculate how many cookies someone has sold over one week.

#Declare variables
Name = ""
DailyCookies = 0
WeeklyCookies = 0
Days = 0
Goal = 0
GoalDifference = 0
price = ""

#Ask for name and the number of cookies the user has set for a goal.
Name = input("Enter your name: ")
      #1  data type needed
Goal = int(input("Enter your goal for selling cookies:  "))

#Loop to accumulate the number of hours worked for a certain number of days in a week

while Days < 7:
    # 2 indentation within the loop
    DailyCookies = int(input("Enter the amount of cookies you sold today:"  ))    # 3 missing quote input type
    WeeklyCookies = WeeklyCookies + DailyCookies
    Days = Days + 1   #  5 Days needs to be incremented


#Determine if the user has reached their goal and their bonus
GoalDifference = WeeklyCookies - Goal
  # if, and elif statement needed.. multi is structure
                     
if GoalDifference <= 0:
    prize = "nothing"
elif GoalDifference < 5:
    prize = "mouse pad"
elif GoalDifference < 10:
    prize = "Starbucks $10 Gift Card"
elif GoalDifference < 25:
    prize = "iTunes $25 Gift Card"

elif GoalDifference >= 25:
    prize = "Movie Packet"

#Print out the bonus and number of boxes sold and number of boxes over or under the goal
print("You sold ", WeeklyCookies, "cookies this week")
print("The difference between what you sold and your goal is ", GoalDifference)
print("Your prize for going over your goal is ", prize)
