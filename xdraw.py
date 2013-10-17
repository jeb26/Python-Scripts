import turtle
pen = turtle.Turtle()

def xDraw(pen,side):
    for i in range(2):
        pen.forward(.5*side)
        pen.back(.5*side/2)
        pen.left(180)
