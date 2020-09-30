#Week 2 Demo
#Written by:  Prof. Jenaway
#Date:  8/27/2013

#This program will tell us how much time we need to spend on Homework this term

#Declare Variables
##Name = "nothing"
##CreditHours = 0
##TimeSpent = 0.0
##StudyTime = 2.0  #This is a constant

#Another way to declare
Name = str()  #" "
CreditHours = int() #0
TimeSpent = float() #0.0
StudyTime = 2  #This is a constant 

#Get name and credit hours from the use
Name = input("What is your name?    ")
CreditHours = input("How many credit hours are you taking this term?   ")

#Determine number of hours needed for homework each week
TimeSpent = CreditHours * StudyTime

print(Name, "you will need to spend ", TimeSpent, " hours doing homework this term.")
