#decalire variables
answer = str()
num_cookies = int()
rate = float()
discount = float()
subtotal = float()
total = float()


while answer != 'quit':
     num_cookies = int(input("Enter the number of cookies:  "))
     if num_cookies <= 6:
          rate = 0.0
     elif num_cookies <= 12:
          rate = 0.5
     elif num_cookies <= 24:
          rate = 0.1
     else:
          rate = 0.2
     #determining the subtotal
     subtotal = num_cookies * 0.5
     #determining the discount
     discount = subtotal * rate
     #determining the total
     total = subtotal - discount
     #print out subtotal, discount and total
     print("Subtotal:  $", subtotal)
     print("Discount:  $", discount)
     print("Total:  $", total)
     #ask the user if they want to enter another batch
     answer = input("Enter 'quit' to end the program:  ")