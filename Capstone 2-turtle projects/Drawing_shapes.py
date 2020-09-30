# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 18:19:00 2020

@author: pc


#****************************************************************************************
#FIRST PART OF ASSIGNMENT BEGINS HERE
#******************************************************************************************
import turtle

# Declare variables
pen_color = str()
fill_color = str()
pen_size = int()

#Moving the pen
turtle.penup()
turtle.goto(0, 150)
turtle.pendown()

#User select the pen size and color
pen_size= int(input("Please Write the pen size you desire to use (Whole Number between 1-10): "))
pen_color= str(input("Please Choose the pen color as either (red, blue or yellow): "))

#Fill color decision structure
if pen_color =="red":
    fill_color="yellow"
    
elif pen_color=="blue":
    fill_color="red"
    
else:
    fill_color="green"

# Drawing
turtle.pensize(pen_size)
turtle.pencolor(pen_color)
turtle.fillcolor(fill_color)

#turning ON nad Off the fill color
turtle.begin_fill()
#draw circle
turtle.circle(50)
#stopping the fill
turtle.end_fill()

#===================================================================================================================================
#Moving the pen to new position for drawing square
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
# user input
pen_color= str(input("Please Choose the pen color for the next shape as either (red, blue or Yellow): "))
turtle.pencolor(pen_color)
# Fill color decision structure
if pen_color == "red":
    fill_color = "yellow"

elif pen_color == "blue":
    fill_color = "red"
else:
    fill_color="green"
# Drawing settings
turtle.fillcolor(fill_color)
turtle.begin_fill()
#square
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
#end fill
turtle.end_fill()

#new position
turtle.penup()
turtle.goto(0, 50)
turtle.forward(100)
turtle.pendown()
#RECTANGLE*****************************************************************************************************
# user input
pen_color= str(input("Please Choose the pen color for the next shape as either (red, blue or Yellow): "))
turtle.pencolor(pen_color)
# Fill color decision structure
if pen_color == "red":
    fill_color = "yellow"

elif pen_color == "blue":
    fill_color = "red"
else:
    fill_color="green"
# Drawing settings
turtle.fillcolor(fill_color)
turtle.begin_fill()
#rectangle
turtle.right(35)
turtle.forward(125)
turtle.right(235)
turtle.forward(150)
turtle.left(127)
turtle.forward(130)
#end fill
turtle.end_fill()
turtle.done()
"""
#****************************************************************************************
#FIRST PART OF ASSIGNMENT ENDS HERE ...UNCOMMENT TO TEST IT
#******************************************************************************************

#****************************************************************************************
#SECOND PART OF ASSIGNMENT BEGINS HERE||||| ON MY OWN
#******************************************************************************************
import turtle
import time
#sets up the size of the window
turtle.setup(600, 600)
# Declare variables
pen_color = str()
fill_color = str()
pen_size = int()
shape=str()
location=str()
# user input
shape= str(input("Which shape do you want to draw(either a circle or a square): "))
if shape=="circle":
    pen_color = str(input("Please Choose the pen color as either (red, blue or Yellow): "))
    # Fill color decision structure
    if pen_color == "red":
        fill_color = "lime"
    elif pen_color == "blue":
        fill_color = "magenta"
    else:
        fill_color = "cyan"

else:
    fill_color = str(input("Please Choose the fill color as either (red, blue or yellow): "))
    # pen color selection structure for square
    if fill_color == "red":
        pen_color = "lime"
    elif fill_color == "blue":
        pen_color = "magenta"
    else:
        pen_color = "cyan"
#User input location
location= str(input("Please Choose the location for your shape as either (TL, TR, BL or BR): "))
#Decision structure for Location of shape to be drawn
if location=="TR":
    pen_size=3
    turtle.penup()
    turtle.goto(150, 180)
    turtle.pendown()
elif location=="TL":
    pen_size=5
    turtle.penup()
    turtle.goto(-150, 180)
    turtle.pendown()
elif location=="BR":
    pen_size=7
    turtle.penup()
    turtle.goto(150, -180)
    turtle.pendown()
else:
    pen_size = 9
    turtle.penup()
    turtle.goto(-150, -180)
    turtle.pendown()

# variable assignment to the user input values
turtle.fillcolor(fill_color)
turtle.pensize(pen_size)
turtle.pencolor(pen_color)

#SELECTION STRUCTURE TO DRAWING THE SHAPES
if shape=="circle":
    # Drawing circle
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    time.sleep(3)
    turtle.reset()

else:
# Drawing a square square instead
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()
    turtle.done()
    time.sleep(3)
    turtle.reset()





