def findPrimes(target):
    for i in range(1,target+1):
        if target % i == 0:
            print(i)

findPrimes(90)
