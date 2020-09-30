#This program shows the various operations/functions that can be done with lists

#Declare and fill FriendsNames list
FriendNames = ["Matt", "Mary", "Jacob", "Sue"]

#print FriendsNames
print("List in original order")
for name in FriendNames:
    print(name)
print()
#Sorting (ascending)
print("List sorted in ascending order")
FriendNames.sort()
for name in FriendNames:
    print(name)
print()
#Sorting (descending)
print("List sorted in descendign order")
FriendNames.reverse()
for name in FriendNames:
    print(name)
print()
#Tells us where in the list Sue resides
print("Where does Sue reside in our list")
print(FriendNames.index("Sue"))
print()
#Adds Beth to the list
print("Adding Beth to the list")
FriendNames.append("Beth")
for name in FriendNames:
    print(name)
print()
#Removes Matt from the list
print("Removing Matt from our list")
FriendNames.remove("Matt")
for name in FriendNames:
    print(name)
print()
#Inserting Tim as the number 2 person
print("Inserting Tim as the second spot")
FriendNames.insert(1,"Tim")
for name in FriendNames:
    print(name)
print()
#How big is our list
print("Our list containts:  ", len(FriendNames), " items.")
#Looking for a friend
Name = input("Enter the name of a friend:  ")
if Name in FriendNames:
    print("We found your friend")
else:
    print("Sorry we did not find your friend")
    
        



