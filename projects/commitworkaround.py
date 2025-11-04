 # FB 1st Maze generator

import turtle
import random

# make a function that makes grid the size of the maze by having a list of lists

def gridsize(size):
    rows = []
    collumns = []
    for i in range(1, size):
        rows.append([])
        collumns.append([])
    mazemaker(rows, collumns)

def is_solvable(rows, collumns):
    pass

def mazemaker(rows, collumns):
    mazesize = len(rows)
    everyline = 0
    for row in rows:
        for row in rows:
            collumns[everyline].append(1)
            rows[everyline].append(1)
        everyline += 1
    

    pass

def drawmaze():
    maze_maker = turtle.Turtle()
    pass

sizeask = int(input("What size of maze do you want?"))

gridsize(sizeask)

