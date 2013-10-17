#'y' is counted as a variable
def moreVowels(aStr, anInt):
        aStr0 = aStr.lower()
        numVowels = 0
        for i in range(len(aStr0)):
                if aStr0[i] == 'a' or aStr0[i] == 'e' or aStr0[i] == 'i' or aStr0[i] == 'o' or aStr0[i] == 'u' or aStr0[i] == 'y':
                        numVowels += 1
        if numVowels > anInt:
                return True
        else:
                return False

                        
