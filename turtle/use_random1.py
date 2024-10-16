from turtle import Turtle
from random import random
t = Turtle()
t.speed(20)
for i in range(30):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)
t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("orange")
t.screen.mainloop()