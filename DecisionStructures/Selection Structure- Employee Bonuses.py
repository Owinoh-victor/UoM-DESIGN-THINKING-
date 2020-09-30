#This program will determine employee bonuses based on the amount cars sold using Selection structeres.

#Declare Variables
EmployeeNames = ""
CarsSold = 0
Bonus = 0

#Statement explaining the purpose of the program to the user
print("This program will determine the bonus of an employee depending on the amount of cars sold in a month")
print()

#Ask for the employee name and for the amount of cars sold
EmployeeName = input("Enter the employee's name: ")
CarsSold = int(input("Enter the amount of cars sold: "))

#if ifel, else statements to determine the bonus
if CarsSold >= 0 and CarsSold <= 5:
    Bonus = 0
    print("Sorry ",EmployeeName,", you have not sold enough cars this month to receive a bonus")
elif CarsSold >= 6 and CarsSold <= 10:
    Bonus = 200
elif CarsSold >= 11 and CarsSold <= 15:
    Bonus = 500
else:
    Bonus = 1000

#Print out statement displaying employee name and his/her bonus if more than five cars where sold
if CarsSold > 5:
    print()
    print("Congratulations ",EmployeeName,"!", " You sold ",CarsSold," cars."," Your bonus is $",Bonus)


