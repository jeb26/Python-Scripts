def readWrite(fileName):
    fileIN = open(fileName,"r")
    fileOUT = open('write.txt',"w")

    for i in fileIN:
        print('Writing:', i)
        fileOUT.write('James is a :' + i)
        
    fileIN.close()
    fileOUT.close()
    
    
