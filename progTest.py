def divisbleTest(m,n):
    ans = m * n
    return ans
    
def intersection(a,b):
    ans = []
    
    for i in a:
        for j in b:
            if i == j:
                ans.append(i)
    return ans
