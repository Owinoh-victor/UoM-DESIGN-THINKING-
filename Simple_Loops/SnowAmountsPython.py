##Create a program that will allow us to keep track of how much snow we have on the ground.  
##The program will ask the user for the month and then how much snow has fallen.  It will
##also ask the user for how much snow has melted.  The program will calculate the amount of
##snow still on the ground, how much snow has fallen in total and how much snow has melted 
##in total.  The program will end when the user is done entering snow values.
##
##inputs:  snow that has fallen, month, snow melted, User Answer
##outputs:  Total snow on the ground, Total snow melted, Total snow fall
##
##30,000 foot view
##********************************
##Declare Variables
##do until UserAnswer = "no"
##	Ask user for month, melted and fallen
##	Calculate total melted, fallen and amount on the ground
##	display total melted, fallen and amount on the ground
##	Ask user if they wish to continue
##end loop

#Declare Variables
month = str()
melted = float()
fallen = float()
TotalFallen = float()
TotalMelted = float()
OnGround = float()
UserAnswer = "yes"

while UserAnswer == "yes":
    #Ask user for month, melted and fallen
    month = input("Enter the month:  ")
    fallen = float(input("Enter the amount of snow that fell this month:  "))
    melted = float(input("Enter the amount of snow that melted this month:  "))
    #Calculate total melted, fallen and amount on the ground
    TotalMelted = TotalMelted + melted
    TotalFallen = TotalFallen + fallen
    OnGround = OnGround + fallen - melted
    #Display total melted, fallen and amount on the ground
    print("Total amount of snow that has fallen:  ", TotalFallen)
    print("Total amount of snow that has melted:  ", TotalMelted)
    print("Snow still on the ground:  ", OnGround)
    #Ask the user if they wish to continue
    UserAnswer = input("Do you want to enter another month's worth of snow?  Enter yes or no :  ")
#End loop
