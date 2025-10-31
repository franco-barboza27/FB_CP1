 # FB 1st Maze generator

import turtle
import random

maze_maker = turtle.Turtle()

# make a function that makes grid the size of the maze by having a list of lists

def gridsize(size):
    maze = []
    for i in range(1, size+1):
        maze.append([])

sizeask = int(input("What size of maze do you want?"))

gridsize(sizeask)