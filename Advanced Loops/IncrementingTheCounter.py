#This program will demonstrate the use of incremented counters
#and the ability to format using tabs
#Declare variables
Square = 0

print("Number\tSquare")
print("---------------------")
    
for num in range(1,20,2):
    Square = num**2
    print(num, '\t', Square)
    
    
