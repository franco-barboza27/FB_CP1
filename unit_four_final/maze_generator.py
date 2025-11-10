# FB 1st Maze generator

import turtle
import random

# make a function that makes grid the size of the maze by having a list of lists

def gridsize(size):
    rows = []
    collumns = []
    outsideparts = [
            # bottom
                  [],
                [],[], # right, top
                  []
           # left
    ]
    for sides in outsideparts:
        tracker = 0
        while tracker in range(0, size):
            tracker += 1
            sides.append(1)

    for i in range(1, size):
        rows.append([])                                         
        collumns.append([])
    mazegenerator(rows, collumns, outsideparts)

def sidechecker(side):
    for wall in side:
        if wall == 0:
            return True
    return False

def is_solvable(rows, collumns, sides):
    # needs to account for the new start coordinate each generation

    rows.insert(0, sides[0])
    rows.insert(len(rows), sides[2])
    collumns.insert(0, sides[3])
    collumns.insert(len(collumns), sides[1])

    gridsize = len(rows)
    size = len(rows)-2
    visited = set()
    foundstart = []
    foundend = ""
    curside = 0
    for side in sides:
        curwall = 0
        # checks where the ending and starting points are and saves them as a value
        if foundstart:
            # bottom side ending checker
            if curside == 0 and sidechecker(side) is True:
                i = -1
                for wall in side:
                    i += 1
                    if wall == 0:
                        curwall = i
                ex, ey = curwall, 0
                foundend = 1
            # right side ending checker
            elif curside == 1 and sidechecker(side) is True:
                i = -1
                for wall in side:
                    i += 1
                    if wall == 0:
                        curwall = i
                ex, ey = size, curwall
                foundend = 1
            # top ending checker
            elif curside == 2 and sidechecker(side) is True:
                i = -1
                for wall in side:
                    i += 1
                    if wall == 0:
                        curwall = i
                ex, ey = curwall, size
                foundend = 1
            # left ending checker
            elif curside == 3 and sidechecker(side) is True:
                i = -1
                for wall in side:
                    i += 1
                    if wall == 0:
                        curwall = i
                ex, ey = curwall, 0
                foundend = 1
            curside += 1
            continue

        if foundend:
            break
        
        # bottom oppening checker
        if curside == 0 and sidechecker(side) is True:
            i = -1
            for wall in side:
                i += 1
                if wall == 0:
                    curwall = i
            sx, sy = curwall, 0
            foundstart.append(side[0])
        # right oppening checker
        elif curside == 1 and sidechecker(side) is True:
            i = -1
            for wall in side:
                i += 1
                if wall == 0:
                    curwall = i
            sx, sy = size, curwall
            foundstart.append(side[1])
        # top oppening checker
        elif curside == 2 and sidechecker(side) is True:
            i = -1
            for wall in side:
                i += 1
                if wall == 0:
                    curwall = i
            sx, sy = curwall, size
            foundstart.append(side[2])
        # left oppening checker
        elif curside == 3 and sidechecker(side) is True:
            i = -1
            for wall in side:
                i += 1
                if wall == 0:
                    curwall = i
            sx, sy = curwall, 0
            foundstart.append(side[3])
        curside += 1

    stack = [(sx, sy)]

    while stack:
        sx, sy = stack.pop()
        # checks if the maze is solvable and re-randomizes it if it's not
        if sx == ex and sy == ey:
            collumns.pop(0)
            rows.pop(0)
            collumns.pop(len(collumns)-1)
            rows.pop(len(rows)-1)
            return True
        
        if (sx, sy) in visited:
            continue

        visited.add((sx,sy))

        # right wall checker
        if sx < size - 1 and collumns[sy][sx + 1] == 0:
            stack.append((sx + 1, sy))
        # below wall checker
        if sy < size - 1 and rows[sy + 1][sx] == 0:
            stack.append((sx, sy + 1))
        # left wall checker
        if sx > 0 and collumns[sy][sx] == 0:
            stack.append((sx - 1, sy))
        # above wall checker
        if sy > 0 and rows[sy][sx] == 0:
            stack.append((sx, sy - 1))

    return False

def mazegenerator(rows, collumns, outsideparts):
    while True:
        mazesize = len(rows)
        # randomizes the walls of the collumns and rows
        rowwy = 0
        for row in rows:
            everyline = 0
            while everyline in range(0, mazesize+1):
                upwall = random.randint(0,1)
                collumns[rowwy].append(upwall)
                sidewall = random.randint(0,1)
                rows[rowwy].append(sidewall)
                everyline += 1
            rowwy += 1

        # keeps track of sides and chooses two different start points
    
        possiblesides = [1, 2, 3, 4]
        oppeningside = random.choice(possiblesides)
        start = random.randint(0, mazesize)
        end = random.randint(0, mazesize)

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

        if is_solvable(rows, collumns, outsideparts) is True:
            break
        else:
            gridsize(mazesize+1)
    drawmaze(rows, collumns, outsideparts)





def drawmaze(rows, collumns, sides):
    maze_maker = turtle.Turtle()
    maze_maker.speed(0)
    maze_maker.penup()
    size = len(rows)-1
    startx = size * -50
    starty = size * -50
    maze_maker.teleport(startx, starty)

    # draw the sides
    poskeeper = 0
    for side in sides:
        if poskeeper == 1:
            maze_maker.left(90)
        elif poskeeper == 2:
            toplefty = maze_maker.ycor()
            maze_maker.teleport(startx,toplefty)
            maze_maker.right(90)
        elif poskeeper == 3:
            maze_maker.teleport(startx, toplefty)
            maze_maker.right(90)
        for wall in side:
            if wall == 0:
                maze_maker.penup()
                maze_maker.forward(50)
            if wall == 1:
                maze_maker.pendown()
                maze_maker.forward(50)
                maze_maker.penup()
        poskeeper += 1
            


    maze_maker.left(90)
    i = 0

    for row in rows:
        
        i += 1
        maze_maker.teleport(startx, starty+(i*50))
        for wall in row:
            if wall == 0:
                maze_maker.penup()
                maze_maker.forward(50)
            if wall == 1:
                maze_maker.pendown()
                maze_maker.forward(50)
        maze_maker.teleport(startx, starty)

    i = 0
    maze_maker.left(90)
    for collumn in collumns:
        
        i += 1
        maze_maker.teleport(startx + (i*50), starty)
        for wall in collumn:
            if wall == 0:
                maze_maker.penup()
                maze_maker.forward(50)
            if wall == 1:
                maze_maker.pendown()
                maze_maker.forward(50)
        maze_maker.teleport(startx, starty)


    turtle.done()

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