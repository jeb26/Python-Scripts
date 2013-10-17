import turtle
pen = turtle.Turtle()
side = 100
invalid = "Sorry, the move you entered has already been taken. Please enter a different move."
invalidCoordinate = "Sorry moves must be between 0 and 8. Please enter a new move."
gameDirect = 'This is the graphical \nrepresentation of possible \nmoves and their coordinates.'
newLine = '\n'
tttMap = '  6   |  7   |   8    \n-------------------\n  3   |  4   |   5    \n-------------------\n  0   |  1   |   2'

##Help function that displays the grid and outlines directions
def TTThelp():
    print(gameDirect)
    print(newLine)
    print(tttMap)
    print(newLine)

##this function draws the TTT grid
def drawTTTGrid(pen,side):
    for i in range(4):
        pen.forward(side)
        pen.back(side*2)
        pen.forward(side)
        pen.right(90)
        pen.forward(side)
        pen.back(side*2)

##this function draws an X
def drawX(pen,side):
    for i in range(1):
        pen.left(45)
        pen.forward(.5*side)
        pen.back(.5*side/2)
        pen.left(90)
        pen.forward(.5*side/2)
        pen.back(.5*side)

##these functions 'poly' and 'drawO' are used to draw an 'o'
def poly(pen,sideLen, sides):
    angle = 360 / sides
    for i in range(sides):
        pen.forward(sideLen)
        pen.right(angle)

def drawO(pen,radius):
    circ = 2*3.14*radius/6
    sideLen = circ / 360
    poly(pen,sideLen,360)


##the following functions are used to draw either x's or o's
##at particular places in the Tic Tac Toe Game.

##coordinate = 0
def gridPlayerX_0():
    pen.up()
    pen.goto(-side/2,-side/2)
    pen.down()
    drawX(pen,side)

def gridPlayerO_0():
    pen.up()
    pen.goto(-side/2,-side/2)
    pen.down()
    drawO(pen,side)

##coordinate = 1
def gridPlayerX_1():
    pen.up()
    pen.goto(side/2,-side/2)
    pen.down()
    drawX(pen,side)

def gridPlayerO_1():
    pen.up()
    pen.goto(side/2,-side/2)
    pen.down()
    drawO(pen,side)

##coordinate = 2
def gridPlayerX_2():
    pen.up()
    pen.goto(3*side/2,-side/2)
    pen.down()
    drawX(pen,side)

def gridPlayerO_2():
    pen.up()
    pen.goto(3*side/2,-side/2)
    pen.down()
    drawO(pen,side)

##coordinate = 3
def gridPlayerX_3():
    pen.up()
    pen.goto(-side/2,side/2)
    pen.down()
    drawX(pen,side)

def gridPlayerO_3():
    pen.up()
    pen.goto(-side/2,side/2)
    pen.down()
    drawO(pen,side)

##coordinate = 4
def gridPlayerX_4():
    pen.up()
    pen.goto(side/2,side/2)
    pen.down()
    drawX(pen,side)

def gridPlayerO_4():
    pen.up()
    pen.goto(side/2,side/2)
    pen.down()
    drawO(pen,side)

##coordinate = 5
def gridPlayerX_5():
    pen.up()
    pen.goto(3*side/2,side/2)
    pen.down()
    drawX(pen,side)

def gridPlayerO_5():
    pen.up()
    pen.goto(3*side/2,side/2)
    pen.down()
    drawO(pen,side)

##coordinate = 6
def gridPlayerX_6():
    pen.up()
    pen.goto(-side/2,3*side/2)
    pen.down()
    drawX(pen,side)

def gridPlayerO_6():
    pen.up()
    pen.goto(-side/2,3*side/2)
    pen.down()
    drawO(pen,side)

##coordinate = 7
def gridPlayerX_7():
    pen.up()
    pen.goto(side/2,3*side/2)
    pen.down()
    drawX(pen,side)

def gridPlayerO_7():
    pen.up()
    pen.goto(side/2,3*side/2)
    pen.down()
    drawO(pen,side)

##coordinate = 8
def gridPlayerX_8():
    pen.up()
    pen.goto(3*side/2,side/2)
    pen.down()
    drawX(pen,side)

def gridPlayerO_8():
    pen.up()
    pen.goto(3*side/2,side/2)
    pen.down()
    drawO(pen,side)

##this function checks which move is entered by either player x or o and then uses other functions to draw the specified move.
##the parameter that is passed to the function is the
##variable which represents the move number
def drawXmoves(move):
    if move == 0:
        ##draw figure at location
        gridPlayerX_0()
    elif move == 1:
        ##draw figure at location
        gridPlayerX_1()
    elif move == 2:
        ##draw figure at location
        gridPlayerX_2()
    elif move == 3:
        ##draw figure at location
        gridPlayerX_3()
    elif move == 4:
        ##draw figure at location
        gridPlayerX_4()
    elif move == 5:
        ##draw figure at location
        gridPlayerX_5()
    elif move == 6:
        ##draw figure at location
        gridPlayerX_6()
    elif move == 7:
        ##draw figure at location
        gridPlayerX_7()
    elif move == 8:
        ##draw figure at location
        gridPlayerX_8()

def drawOmoves(move):
    if move == 0:
        ##draw figure at location
        gridPlayerO_0()
    elif move == 1:
        ##draw figure at location
        gridPlayerO_1()
    elif move == 2:
        ##draw figure at location
        gridPlayerO_2()
    elif move == 3:
        ##draw figure at location
        gridPlayerO_3()
    elif move == 4:
        ##draw figure at location
        gridPlayerO_4()
    elif move == 5:
        ##draw figure at location
        gridPlayerO_5()
    elif move == 6:
        ##draw figure at location
        gridPlayerO_6()
    elif move == 7:
        ##draw figure at location
        gridPlayerO_7()
    elif move == 8:
        ##draw figure at location
        gridPlayerO_8()

##function which checks to make sure that moves are in corect range
##function must be passed the variable which holds the current move
def checkMove(move):
    while move < 0 or move > 8:
        print(invalidCoordinate)
        move = int(input('Player X, please enter the first move:'))
