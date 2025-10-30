# FB 1st Turtle Race

import turtle
import random

# Makes the finish line
line = turtle.Turtle()
line.hideturtle()
line.teleport(200,500)
line.right(90)
line.width(10)
line.forward(1000)

screen = turtle.Screen()
screen.screensize(1000, 1000)


# declares all the racers
green = turtle.Turtle()
blue = turtle.Turtle()
red = turtle.Turtle()
black = turtle.Turtle()
pink = turtle.Turtle()

# gets the writer turtle to the right place
writer_turt = turtle.Turtle()
writer_turt.teleport(0, 500)



# puts all the turtles to their spots
turtles = {"green":green, "blue":blue, "red":red, "black":black, "pink":pink}
move = 0
direction = 0
location = 400
for turty in turtles:
    print(turty)
    turtles[turty].color(turty)
    turtles[turty].shape("turtle")
    turtles[turty].teleport(-500, location)
    location -= 200


#moves each turtle
while True:
    for turty in turtles:
        move = random.randint(5, 10)
        direction = random.randint(-5, 5)
        if turtles[turty].ycor() <= -475 or turtles[turty].ycor() >= 475:
            turtles[turty].penup()
            turtles[turty].sety(0)
            turtles[turty].seth(0)
            turtles[turty].pendown()
        turtles[turty].right(direction)
        turtles[turty].forward(move)
        if turtles[turty].xcor(200):
            message = f"{turtles}"
            writer_turt.write(f"The {message} turtle Won!!!", move=False, align="center", font=("Arial", 8, "normal"))


def winCheck(turt, endcord):

    turtle.write(f"{turt} won!")
    turtle.done()


turtle.done()