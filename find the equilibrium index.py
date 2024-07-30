def equilibrium():
    a=[1,-1,4]
    n=len(a)
    
    for i in range(n):
        left=0
        right=0
        for j in range(0,i):
            left+=a[j]
        for j in range(i+1,n):
            right+=a[j]
        if left==right:
            return i
    
            
    return -1
print(equilibrium())
        
        
