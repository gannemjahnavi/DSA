def diffofsum():
    n=int(input())
    m=int(input())
    c=0
    d=0
    if n<=0 or m<=0:
        return 0
    for i in range(1,m+1):
        if i%n==0:
            c=c+i
        else:
            d=d+i
    return abs(d-c)
print(diffofsum())
            
    
