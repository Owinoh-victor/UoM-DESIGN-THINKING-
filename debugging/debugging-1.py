#------------------------------------------------------------------------------
#
#  Shungloon Wong
# Debugging #1: If Structures
#
#------------------------------------------------------------------------------

# Setting Variables
income = float()
bills = float()
groceries = float()
item = float()

print("Hi, this program will determine whether you're able to responsibly \  afford a new item or not")
#bug1: missing one quote to print a string value
print("If the item is 20% or more money than what you have currently \ after bills or groceries you cannot responsibly afford it.")

income = input('Enter your monthly income: ')

income = float(income)

bills = input('Enter how much you must pay for bills (utilities, rent, etc): ')

#NameError: bill not defined, I suppose to use bills in the parenthesis coz that is what is defined above
#bills = float(bill) this is the initial error code
bills = float(bills)

groceries = input('Enter how much you have spent on food: ')

groceries = float(groceries)

item = input('Please enter the cost of the item you wish to buy: ')

item = float(item)

# Calculations

money_left = income - bills - groceries

afforability = money_left - item
afforability = afforability / money_left * 100

# If you can afford the item or not
#bug2: missing the colon to terminate an if statement as a block
#bug3: logic error for the if structure. From your statement above, affordability should be >= 20% but the program has > alone
if afforability >= 20:
#bug4: missing quotation mark to print a string
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print( "Affordability is : ", afforability,"%")
    print("You can responsibly afford this item!")
# bug5: missing colon for else statement
else:
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print( "Affordability is : ", afforability,"%")
    print("You can not responsibly afford this item.")

# Apologies for adding unnecessary outputs on your code
#I wanted to see the logic in the percentage affordability, so I had to print it out and separate the input and output with the many xxx
# Your code runs pretty well after correcting the easily noticed errors highlighted by the comments as bug1 -5
# however, just out of curiosity, I noticed a logical error if my income is 100$(imaginary value),i spend 50 and 60 on bills and food
#Am supposed to have a (-ve) balance right? Besides, I wish to buy an item worth 20$... Logically reasoning, am not able to afford this Item
# But the program outputs 300% affordability, meaning I can afford this Item.
# How is this possible?? Maybe the tutor can also contribute to this because I also don't understand how is that possible.
