a=[1,8,0,2,3,5,6]
n=len(a)
def largesum(a,n):
    c=[]
    d=[]
    for i in range(n):
        if i%2==0:
            c.append(a[i])
            
        else:
            d.append(a[i])
    
    c.sort()
    d.sort()
    return c[-2]+d[-2]
print(largesum(a,n))
