import turtle
import time

def drawHouse(turtle):

    turtle.penup()
    turtle.goto(-160, -20)
    turtle.pendown()
    turtle.setheading(90)
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.forward(150)
    roof1 = turtle.position()
    turtle.right(90)
    turtle.forward(300)
    roof2 = turtle.position()
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.end_fill()

    # roof
    turtle.penup()
    turtle.goto(roof1)
    turtle.fillcolor("maroon")
    turtle.begin_fill()
    turtle.pendown()
    turtle.goto(-10, 200)
    turtle.goto(roof2)
    turtle.goto(roof1)
    turtle.end_fill()
    turtle.setheading(90)

def DrawDoor(turtle, x, y):
        # door
        turtle.penup()
        turtle.goto(x, y)
        turtle.fillcolor("maroon")
        turtle.begin_fill()
        turtle.setheading(90)

        for x in range(2):
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(30)
            turtle.right(90)

        turtle.end_fill()

        # handle
        turtle.fillcolor("black")
        turtle.penup()
        turtle.goto(x, y + 20)
        turtle.begin_fill()
        turtle.circle(4)
        turtle.end_fill()

        turtle.write('Working From Home', move=False, align="left", font=(" arial", 16, "bold"))
        time.sleep(3)
        turtle.clear()

""""
**********************Turtle Making some art work****************

"""
def MakeArt(colors,pen_size,bg):
    turtle.bgcolor(bg)
    turtle.speed(20)
    turtle.pensize(pen_size)

    turtle.pendown()
    n = -1
 #Nested Loop for drawing a pattern of circles
    for angle in range(0, 360, 15):
        n = n + 1
        if n == 5:
            n = -1
        turtle.pencolor(colors[n])
        turtle.seth(angle)
        turtle.circle(100)

    turtle.penup()
    turtle.setpos(150, -270)
    turtle.pendown()
    turtle.pencolor('olive')
    turtle.write('Beautiful Art', move=False, align="left", font=(" arial", 16, "bold"))
    time.sleep(4)




def main():

    #  Settings  up my  turtle builder
    turtle.title("TURTLE ACTIVITIES DURING GUARANTINE PERIOD ")
    turtle.speed(100)
    turtle.setup(800, 600)
    turtle.bgcolor('green')
    colors = ["red", "blue", "yellow", "white","olive"]
    pen_size=int(input("Enter PenSize:"))
    bg=str(input("Choose BG color for Making Art  as black or green: "))



    #function calls
    drawHouse(turtle)
    DrawDoor(turtle, -25, -20, )
    MakeArt(colors,pen_size,bg)


main()