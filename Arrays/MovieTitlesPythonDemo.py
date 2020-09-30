#This program will collect from the user a list of their favorite Movies
#Declare Variables
MovieNum = 0
Title = "nothing"
Index = 0

#Ask user for the number of movies
MovieNum = int(input("Enter the number of titles you wish to add to your list"))

#Declare array now that we know how many items are in it
Movies = [0] * MovieNum

while Index < MovieNum:
    Title = input("Enter a movie title:  ")
    Movies[Index] = Title
    Index = Index + 1

#Reset Index so that we can use it again
Index = 0

#Print out the list
while Index < MovieNum:
    Title = Movies[Index]
    print(Index + 1, ".  ", Title)



