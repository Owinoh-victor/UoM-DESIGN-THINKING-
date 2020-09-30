#This program will determine the amount of discount based on the number of points a customer has earned and how long
# they have been a customer.
#==========================================
# inputs are
# 1. points
#2. Years of loyalty
#==================================================
# Decision is as follows
#
#if points<=50: discount=0
#elif points<100: discount= 10/100
# elif points<200: discount=20/100
#elif points< 300: discount= 25/100
# else: discount= 30/100
#Additional discount
#if years>=5: add_discount= 5/100
#else: add_discount=0
#===========================================
#Output is
# discount
#additional discount
#total discount
#==============================================



#declare variables
points=float()
years= int()
discount=float()
add_discount=float()
total_discount=float()

#user input
points=float(input("Please Enter the number of points you've Earned: "))
years=int(input("How many Years have you been A loyal Customer: "))

# Decision Structures

if points<=50:
    discount=0
elif points<100:
    discount= 10/100
elif points<200:
    discount=20/100
elif points< 300:
    discount= 25/100
else:
    discount= 30/100
#Additional discount
if years>=5:
    add_discount= 5/100
else:
    add_discount=0

#Total discount
total_discount = discount + add_discount


#Output
print('===========================================')
print("Discount is: ", discount)
print("Additional Discount is: ", add_discount)
print ("Total Discount is: ", total_discount)
