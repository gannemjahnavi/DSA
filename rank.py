def rank():
    a=[20 ,15 ,26 ,2 ,98, 6]
    n=len(a)
    c=sorted(a)
    m=len(c)
    for i in range(n):
        for j in range(m):
            if a[i]==c[j]:
                print(j+1)

    
                
    return 0
rank()
