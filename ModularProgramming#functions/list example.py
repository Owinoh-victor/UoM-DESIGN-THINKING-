#Global Variables
quantities = [17, 25, 3, 11, 100, 6]
#print quantities in Global namespace
print('quantities in Global Namespace')
for i in range(0, len(quantities)):
    print(quantities[i])    

def SortQuantities():
    quantities.sort()
    #print quantities in SortQuantities
    print('quantities in SortQuantities')
    for i in range(0, len(quantities)):
        print(quantities[i])

def main():
    #printing quantities before call to SortQuantities
    print('quantities before the function call in main')
    for i in range(0, len(quantities)):
        print(quantities[i])    
    #Calling SortQuantities
    SortQuantities()
    #printing after the function call
    print('quantities after the function call in main')
    for i in range(0, len(quantities)):
        print(quantities[i])    
    #Reversing the order of quantities
    quantities.reverse()
    #printing after the reverse
    print('quantities after the reverse in main')
    for i in range(0, len(quantities)):
        print(quantities[i])

main()
print('quantities in global after all calls')
for i in range(0, len(quantities)):
    print(quantities[i])    


    
