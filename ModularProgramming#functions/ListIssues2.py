#Some issues with the list datatype
#Reminder lists are considered by reference passes

def main():
    fruits = ["pear", "kiwi", "melon", "orange", "apple"]#defines the list
    index = int()
    #Printing out the list before it is sorted
    print("Before being sorted")
    PrintList(fruits) #Function call, will not return a value

    mylist = [" "] * len(fruits)

    #making a copy of fruits
    for index in range(0, len(fruits)):
        mylist[index] = fruits[index]

    #now sort
    SortList(mylist)    

    #Sorting the list
    SortList(fruits)

    #Print out the list after being sorted to show the bug
    print("Printing the list after being sorted showing our issue")
    PrintList(fruits)

def SortList(a_list):
    a_list.sort() #sorts the list

    print("After being sorted while inside SortList")
    PrintList(a_list)    

def PrintList(a_list):
    #local variables
    index = int()
    onefruit = str()

    for index in range(0, len(a_list)):
        onefruit = a_list[index]
        print(index + 1, "\t", onefruit)

    print()

    return


main()
