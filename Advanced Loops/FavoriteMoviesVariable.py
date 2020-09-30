#This program will ask you for your 5 favorite movies
#Declare variables
MovieTitle = "nothing"
MovieRanking = range(1,6)

#Ask the user for their movie title
for count in MovieRanking:
    MovieTitle = input("Please enter a Movie Title:  ")
    print(count, ":  ", MovieTitle)

print("All Done")
