#Random Number Sort Program
#Written by:  Betsy Jenaway
#Date:  July 31, 2012

#This program will populate an array with 4 random numbers.  It will then
#sort those numbers in descending and ascending order.

#import the Random Library
import random

#Declare Variables
RandomArray = [0,0,0,0]
RandomNumber = 0
Index = 0

#Load the array
print("Here is your unsorted list of random numbers")
print("============================================")
for Index in range(4):
    RandomNumber = random.randint(1, 10)
    RandomArray[Index] = RandomNumber
    print("\t\t\t", RandomNumber)

#Sort the array in ascending order and print it out
RandomArray.sort()
Index = 0
print("Here is your list sorted in ascending order")
print("============================================")
for Index in range(4):
    print("\t\t\t", RandomArray[Index])

#Sort the array in descending order and print it out
RandomArray.reverse()
Index = 0
print("Here is your list sorted in descending order")
print("============================================")
for Index in range(4):
    print("\t\t\t", RandomArray[Index])


    
