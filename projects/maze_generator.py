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
    # needs to change in accordance to the new 0,0 cord

    size = len(rows)
    visited = set()
    stack = [(0,0)]

    while stack:
        x, y = stack.pop()

        if x == size - 1 and y == size -1:
            return True
        
        if (x, y) in visited:
            continue

        visited.add((x,y))

        if x < size - 1 and collumns[y][x+1] == 0:
            stack.append((x,y+1))

        if y < size - 1 and rows[y+1][x] == 0:
            stack.append((x,y+1))

        if x > 0 and collumns[y][x] == 0:
            stack.append((x-1,y))

        if y > 0 and rows[y][x] == 0:
            stack.append((x,y-1))
        
    return False

def mazemaker(rows, collumns, outsideparts):
    mazesize = len(rows)
    
    rowwy = 0
    for row in rows:
        everyline = 0
        while everyline in range(0, mazesize+1):
            #looping infinitely currently
            upwall = random.randint(0,1)
            collumns[rowwy].append(upwall)
            sidewall = random.randint(0,1)
            rows[rowwy].append(sidewall)
            everyline += 1
        rowwy += 1

    # keeps track of sides and chooses two different start points
    possiblesides = [1, 2, 3, 4]
    oppeningside = random.choice(possiblesides)
    start = random.randint(0, mazesize+1)
    end = random.randint(0, mazesize+1)

    if oppeningside == 1:
        outsideparts[0][start] = 0
        start = outsideparts[0]
    if oppeningside == 2:
        outsideparts[1][start] = 0
        start = outsideparts[1]
    if oppeningside == 3:
        outsideparts[2][start] = 0
        start = outsideparts[2]
    if oppeningside == 4:
        outsideparts[3][start] = 0
        start = outsideparts[3]
    possiblesides.remove(oppeningside)

    oppeningside = random.choice(possiblesides)
    if oppeningside == 1:
        outsideparts[0][end] = 0
        end = outsideparts[0]
    if oppeningside == 2:
        outsideparts[1][end] = 0
        end = outsideparts[1]
    if oppeningside == 3:
        outsideparts[2][end] = 0
        end = outsideparts[2]
    if oppeningside == 4:
        outsideparts[3][end] = 0
        end = outsideparts[3]

    is_solvable(rows, collumns, start, end)

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