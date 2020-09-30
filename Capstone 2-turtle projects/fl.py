import turtle
import time


turtle.speed(15)
turtle.setup(800, 600)
turtle.bgcolor('green')
colors = ["red", "blue", "yellow", "white","olive"]


turtle.pensize(3)

n = -1

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
turtle.clear()