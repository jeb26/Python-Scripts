##Simple algorithm that drills you on your addition mental math.
##You enter the base operand which should be from 1 to 9. Any you enter the amount
##of rounds / number of questions you would like to be asked. At the end,
##the algorithm will compute your score. 

import random

def addition():
    currentRound = 0
    numWrong = 0
    userBaseInput = input('What would you like the base operand to be?')
    BASE = int(userBaseInput)
    userRoundInput = input('How many problems would you like to be asked?')
    ROUNDS = int(userRoundInput)
    while currentRound < ROUNDS:
        currentRound += 1
        operand = random.randint(1,9)
        CORRECT_ANSWER = BASE + operand
        userAnsInput = input('What is {0} + {1} ?'.format(BASE, operand))
        USER_ANSWER = int(userAnsInput)
        if USER_ANSWER == CORRECT_ANSWER:
            print('Correct!')
        else:
            while USER_ANSWER != CORRECT_ANSWER:
                numWrong += 1
                print('Incorrect Please Try Again!')
                userAnsInput = input('What is {0} + {1} ?'.format(BASE, operand))
                USER_ANSWER = int(userAnsInput)
        if currentRound == ROUNDS:
            print('Out of {0} rounds.\nYou got {1} wrong.\n Your score is {2}!'.format(ROUNDS,numWrong,((ROUNDS-numWrong)/ROUNDS)*100))
