import random

#creates a random list of size anInt between 1 and 500
def randList(anInt):
    aList = []
    for i in range(anInt):
        num = random.randint(1,500)
        aList.append(num)
    return aList

#finds the maximum number in a given list

def find_max(aList):
    max_num = 0
    for i in aList:
        if i > max_num:
            max_num = i
    return max_num

#attempts to sort a list. but fails.

def sort(aList):
    init_list = [find_max(aList)]
    index_acc = 0

    while len(init_list) < len(aList):
        if aList[index_acc] < init_list[0]:
            current_num = aList[index_acc]
            aList.insert(0,current_num)
            index_acc = 0
            print('current num is:\n',current_num,'\n','init list is:\n',init_list)
        index_acc += 1
##        if index_acc == len(aList):
##            index_acc = 0
##            print('RESET')
##            break

l = randList(10)
