# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:11:15 2020
https://online.macomb.edu/courses/37557
@author: pc
"""

import turtle
#set title
turtle.title("My First Turtle Graphics")
#setting our window bg color and size
turtle.setup(800, 500)
turtle.bgcolor('maroon')
#giving a custom color, speed  and shape to our turtle
turtle.shape('circle')
turtle.fillcolor('green')
turtle.speed(2)
#customizing the pen traces
turtle.pensize('10')
turtle.pencolor('white')
#On Your Mark!! set!1 Go!! This is the start of our walk
turtle.write('Starting Our Walk')
#retracing  steps
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
#signaling a wrong direction and making a turn to the 0,0 position without trace
turtle.write('OPPS!!Wrong Direction')
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
 #Moving to the left side
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.write('CONGRATULATIONS!! ITS ALL DONE')
