from turtle import *

speed(0)
bgcolor('pink')

t=Turtle() #create output.
t.pensize(4)  # size of turtle

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)

for i in range(4):
    t.forward(100)
    t.left(90)

hideturtle()
exitonclick()

mainloop() #pose the loop for view output