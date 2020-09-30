#Create a program that will keep track of the number of tokens won in a game.
#The program will ask the user for the number of tokens after 7 games and print
#those values to the screen.  It will also determine the total number of tokens
#and the average.  Finally the program will determine what is the highest token
#and lowest token.

#Declare Variables
tokens = [0,0,0,0,0,0,0] #declares the list to hold 7 items
tokens = [0] * 7 #Another way to declare the list
index = int()
total_tokens = int()
avg_tokens = int()
highest_token = int()
lowest_token = int()
one_token = int()
min_token = int()
max_token = int()

#Load up the tokens list
##for index in range(0, 7):
##    one_token = int(input("Enter the number of tokens you won:  "))
##    tokens[index] = one_token
###end for

#This is how we load a list without a loop
tokens = [10, 20, 30, 40, 50, 60, 70]

#Print out tokens list
for index in range(0, 7):
    one_token = tokens[index]
    print("Tokens won in game ", index + 1, one_token)
    #index + 1 takes into consideration that the indexes in Python
    #start at 0
#end for
#Figuring out the total number of tokens both ways
for index in range(0, 7):
    one_token = tokens[index]
    total_tokens = total_tokens + one_token
#end for

#Here is the second way
total_tokens = sum(tokens)

#print out the total number of tokens
print("The total number of tokens you have won:  ", total_tokens)

#Two ways to determine the average
#method 1
avg_tokens = total_tokens/7

avg_tokens = sum(tokens)/len(tokens)
#method 2
#avg_tokens = avg(tokens)
print(avg_tokens)

min_token = min(tokens)

print("The lowest number of tokens collected:  ", min_token)

max_token = max(tokens)

print("The highest number of tokens collected:  ", max_token) 

















