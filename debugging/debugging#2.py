# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 09:33:24 2020

@author: Bassam Ton
"""
#Declaire variables
initial_amount=(float)
time=int()
compound_rate=float()
Time=float()
compounded=int() # monthly=1; bi-annually=2 : annually=12; e.t.c
amount=0

#constant  rate variable
rate=5/100

#User input  the Initial amount
initial_amount = int(input("Enter the Principle Investment Amount: $"))

#input validation
if initial_amount<500:
    print ("Amount too small for an investment, please adjust the amount.")

else:
    #the user inputs the investment period
    time = int(input("Enter the period of Investment (Years): "))
    compounded=int(input(" How many times is the interest compounded: "))
#Input and validation ends here
# ---------------------------------

#Loop to calculate the compounded interest
    for i in range (time):
        compound_rate= 1 + (rate/compounded)
        Time=compounded * time # this is the time of compounding the interest
        amount=initial_amount * (compound_rate**Time)
        total_interest=amount-initial_amount


#output
        print("******************* INVESTMENT  ***  SUMMARY   **************************")
        print ("Your Principle Investment is:\t\t\t$", initial_amount)
        print("For an Investment period of:\t\t\t", time,"Years")
        print("Interest is compounded :\t\t\t",compounded," times per time period")
        print("\t\t\t\t\t\t*********************************")
        print("Interest earned for the investment period is:\t\t $", total_interest)
        print("The investment balance after", time ,"years is:\t\t  $", amount)


