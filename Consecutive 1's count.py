a=[1,1,0,1,1,1]
def seq():
    n=len(a)
    c=0
    maximum=0
    for i in range(n):
        if a[i]==1:
            c=c+1
        else:
            c=0
        maximum=max(maximum,c)
    return maximum
print(seq())
        
