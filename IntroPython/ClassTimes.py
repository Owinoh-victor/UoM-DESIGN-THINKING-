# Example 01 // by R.M. Weidner // I'm a lumberjack and I'm okay, I sleep all night and I work all day.

#This is the Python code which follows the Example01 Raptor file. Feel free to compare the two
#at your leisure.

#The first thing to do is to declare your variables. There are a couple of ways to do this, but we'll start with the simplest
#way for now.
Length = 0 #A single zero tells Python that this is an integer. Using 0.0 or 0.00 would indicate this is a float.
Days = 0
Weeks = 16
Number = 0
Total = 0

print("Let's see how long you have left in this class, shall we?")
print("") # I entered a blank line here. You will learn how to do this an easier way as the class progresses.
Length = int(input("How many hours does this class run daily?"))
Days = int(input("How many times each week does this class meet?"))
Number =int( input("How many times has this class met so far this semester (not counting today)?"))

Total = (Length*Days*Weeks)-(Length*Number) #This is the calculation which uses the numbers entered.

print("")
print("Congratulations! You only have ", Total, " hours of class left!")
