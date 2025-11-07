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
                [],[], # <==top & bottom
                  []
           # side ^
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

def is_solvable(rows, collumns, sides):
    # needs to account for the new start coordinate each generation

    size = len(rows)
    visited = set()
    foundstart = []

    for side in sides:
        for wall in side:
            if foundstart:
                if side.index() == 0:
                    ey = 0
                    ex = wall.index()
                elif side.index() == 1:
                    ey = wall.index()
                    ex = size
                elif side.index() == 2:
                    ey = size
                    ex = wall.index()
                elif side.index() == 3:
                    ey = 0
                    ex = wall.index()
                continue

            if index(0):
                sy = 0
                sx = wall.index()
                foundstart.append(side.index())
            elif side.index() == 1:
                sy = wall.index()
                sx = size
                foundstart.append(side.index())
            elif side.index() == 2:
                sy = size
                sx = wall.index()
                foundstart.append(side.index())
            elif side.index() == 3:
                sy = 0
                sx = wall.index()
                foundstart.append(side.index())

    stack = [(sx, sy)]

    while stack:
        x, y = stack.pop()

        if x == ex - 1 and y == ey -1:
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

def mazegenerator(rows, collumns, outsideparts):
    while True:
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

        if is_solvable(rows, collumns, outsideparts) == True:
            break
        if is_solvable(rows, collumns, outsideparts) == False:
            gridsize(mazesize+1)
    drawmaze(rows, collumns, outsideparts)





def drawmaze(rows, collumns, sides):
    maze_maker = turtle.Turtle()
    maze_maker.speed(0)
    maze_maker.penup()
    size = len(rows)+1
    startx = size * -50
    starty = size * -50
    maze_maker.teleport(startx, starty)
    print(maze_maker.position())

    # draw the sides
    for side in sides:
        for wall in side:
            if wall == 0:
                maze_maker.penup()
                maze_maker.forward(50)
            if wall == 1:
                maze_maker.pendown()
                maze_maker.forward(50)
        maze_maker.left(90)

    i = 0

    for row in rows:
        
        i += 1
        maze_maker.teleport(startx, starty+i*50)
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
        maze_maker.teleport(startx+i*50, starty)
        for wall in collumn:
            if wall == 0:
                maze_maker.penup()
                maze_maker.forward(50)
            if wall == 1:
                maze_maker.pendown()
                maze_maker.forward(50)
        maze_maker.teleport(startx, starty)


    turtle.done()
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