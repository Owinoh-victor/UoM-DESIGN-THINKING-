#Demo on working with Lists, Functions, returning multiple values


#out here I am in Global Land
def PrintLists(scores, worth):
    #In here I am a local variable
    for index in range(len(scores)):
        print(scores[index], "\t", worth[index])

    #end for

    return #not necessary since this function returns nothing

def CreatePercents(scores, worth):
    #local variables to CreatePercents
    percent = float()

    print()
    #print a heading
    print("Percents Earned")
    print("***************")

    for index in range(len(scores)):
        percent = scores[index]/worth[index]
        print(format(percent, '.2%'))

    return

def ReturnTotals(scores, worth):
    #local Variables
    total_scores = float()
    total_worth = float()

    total_scores = sum(scores)
    total_worth = sum(worth)

    return total_scores, total_worth

def FindHighest(scores):
    #local variable
    highest_value = float()
    highest_index = int()

    highest_value = max(scores)
    highest_index = scores.index(highest_value)

    print()
    print("The highest score is:\t", highest_value)
    print("Found at:\t", highest_index)

    return

def main():
    #create 2 lists, one will hold test scores and the other will hold
    #the number of points they are worth.
    scores = [10, 32.5, 8, 45, 5]
    worth = [10, 35, 10, 50, 5]

    totalW = float()
    totalS = float()
    totalA = float()

    #Call function to print both lists
    PrintLists(scores, worth)
    #Call the CreatePercents function
    CreatePercents(scores, worth)
    #Call and return Totals
    totalS, totalW = ReturnTotals(scores, worth)
    totalA = totalS/totalW

    print()
    print("Total Scores:\t", totalS)
    print("Total Worth:\t", totalW)
    print("Total Average:\t", format(totalA, '.2%'))

    #Call to Find Highest
    FindHighest(scores)




main()
