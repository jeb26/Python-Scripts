##
##for i in range(-1,5,-2):
##    print('i is:', i)
##
##########write a function which would travel through a list and square every number
########def sqList(aList):
########    finalList = []
########    for item in aList:
########        finalList.append(item**2)
########    return finalList
########def sqIter(_list):
########    for i in range(len(_list)):
########        _list[i]=_list[i]**2
########    return _list
######
########a = 'lisa'
########b = ['lisa-marie','anne','lena','denise']
########x=0
########
########while a in b:
########    print('a is in b')
########    x += 1
########    print('x is',x)
########    if x == 10:
########        break
########else:
########    print(a,'is not in',b)
########    
######
####_dictionary = {'army':'ground','navy':'boats','jersey city':'jungle','audi':'german','money':'is everything'}
######
########for i in _dictionary:
########    print(i)
######
######for i in _dictionary.values():
######    print(i)
######
######x = "" 
######s = 'Arrest the usual suspects' 
######i = 0 
######while 'usual' not in x: 
######    x += s[i] 
######    i += 1 
######print(x) 
####
####_dictionary = {'kathy':'201-366-4874','mike':'551-580-1057','jim':'805-665-4789'}
####
####def phoneInit0(aDict,intial):
####    newDict = {}
####    for item in aDict:
####        if item[0].find(intial) > -1:
####            newDict[item] = aDict[item]
####    return newDict
####
######another way of doing it
####def phoneInit1(aDict,intial):
####    newDict = {}
####    for i in aDict:
####        if intial in i[0]:
####            newDict[i] = aDict[i]
####    return newDict
####
####def phoneByAreaCode(aDict,areaCode):
####    newDict = {}
####    for i in aDict:
####        if areaCode in aDict[i][0:3]:
####            newDict[i] = aDict[i]
####    return newDict
##
s = 'the cat in the hat came back'
moreAs = -1 
aCount = 0 
eCount = 0 
for i in range(len(s)): 
      if s[i] == 'e' or s[i] == 'E': 
          eCount += 1 
          continue 
      if s[i] == 'a' or s[i] == 'A': 
        aCount += 1 
        if aCount > eCount: 
             moreAs = i 
             break 
print('i = ', i, ', moreAs = ', moreAs) 
