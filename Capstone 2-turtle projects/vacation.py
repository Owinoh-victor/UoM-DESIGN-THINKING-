import turtle
import time

def climbing(pensize, pencolor ):
    turtle.shape("turtle")
    turtle.pensize('4')
    turtle.pencolor('maroon')

    # On Your Mark!! set!1 Go!! This is the start of our walk
    for i in range (0, 4):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
    turtle.forward(50)
    turtle.write("Hurray! Made it to the top!")
    time.sleep(3)

def swimming(pensize, pencolor):
    turtle.reset()
    turtle.shape("triangle")
    turtle.pensize('4')
    turtle.pencolor('blue')
    turtle.fillcolor('blue')
    #-moving to the upper left quandrant of your screen
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    #----------------------------
    # Drawing the  pond
    turtle.begin_fill()
    turtle.circle(70)
    turtle.end_fill()
    #---------------------------
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
    turtle.shape("turtle")
    turtle.pensize('4')
    turtle.pencolor('maroon')
    #-------------------------
    # Drawing the path around the pond
    turtle.circle(100)
    #-going swimming------------
    turtle.pencolor('blue')
    turtle.fillcolor('green')
    turtle.left(90)
    turtle.forward(60)
    turtle.pencolor('black')
    turtle.write('Yeah! I’m swimming!', move=False, align="left", font=(" arial", 20, "bold"))
    time.sleep(3)

#----------------------
def eating():
    turtle.reset()
    # variables
    colors = ["red", "blue", "maroon", "green"]
    # location
    turtle.penup()
    turtle.goto(-200, -100)
    turtle.pendown()
    turtle.pensize('4')
    turtle.shape("turtle")

    # draw circles (food)
    for count in range(0, 4):
        turtle.fillcolor(colors[count])
        turtle.pencolor(colors[count])
        turtle.begin_fill()
        turtle.circle(25)
        turtle.penup()
        turtle.forward(25)
        turtle.pendown()
        turtle.end_fill()

        #--------------- moving to the first circle
    turtle.penup()
    turtle.goto(-200, -100)
    turtle.pendown()
    time.sleep(3)
        #--------------------
    # loop to to show turtle eating the food
    for count in range(0, 4):
        turtle.fillcolor("white")
        turtle.pencolor("white")
        turtle.begin_fill()
        # draw circles (food)
        turtle.circle(25)
        turtle.penup()
        turtle.forward(25)
        turtle.pendown()
        turtle.end_fill()
        time.sleep(3)
    turtle.pencolor('black')
    turtle.write("wow! what a great meal!", move=False, align="left", font=(" arial", 20, "bold"))
    turtle.fillcolor('green')
    time.sleep(3)


def sleeping():
    turtle.reset()
    # moving to lower right quadrant of your screen
    turtle.penup()
    turtle.goto(200, -100)
    turtle.pendown()

    turtle.shape("turtle")
    turtle.pensize('4')

    turtle.begin_fill()
    for i in range(0, 4):
        turtle.pencolor('maroon')
        turtle.fillcolor("maroon")
        turtle.forward(150)
        turtle.left(90)
    turtle.end_fill()
    # ------------------
    # moving to pillow position
    # ---------------------
    turtle.penup()
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.pencolor('white')
        turtle.fillcolor("white")
        turtle.forward(20)
        turtle.left(90)
    turtle.end_fill()
    turtle.fillcolor("green")
    turtle.pencolor('black')
    turtle.write('Good Night!', move=False, align="left", font=(" arial", 16, "bold"))
    time.sleep(3)
#----------------------
#Main functionpy
#----------------------------
def main():
    #set title
    turtle.title("Going on A Vacation")
    # setting our window bg color and size
    turtle.setup(800, 600)
    # variables
    pensize = int()
    pencolor = str()

    #function calls
    climbing(pensize, pencolor)
    swimming(pensize, pencolor)
    eating()
    sleeping()
#calling the main function
main()

