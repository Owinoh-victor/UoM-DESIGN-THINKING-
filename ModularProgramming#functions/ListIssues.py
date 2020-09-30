#Some issues with the list datatype

def PrintList(someList):
    #local variables to PrintList
    index = int()

    #print out the list using a for loop
    for index in range(0, len(someList)):
        print(index +1, "\t", someList[index])

    print()    

def SortIssueFixed(a_list):
    newlist = [" "] * len(a_list)

    for index in range(0, len(a_list)):
        newlist[index] = a_list[index]
        
    newlist.sort()

    #print newList
    PrintList(newlist)  
    
def main():
    #local variables to main
    fruitsNveggies = ["carrot", "apple", "pear", "broccoli", "green beans"]
    
    #print a small header
    print("My List as declared")
    PrintList(fruitsNveggies)

    #Fixing the problem
    SortIssueFixed(fruitsNveggies)
    PrintList(fruitsNveggies)
    
main()
