from turtle import *

speed(0)
bgcolor('pink')

t=Turtle() #create output.
t.pensize(10)  # size of turtle

t.penup()
t.goto(-150,100)
t.pendown()

t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)

t.color('purple')
t.end_fill()

t.penup()
t.goto(-30,100)
t.pendown()
t.begin_fill()
for i in ['red','blue','magenta','green']:
    t.color(i)
    t.forward(100)
    t.left(90)
t.color('cyan')
t.end_fill()

hideturtle()
exitonclick()

mainloop() #pose the loop for view output