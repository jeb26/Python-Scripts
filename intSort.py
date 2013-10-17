def intSort(a,b,c):
    if (a > b) and (b > c):
        print(a,"\t",b,"\t",c)
    elif (b > c) and (c > a):
        print(b,"\t",c,"\t",a)
    elif (c > b) and (b > a):
        print(c,"\t",b,"\t",a)
    elif (b > a) and (a > c):
        print(b,"\t",a,"\t",c)
    elif (c > a) and (a > b):
        print(c,"\t",a,"\t",b)
    elif (a > c) and (c > b):
        print(a,"\t",c,"\t",b)
