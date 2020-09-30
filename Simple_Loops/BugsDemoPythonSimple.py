#Declare Variables
WeeklyBugs = 0
DailyBugs = 0
Days = 1

#Loop to count the number of bugs collected this week
while Days <= 7:
    DailyBugs = int(input("Enter today's collection of bugs:     "))
    WeeklyBugs = WeeklyBugs + DailyBugs
    Days = Days + 1

#Output the total number of bugs to the user
print("You collected ", WeeklyBugs, " this week.")
