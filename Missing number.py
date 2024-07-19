def missingNumber(a , N ):
    c=len(a)
    for i in range(1,N+1):
        d=0
        for j in range(c):
            if a[j]==i:
                d=1
                break
        if d==0:
            return i
            
    return -1
