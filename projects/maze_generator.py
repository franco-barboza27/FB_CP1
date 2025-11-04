 # FB 1st Maze generator

import turtle
import random

# make a function that makes grid the size of the maze by having a list of lists



sizeask = int(input("What size of maze do you want?"))

maze_maker = turtle.Turtle()
maze_maker.hideturtle()
maze_maker.penup()
maze_maker.teleport(sizeask)

for i in range(1, sizeask+1):
    maze_maker.