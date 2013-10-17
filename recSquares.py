import turtle

pen = turtle.Turtle()

def drawSq(pen,sideLen):
    for i in range(4):
        pen.forward(sideLen)
        pen.right(90)
    pen.forward(sideLen)

def nSq(pen,sideLen,numSq):
    rounds = 1
    while(numSq != 0):
        for i in range(numSq):
            drawSq(pen,sideLen)
        pen.up()
        pen.goto(((sideLen / 2) * rounds),(sideLen * rounds))
        numSq -= 1
        rounds += 1
        pen.down()
    turtle.exitonclick()

'''
nSq(pen,30,4)
'''
