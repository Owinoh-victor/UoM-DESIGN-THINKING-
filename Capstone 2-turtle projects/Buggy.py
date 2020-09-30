#declare variables
breakfast = float()
lunch = float()
dinner = float()
total = float()

#ask user for calories
breakfast = float(input("Enter the calories consumed at breakfast:  "))  # all inputs are suppossed to be float
lunch = float(input("Enter the calories consumed at lunch:  ")) # missing parenthesis
dinner = float(input("Enter the calories consumed at dinner:  ")) # == is only used for assignment of logic operation not input

#Determine total calories
total = breakfast + lunch + dinner # bug 4 sum all

#print total
print("Total calories consumed today:  " , total)#bug 5 nocncatinate string