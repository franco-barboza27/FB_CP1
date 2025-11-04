import turtle
import random


x = turtle.Turtle()
x.color("green")
x.fillcolor("yellow")
x.speed(10000000)
x.width(3)
angl = 45
change = 1
for i in range(1, 900):
    i += 1
    x.begin_fill()
    x.circle(100, extent=None, steps=90)
    x.hideturtle()
    x.end_fill()
    x.right(angl)
    angl += change
    if angl <= 0:
        change = 1
    elif angl >= 360:
        change = -1
turtle.done()