# FB 1st Maze generator

import turtle
import random

# make a function that makes grid the size of the maze by having a list of lists

def gridsize(size):
    rows = []
    collumns = []
    outsideparts = [
            # Top V
                  [],
                [],[], # <==sides
                  []
           # untop ^
    ]
    for sides in outsideparts:
        tracker = 0
        while tracker in range(0, size):
            tracker += 1
            sides.append(1)

    for i in range(1, size):
        rows.append([])
        collumns.append([])
    mazemaker(rows, collumns, outsideparts)

def is_solvable(rows, collumns, start, end):
    pass

def mazemaker(rows, collumns, outsideparts):
    mazesize = len(rows)
    everyline = 0

    for row in rows:
        while len(row) in range(0, mazesize):
            #loopong infinitely currently
            upwall = random.randint(0,1)
            collumns[len(row)].append(upwall)
            sidewall = random.randint(0,1)
            rows[len(row)].append(sidewall)

    sidescheck = []
    
    while len(sidescheck) < 2:
        oppeningside = random.randint(1,4)
        oppening = random.randint(0, mazesize+1)
        if oppeningside == 1:
            outsideparts[0][oppening] = 0
        if oppeningside == 2:
            outsideparts[1][oppening] = 0
        if oppeningside == 3:
            outsideparts[2][oppening] = 0
        if oppeningside == 4:
            outsideparts[3][oppening] = 0
                
                


    pass

def drawmaze():
    maze_maker = turtle.Turtle()
    pass

while True:
    sizeask = int(input("What size of maze do you want?"))
    if sizeask <= 2:
        print("THAT IS WAY TO SMALL!!!!!!\nKindly choose a bigger number :')")
    elif sizeask > 2:
        print("Thanks!")
        break
    else:
        print("What? That's a wierd input, try another one.")


gridsize(sizeask)