# FB 1st Turtle Race

import turtle
import random
import time
import sys

print("Hello!, this is a turtle race program!\nPlease make sure to fullscreen!")
while True:
    start = input("Would you like to begin?Y/N:\n")
    if start == "Y":
        print("Great! Now beginning the race!")
        time.sleep(1)
        break
    elif start == "N":
        print("Ok, goodbye!")
        sys.exit()
    else:
        print("That's not an option!\n Try again.")

# Makes the finish line
line = turtle.Turtle()
line.hideturtle()
line.teleport(200,500)
line.right(90)
line.width(10)
line.forward(1000)

# declares all the racers
green = turtle.Turtle()
blue = turtle.Turtle()
red = turtle.Turtle()
black = turtle.Turtle()
pink = turtle.Turtle()

# gets the writer turtle to the right place
writer_turt = turtle.Turtle()
writer_turt.hideturtle()
writer_turt.teleport(300, 0)

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

# Says the GO message part
writer_turt.write("3", align="center", font=("Times New Roman", 40, "normal"))
time.sleep(1)
writer_turt.clear()
writer_turt.write("2", align="center", font=("Times New Roman", 40, "normal"))
time.sleep(1)
writer_turt.clear()
writer_turt.write("1", align="center", font=("Times New Roman", 40, "normal"))
time.sleep(1)
writer_turt.clear()
writer_turt.write("GO!", align="center", font=("Times New Roman", 40, "normal"))

# moves each turtle and checks who wins then ends when a turtle wins
loop = True
while loop:
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
        closeness = turtles[turty].xcor()
        if closeness >= 200:
            message = str(turty)
            writer_turt.clear()
            writer_turt.teleport(0, 0)
            writer_turt.write(f"The {message} Turtle Won!!!", move=False, align="right", font=("Times New Roman", 50, "normal"))
            loop = False
            break

turtle.done()