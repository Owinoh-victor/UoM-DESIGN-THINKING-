"""
inputs:
-----------------------------
rainfall for 2018
rainfall for  2019

outputs:
------------------------
difference in the amount of rainfall for the two years

Basically what is going on:
----------------------------------------
ask user for  rainfall input as long as it is in the range of the three months (june, july, august)
calculate the difference between the 2019 and 2018 rainfall

# Decomposition
--------------------------------------------------------------
variables
--------------
rain_2018 = float()
rain_2019 = float()
difference = float()
 user_input
 ----------------
 while month < 3:
 rain_2018:
 rain_2019:

calculate
---------
difference rain_2019 - rain_2018
_____________________
Nested loop and decision structure
-------------------------
    if difference < 0:
        print("2018 had more rain than 2019 by", difference, "inches.")
    elif difference > 0:
        print("2019 had more rain than 2018 by", difference, "inches.")
    else:
        print("No change.")
"""
# variables
rain_2018 = float()
rain_2019 = float()
difference = float()
# count for the three months of june, july and august
for month in range(0, 3):
    # ask user for input as long as it is in the range of the three months
    rain_2018 = float(input("Enter the rainfall for 2018:"))
    rain_2019 = float(input("Enter the rainfall for 2019:"))
    # calculating the difference
    difference = rain_2019 - rain_2018
    # Nested loop using if structure for output decision
    if difference < 0:
        print("2018 had more rain than 2019 by", difference, "inches .")
        print("*******************Next Month Rainfall *****************************")
    elif difference > 0:
        print("2019 had more rain than 2018 by", difference, "inches .")
        print("********************Next Month Rainfall****************************")
    else:
        print("No change.")
        print("********************   Next Month Rainfall *****************************")


