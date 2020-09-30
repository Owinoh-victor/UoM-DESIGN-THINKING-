#This program will calculate the weekly salary by summing up the hours worked each day and multiplying it
#   by the employee wage.

#Declare variables
EmployeeName = ""
DailyHours = 0.00
WeeklyHours = 0.00
Wage = 0.00
WeeklySalary = 0.00
NumberDaysWorked = 0
Count = 0

#Ask for name, wage, days worked, and the daily hours worked in the week.
EmployeeName = input("Enter the employee's name: ")
Wage = float(input("Enter the employee's wage: "))
NumberDaysWorked = float(input("Enter the number of days the employee worked this week: "))


#Loop to accumulate the number of hours worked for a certain number of days in a week
while Count < NumberDaysWorked:
    DailyHours = float(input("Enter the amount of daily hours worked: "))    
    WeeklyHours = WeeklyHours + DailyHours
    Count = Count + 1
    

#Calculate weekly salary
WeeklySalary = WeeklyHours * Wage

#Ouput employee name and weekly salary
print(EmployeeName,"'s wage: $",Wage)
print(EmployeeName+" worked ",WeeklyHours," hours this week.")
print(EmployeeName,"'s weekly salary is $",WeeklySalary)

                       

