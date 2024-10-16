from turtle import *


t=Turtle() #create output.
t.pensize(4)  # size of turtle

for i in range(5):
    t.forward(80)
    t.right(144)
t.done()

hideturtle()
exitonclick()

mainloop() #pose the loop for view output