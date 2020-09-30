#This program will calculate the batting average for a baseball player.
##
##Inputs:  player name, jersey number, at bats, hits
##Outputs:  player name, jersey number, average
##Problem Statement:  this program will ask the user for the name and
              #jersey number, at bats and hits.  It will then determine
              #the batting average and display that to the user
##
##30,000 foot view
##1).  Ask user for name, jersey number, at bats, hits
##2).  Calculate the batting average (hits/at bats)
##3).  Display name, jersey number and average

#Declare variables
name = str()
jersey_num = str()
at_bats = int()
hits = int()
average = float()
##Ask user for name, jersey number, at bats, hits
name = input("Enter the name of the player:  ")
jersey_num = input("Enter the jersey number:  ")
at_bats = int(input("Enter the number of times this player has batted:  "))
hits = int(input("Enter the number of times this player hit the ball:  "))

##Calculate the batting average (hits/at bats)
average = hits/at_bats

##Display name, jersey number and average
print("Player Name:  ", name)
print("Player Jersey Number:  ", jersey_num)
print("Batting Average:  ", average)


