#This program will ask you for your 5 favorite movies
#Declare variables
MovieTitle = "nothing"
count = int()
nummovies = int()
#setting up count
count = 1
#Ask the user for the number of movice they want to list
nummovies = int(input("Enter the number of movies you want for your list:  "))

#Ask the user for their movie title
while count <= nummovies:
    MovieTitle = input("Please enter a Movie Title:  ")
    print(count, ":  ", MovieTitle)
    count = count + 1

print("All Done")
