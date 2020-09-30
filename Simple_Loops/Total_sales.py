# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 09:33:24 2020

@author: pc
"""

#variable declarations
weeks=int()
sales=float()
total_sales=0
average=0
count=1

#input1
weeks = int(input("Enter the total week of sales:"))

#Loop code
while count <= weeks:
    sales = float(input("Enter sales: "))
    count=count + 1
    total_sales= total_sales + sales77
    average=total_sales/weeks
#end loop

#print total sales
print(total_sales)

#print average
print(average)