# FB 1st Turtle Race

import turtle
import random

line = turtle.Turtle()

line.hideturtle()

line.teleport(200,500)

line.right(90)

line.width(10)
line.forward(1000)
green = turtle.Turtle()
blue = turtle.Turtle()
red = turtle.Turtle()
yellow = turtle.Turtle()
pink = turtle.Turtle()

turtles = {"green":green, "blue":blue, "red":red, "yellow":yellow, "pink":pink}
location = 450
for turty in turtles:
    print(turty)
    turtles[turty].color(turty)
    turtles[turty].shape("turtle")
    turtles[turty].teleport(-400, location)
    location -= 50


def winCheck(turt, endcord):

    turtle.write(f"{turt} won!")
    turtle.done()


turtle.done()