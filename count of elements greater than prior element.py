def countofprior():
    a=[3,4,5,8,9]
    n=len(a)
    c=1
    k=a[0]
    for i in range(1,n):
        if a[i]>k:
            c+=1
    return c
print(countofprior())
            
