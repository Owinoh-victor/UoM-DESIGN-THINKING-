#Movie Titles Revisited
#This program asks the user for the number of movies they want on their list
#and then adds those movies to the list.  It also prints out the movies on
#the list.
#Written by:  Betsy Jenaway
#Dated:  August 3, 2012

#Declare Global Variables
MovieNum = 0
Movies = []

def main():
    #Bind Global Variables
    global MovieNum
    global Movies
    #Get Number of movies
    GetNumber()
    #Get Movie Titles
    GetTitles(MovieNum)
    #Print Movie Titles
    PrintList(Movies, MovieNum)
    
#Get the number of movies from the user
def GetNumber():
    #Binding Global Variables
    global MovieNum
    #Declare local variables
    flag = False
    StrMovieNum = "nothing"
    
    #Ask the user for the number and validate it
    StrMovieNum = input("Enter the number of titles you wish to add to your list:   ")
    while flag == False:
        if StrMovieNum.isdigit():
            MovieNum = int(StrMovieNum)
            if MovieNum > 0:
                flag = True
            else:
                flag = False
                StrMovieNum = input("Sorry you need to enter a number.  Please try again:  ")
        else:
            flag = False
            StrMovieNum = input("Sorry you need to enter a number greater than 0.  Please try again:   ")
      
#Fill the Movies list with the favorite movies
def GetTitles(NumList):
    #Binding Global Variables
    global Movies
    #Declare Local Variables
    Index = 0
    Title = "nothing"

    #Loop to fill the Movies array
    for Index in range(0, NumList):
        Title = input("Enter a movie title:   ")
        Movies.append(Title)

#Print out the movie list
def PrintList(Movies, MovieNum):
    Index = 0
    for Index in range(0, MovieNum):
        print(Movies[Index])
main()
