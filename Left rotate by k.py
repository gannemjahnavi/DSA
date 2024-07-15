a=[1,4,2,7,5]
n=len(a)
def x(a,n):
    c=a[0]
    for i in range(n-1):
        a[i]=a[i+1]
    a[n-1]=c
    return a
print(x(a,n))
