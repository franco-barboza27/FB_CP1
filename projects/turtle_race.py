# FB 1st Turtle Race

import turtle
import random

t = turtle.Turtle()

line_color = ['red', 'black', 'blue', 'orange', 'yellow']
fill = ['pink', 'white', 'cyan']

side_len = random.randint(100, 300)
square_width = random.randint(100, 300)
for turn in range(4):
    for lc in line_color:
        t.right(random.randint(0,360))
        for fc in fill:
            t.fillcolor(fc)
            t.color(lc)
            t.begin_fill()
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.end_fill()
            t.penup()
            t.right(90)
            t.forward(100)
            t.pendown()

turtle.done()