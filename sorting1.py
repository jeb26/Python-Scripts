#Simple sorting algorithm which takes one parameter, a list containing integers to
#be sorted. After the sort is completed a new list is returned. Everything is done
#from smallest number to largest number.

def sort(aList):
    listMax = 0
    listMin = 0
    results = []

    for i in range(len(aList)):
        for j in aList:
            if j > listMax:                 #Determine the Max
                listMax = j
        results.append(listMax)
        aList.remove(results[i])
        print(aList)
            #aList.remove(i)
##    for j in integers:                  #Determine the Min
##        if j < listMin:
##            listMin = j
##            results.insert(0,listMin)
##        integers.remove(list)
    return results

for i in range(len(aList)):
    aList[i]
    
