def FillCranes():
    cranes = [0] * 5
    one_crane = int()

    for index in range(0, 5):
        #ask the user for one week
        one_crane = int(input("Enter cranes observed:  "))
        cranes[index] = one_crane
    #end for

def CalcTotal(cranes):
    total = int()
    #one_crane = int()

    #calculating the total
    for index in range(0, len(cranes)):
        cranes[index]=one_crane
        total = total + one_crane
    #end for

    #print out total
    print("Total number of cranes observed:  ", total)

def main():
    cranes = [0] * 5
    total = float()

    FillCranes()
    total = CalcTotal(cranes)

    print("Total number of cranes observed:  ", total)

main()