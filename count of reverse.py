def reverse():
    a=[1,3,2,3,1]
    n=len(a)
    d=[]
    e=[]
    f=0
    for i in range(n):
        for j in range(i+1,n):
            if a[i] > 2 * a[j]:
                f+=1
            else:
                pass
        
        
            
            
        
    return f
print(reverse())
