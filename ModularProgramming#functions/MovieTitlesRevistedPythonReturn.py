#Movie Titles Revisited
#This program asks the user for the number of movies they want on their list
#and then adds those movies to the list.  It also prints out the movies on
#the list.
#Written by:  Betsy Jenaway
#Dated:  August 3, 2012


def main():
    #Declare variables
    MovieNum = 0
    Movies = []
    #Get Number of movies
    MovieNum = GetNumber()
    #Get Movie Titles
    Movies = GetTitles(MovieNum)
    #Print Movie Titles
    PrintList(Movies, MovieNum)
    
#Get the number of movies from the user
def GetNumber():
    #Declare local variables
    flag = False
    UserNumber = 0
    stringnumber = str()
    #Ask the user for the number and validate it
    stringnumber = input("Enter the number of titles you wish to add to your list:   ")
    while flag == False:
        if stringnumber.isdigit():
            UserNumber = int(stringnumber)
            if UserNumber > 0:
                flag = True
            else:
                flag = False
                stringnumber = input("Sorry you need to enter a number.  Please try again:  ")
        else:
            flag = False
            stringnumber = input("Sorry you need to enter a number greater than 0.  Please try again:   ")
            
    return UserNumber

#Fill the Movies list with the favorite movies
def GetTitles(NumList):
    #Declare Local Variables
    Index = 0
    Title = "nothing"
    Values = [] #Declares an open array to return back
    #Loop to fill the Movies array
    for Index in range(0, NumList):
        Title = input("Enter a movie title:   ")
        Values.append(Title)

    return Values

#Print out the movie list
def PrintList(Movies, MovieNum):
    Index = 0
    for Index in range(0, MovieNum):
        print(Movies[Index])
main()
