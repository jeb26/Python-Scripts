##Program takes in an integer of multiple digits.
##And sums them. Then returns the answer.

def intTake():
    intAcc = 0
    INTEGER_INPUT = input("Please enter an integer.")
    CURRENT_INTEGER = 0

    for i in INTEGER_INPUT:
        CURRENT_INTEGER = int(i)
        intAcc += CURRENT_INTEGER

    return intAcc 
        
