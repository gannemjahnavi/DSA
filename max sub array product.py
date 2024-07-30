def maxproductsubarray():
    a=[1,2,3,4,5,0]
    n=len(a)
    pre=1
    suc=1
    prod=float('-inf')
    if pre==0:
        pre=1
    if suc==0:
        suc=1
    for i in range(n):
        pre=pre*a[i]
        suc=suc*a[n-i-1]
        prod=max(prod,max(pre,suc))
    return prod
print(maxproductsubarray())
        
    
