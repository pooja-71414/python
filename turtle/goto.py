from turtle import *

speed(0)
bgcolor('pink')

t=Turtle() #create output.
# t.pensize(4)  # size of turtle

t.penup()
t.goto(100,50)
t.pendown()

t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)

t.color('purple')
t.end_fill()

hideturtle()
exitonclick()

mainloop() #pose the loop for view output