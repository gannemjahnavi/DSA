def product():
    sum=int(input())
    a=[5,2,4,3,9,7,1]
    a=sorted(a)
    n=len(a)
    if a[0]+a[1]<sum:
        return a[0]*a[1]
        
           
print(product())
            
