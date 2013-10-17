a = [5,6,0,22,69,4,55858,0]

def findMax(aList):
    placeHolder = 0
    for item in aList:
        if item > placeHolder:
            placeHolder = item
        else:
            continue
    return placeHolder
    
print(findMax(a))
