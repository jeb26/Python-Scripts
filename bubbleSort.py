a = [45,56,1,98,15,39,5,44,185,111,44]

def printArray(a):
        print "Array:\n"
        for i in range(len(a)):
                print "%d\t" % a[i]
        print "\n"

def bubbleSort(a):
        for i in range(len(a)-1):
                if ((i < (len(a) - 1)) and (a[i] > a[i+1])):
                        temp = a[i]
                        a[i] = a[i + 1]
                        a[i + 1] = temp
                        i = -1
