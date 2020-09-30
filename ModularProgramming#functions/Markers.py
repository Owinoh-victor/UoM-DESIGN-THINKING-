#demo on lists and list method
#1).  Declaring and assigning values for a list
#2).  How to fill a list with a loop
#3).  How to print a list
#4).  Sorting lists
#5).  Other functions

#Declare Variables
#declaring and filling in one line
markers = ["pink", "yellow", "blue", "red", "green", "black", "orange"]
onemarker = str()
index = int()
testscores = [85, 81.5, 90, 87, 95.5]
onetestscore = float()
maxtestscore = float()
mintestscore = float()
maxindex = int()
minindex = int()

#However, what if we need to let the user fill our array?
#for index in range(0, len(markers)):  #tells us the number of items -- 7
    #onemarker = input("Enter a marker:  ")
    #markers[index] = onemarker
#end for

#print the list markers
print()
print("Your list of markers")
print("********************")
for index in range(0, len(markers)):
    onemarker = markers[index]
    print(onemarker)
    #print(marker[index])  #can also use this to print if you don't want the
#end for                   #extra variable

#Sort
#Sort markers in descending order
markers.reverse()##Be careful this just flips the order of your elements
print()
print("Your list of markers")
print("********************")
for index in range(0, len(markers)):
    onemarker = markers[index]
    print(onemarker)

#A better way to sort in reverse order
markers.sort(reverse = True)
print()
print("Your list of markers")
print("********************")
for index in range(0, len(markers)):
    onemarker = markers[index]
    print(onemarker)
#Now we are going to sort in ascending order
markers.sort()
print()
print("Your list of markers")
print("********************")
for index in range(0, len(markers)):
    onemarker = markers[index]
    print(onemarker)

#Switching gears and using the testscores list
#Finding the highest and lowest values and where they are in the list
maxtestscore = max(testscores)
mintestscore = min(testscores)
maxindex = testscores.index(maxtestscore)
minindex = testscores.index(mintestscore)

#printing them all out
print("The highest value in testscores =  ", maxtestscore)
print("The lowest value in testscores =  ", mintestscore)
print()
print("The highest value was found at index:  ", maxindex)
print("The lowest value was found at index:  ", minindex)

















    















    













    

