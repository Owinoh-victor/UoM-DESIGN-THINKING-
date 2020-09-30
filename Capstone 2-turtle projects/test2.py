trtl=turtle.Turtle()
screen=turtle.Screen()
screen.setup(620,620)
screen.bgcolor('black')
trtl.pensize(3)
trtl.speed(10)
n=-1
for angle in range(0,360,15):
     n=n+1
     if n==5:
      n=-1
      trtl.color(colors[n])
      trtl.seth(angle)
      trtl.circle(100)
trtl.penup()
trtl.setpos(150,-270)
trtl.pendown()
trtl.pencolor('olive')
trtl.write('Vivax Solutions',font=("Arial", 12, "normal"))
trtl.ht()