#Program to draw chessboard in Python Turtle
import turtle
chessboard = turtle.Turtle()
chessboard.speed(8) #for speedily drawing chessboard
for i in range(4): #for loop will run 4 times
    chessboard.forward(800) #forward turtle by 800 units
    chessboard.right(90) #turn turtle clockwise by 90 degree
a = 0 #for controlling alternate colors in a row
b = 0 #for controlling alternate colors in a column
for i in range(8): #for loop will run 8 times as there are 8 rows in the chessboard
    if(b == 0):
        a=1
    else:
        a=0
    for j in range(8): #for loop will run 8 times as there are 8 columns in the chessboard
        chessboard.penup()
        chessboard.goto(j*100, i*100*(-1))
        chessboard.pendown()
        if(a==0):
            chessboard.fillcolor('black')
            a=1
        else:
            chessboard.fillcolor('white')
            a=0
        chessboard.begin_fill()
        for k in range(4):
            chessboard.forward(100)
            chessboard.right(90)
        chessboard.end_fill()
    if(b==0):
        b=1
    else:
        b=0