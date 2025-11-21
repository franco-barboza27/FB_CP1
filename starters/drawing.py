from turtle import *

def draw_branch(length):
    if length > 5:
        for i in range(3):
            turt.forward(length)
            draw_branch(length/3, turt)
            turtle.backward(length)
            turtles.right(60)

draw_branch(90)