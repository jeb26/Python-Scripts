def isPrime(aNum):
    if aNum in [1,2]:
        return True
    for i in range(2,aNum):
        if aNum % i == 0:
            return False
        else:
            return True
