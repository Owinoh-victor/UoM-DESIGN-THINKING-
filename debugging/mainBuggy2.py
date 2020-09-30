# Shungloon Wong

# This program is just a basic restaurant with a small menu
# It will prompt you with a menu and draw the food (just circles with color)
# The program will ask you if you enjoyed the food and whether you'd like to come back
# The program will continue indefinitely until you decide to leave

# Importing 
import turtle

# functions to do the simple drawings
def chicken():
    turtle.clear()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(100)
    turtle.end_fill()
    turtle.time.sleep(2)
# a colon is missing at the end of the function
def steak():
    turtle.clear()
    turtle.color("brown")
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(100)
    turtle.end_fill()
    turtle.time.sleep(2)

def salmon():
    turtle.clear()
    # No need for double parenthesis
    turtle.color("pink")
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(100)
    turtle.end_fill()
    turtle.time.sleep(2)

def foodquality(food):
    price = int()
    satisfaction = str()
    if food == "steak":
        price = 12
    elif food == "chicken":
        price = 8
    else:
        price = 7
    print("Your total is", price, "dollars for", food)

def satisfactionTest(satisfaction):
    if satisfaction == "yes":
        print("Great, thank you for your patronage.")
    else:
        print("Sorry, we will try our best next time.")

# Main
def main():  #colon is needed
    # variables
    restaurant = str()

    while restaurant != "no":
        #variables
        inputFood = str()
        satisfaction = str()
        #input order
        inputFood = input("What would you like to eat? (Salmon, Chicken, Steak)").lower()
        #printing order
        print("You have ordered", inputFood)
        # if statement
        if inputFood == "salmon":
            salmon()
        elif inputFood == "steak":
            steak()
        else:
            chicken() #no need for colon in function call
        #end if

        # function call
        foodquality(inputFood) # no need for colon in function call

        satisfaction = input("Are you satisfied with your order?").lower()

        # function call
        satisfactionTest(satisfaction)

        restaurant = input("Would you like to come again? (Yes or No)").lower()

# calling main
main()