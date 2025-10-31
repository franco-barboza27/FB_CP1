# FB 1st Turtle Race

import turtle
import random
import time
import sys

def begin(check):
    if check == "Y":
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
        location = 400
        for turty in turtles:
            print(turty)
            turtles[turty].color(turty)
            turtles[turty].shape("turtle")
            turtles[turty].teleport(-500, location)
            location -= 200
    go(turtles, writer_turt,)

def go(turts, writer):
    # Says the GO message part
    writer.write("3", align="center", font=("Times New Roman", 40, "normal"))
    time.sleep(1)
    writer.clear()
    writer.write("2", align="center", font=("Times New Roman", 40, "normal"))
    time.sleep(1)
    writer.clear()
    writer.write("1", align="center", font=("Times New Roman", 40, "normal"))
    time.sleep(1)
    writer.clear()
    writer.write("GO!", align="center", font=("Times New Roman", 40, "normal"))
    gameloop(turts, writer)

def gameloop(turts, writer):
    # moves each turtle and checks who wins then ends when a turtle wins
    loop = True
    while loop:
        for turty in turts:
            steps = random.randint(5, 10)
            direction = random.randint(-5, 5)
            if turts[turty].ycor() <= -475 or turts[turty].ycor() >= 475:
                turts[turty].penup()
                turts[turty].sety(0)
                turts[turty].seth(0)
                turts[turty].pendown()
            turts[turty].right(direction)
            turts[turty].forward(steps)
            closeness = turts[turty].xcor()
            if closeness >= 200:
                message = str(turty)
                writer.clear()
                writer.teleport(0, 0)
                writer.write(f"The {message} Turtle Won!!!", move=False, align="right", font=("Times New Roman", 50, "normal"))
                loop = False
                break

    turtle.done()

print("Hello!, this is a turtle race program!\nPlease make sure to fullscreen!")
while True:
    start = input("Would you like to begin?Y/N:\n")
    if start == "Y":
        print("Great! Now beginning the race!")
        time.sleep(1)
        begin(start)
        break
    elif start == "N":
        print("Ok, goodbye!")
        sys.exit()
    else:
        print("That's not an option!\n Try again.")
