import turtle
import time

# Boundary  lines /rectangle
# You need a colon
def boundary():
    turtle.penup()
    turtle.goto(-140, 195)
    turtle.pendown()
    turtle.goto(140, 195)
    turtle.goto(140, -195)
    turtle.goto(-140, -195)
    turtle.goto(-140, 195)

# Penalty Box - Top
def penaltyTop():
    turtle.penup()
    # You forgot a comma
    turtle.goto(0, 115)
    turtle.pendown()
    turtle.circle(40)

    turtle.penup()
    turtle.goto(-80, 195)
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.goto(80, 195)
    turtle.goto(80, 140)
    turtle.goto(-80, 140)
    turtle.goto(-80, 195)
    turtle.end_fill()
# Penalty Box - Bottom
def penaltyBottom():
    turtle.penup()
    turtle.goto(0, -195)
    turtle.pendown()
    turtle.circle(40)

    turtle.penup()
    turtle.goto(-80, -195)
    turtle.pendown()
    # You need apostrophes here
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.goto(80, -195)
    turtle.goto(80, -140)
    turtle.goto(-80, -140)
    turtle.goto(-80, -195)
    turtle.end_fill()

# Goal Box - Bottom
def goalBottom():
    turtle.penup()
    turtle.goto(40, -195)
    turtle.pendown()
    turtle.goto(40, -170)
    turtle.goto(-40, -170)
    turtle.goto(-40, -195)

# Goal Box - Top
def goalTop():
    turtle.penup()
    turtle.goto(40, 195)
    turtle.pendown()
    turtle.goto(40, 170)
    turtle.goto(-40, 170)
    turtle.goto(-40, 195)
# Semicolon rather than a colon
def midPitch():
    # Mid pitch Line
    turtle.penup()
    turtle.goto(-140, 0)
    turtle.pendown()
    turtle.goto(140, 0)
# mid pitch Central Circle
    turtle.penup()
    turtle.goto(0, -40)
    turtle.pendown()
    turtle.circle(40)

def main():
    # set title
    turtle.title("FLY EMIRATES : GUNNERS FOREVER!!!")
    # setting our window bg color and size
    turtle.setup(500, 600)
    turtle.bgcolor('green')
    # variables
    pensize = int()
    pencolor = str()
    turtle.pensize(4)
    turtle.pencolor("white")
    # my function calls in the main()
    # You don't need a colon here
    boundary()
    penaltyTop()
    penaltyBottom()
    goalBottom()
    goalTop()
    midPitch()

#calling all the functions using the main functions
main()
time.sleep(5)
