#importing libraries
import random
import time
import turtle
#setting our window size
turtle.setup(600, 600)
#title
turtle.title("Drawing Random Circles")
#variables
horizontal = int()
radius = int()
colors = ["red", "blue", "yellow", "green"]
pen_size = int()

#initializing the location and size of the circles
horizontal = -200
radius = 25
pen_size = 2
#location
turtle.penup()
turtle.goto(horizontal, 0)
turtle.pendown()
#Initialize the pensize by typing in
turtle.pensize(5)
#loop to draw the circles
for count in range(0, 4):
    turtle.fillcolor(colors[count])
    turtle.pensize(pen_size)
    turtle.begin_fill()
    #draw circle
    turtle.circle(radius)
    #reset location, radius and pensize
    horizontal= horizontal + 75
    radius= radius + 20
    pen_size= pen_size + 2
    # moving the turtle
    turtle.penup()
    turtle.goto(horizontal, 0)
    turtle.pendown()
    turtle.end_fill()
time.sleep(3)


"""
************ Part 1 ends here*********************
Ready for more circles?
"""

turtle.reset()
#setting our window size
turtle.setup(600, 600)
#title
turtle.title("Drawing Random Circles")
#variables
turtle.write('Ready for more circles?', move=False, align="center", font=(" arial", 16, "bold"))
time.sleep(3)
#clear screen
turtle.clear()

#variables
radius = int()
colors = ["red", "blue", "yellow", "green"]
pen_size = int()

# random generation of variables
radius = random.randint(25,125)
pen_size = random.randint(0,10)
x = random.randint(-150,150)
y = random.randint(-150,150)
random_index = random.randint(0,3)

# loop for the choice selection within every iteration
for count in range(0, 20):
    turtle.pensize(pen_size)
    turtle.fillcolor(colors[random_index])

    # begin fill and draw circle
    turtle.begin_fill()
    turtle.circle(radius)

    # reset location, radius and pensize
    radius = random.randint(25,125)
    pen_size = random.randint(0,10)
    random_index = random.randint(0, 3)
    count= count + 1

    # generate random x and y location with each iteration
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)

    # taking pen up
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()  # pen down
    turtle.end_fill()
    turtle.write(count, "Done")
time.sleep(3)




