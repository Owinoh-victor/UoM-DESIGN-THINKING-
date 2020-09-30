#Playing with Lists
#1).  Declaring a list
#2).  Filling a list without a loop
#3).  Printing a list
#4).  Sorting a list

#Declare Variables
#Here is #1 and #2
markers = ["yellow", "blue", "red", "pink", "black", "green", "orange"]
onemarker = str()
index = int()


#Loading a list with a for statement
#for index in range(0, len(markers)): #len tells us how many elements in markers
    #onemarker = input("Enter a marker color: ")
    #markers[index] = onemarker
#end for

#Printing our list
print("Here is our list of markers")
print("***************************")
for index in range(0, len(markers)):
    onemarker = markers[index]
    print(onemarker)
    #print(markers[index])
#end for
print()

#Playing with the sorting
#First we're going to sort in descending order
#We are going to try to use the reverse method

markers.reverse()
print("Here is our list of markers")
print("***************************")
for index in range(0, len(markers)):
    onemarker = markers[index]
    print(onemarker)
print()
#Now we are going to really sort in descending order
markers.sort(reverse = True)
#Printing out the list
print("Here is our list of markers")
print("***************************")
for index in range(0, len(markers)):
    onemarker = markers[index]
    print(onemarker)

#First were going to sort in ascending order
markers.sort()
print()
#printing the new sorted list
print("Here is our list of markers")
print("***************************")
for index in range(0, len(markers)):
    onemarker = markers[index]
    print(onemarker)

















    



