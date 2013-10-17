array = [25,66,87,2156,58,96,44,12,3,15]

def findMin(a):
    for i in range(len(a)):
        numMin = i
        for j in range(len(a)):
            if a[j] < numMin:
                numMin = a[j]
    return numMin

