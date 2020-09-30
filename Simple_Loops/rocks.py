#Declare variables
rocks = int() 
totalrocks = int()
rockcounter = int()
while rockcounter <= 10:
    print(rockcounter)
    rocks = int(input("Enter the number of rocks collected:  "))
    totalrocks = totalrocks + rocks
    rockcounter = rockcounter + 1
