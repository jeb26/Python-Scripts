from tttObjects import *

def TTTplay():
    TTThelp()
    drawTTTGrid(pen,side)
    move1 = int(input('Player X, please enter the first move:'))
    checkMove(move1)
    drawXmoves(move1)

    move2 = int(input('Player Y, please enter the second move:'))
    while move2 == move1:
        print(invalid)
        move2 = int(input('Player Y, please enter the second move:'))
    checkMove(move2)
    drawOmoves(move2)

    move3 = int(input('Player X, please enter the third move:'))
    while move3 == move2 or move3 == move1:
        print(invalid)
        move3 = int(input('Player X, please enter the third move:'))
    checkMove(move3)
    drawXmoves(move3)

    move4 = int(input('Player Y, please enter the fourth move:'))
    while move4 == move3 or move4 == move2 or move4 == move1:
        print(invalid)
        move4 = int(input('Player Y, please enter the fourth move:'))
    checkMove(move4)
    drawOmoves(move4)

    move5 = int(input('Player X, please enter the fifth move:'))
    while move5 == move4 or move5 == move3 or move5 == move2 or move5 == move1:
        print(invalid)
        move5 = int(input('Player X, please enter the fifth move:'))
    checkMove(move5)
    drawXmoves(move5)

    move6 = int(input('Player Y, please enter the sixth move:'))
    while move6 == move5 or move6 == move4 or move6 == move3 or move6 == move2 or move6 == move1:
        print(invalid)
        move6 = int(input('Player Y, please enter the sixth move:'))
    checkMove(move6)
    drawOmoves(move6)

    move7 = int(input('Player X, please enter the seventh move:'))
    while move7 == move6 or move7 == move5 or move7 == move4 or move7 == move3 or move7 == move2 or move7 == move1:
        print(invalid)
        move7 = int(input('Player X, please enter the seventh move:'))
    checkMove(move7)
    drawXmoves(move7)

    move8 = int(input('Player Y, please enter the eigth move:'))
    while move8 == move7 or move8 == move6 or move8 == move5 or move8 == move4 or move8 == move3 or move8 == move2 or move8 == move1:
        print(invalid)
        move8 = int(input('Player Y, please enter the eigth move:'))
    checkMove(move8)
    drawOmoves(move8)

    move9 = int(input('Player X, please enter the final move:'))
    while move9 == move8 or move9 == move7 or move9 == move6 or move9 == move5 or move9 == move4 or move9 == move3 or move9 == move2 or move9 == move1:
        print(invalid)
        move9 = int(input('Player X, please enter the final move:'))
    checkMove(move9)
    drawXmoves(move9)

