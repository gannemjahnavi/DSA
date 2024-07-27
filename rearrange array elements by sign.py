def random():
    a=[1,2,-4,-5]
    n=len(a)
    for i in range(n):
        if i%2==0:
            if a[i]>0:
                i=i+1 
            else:
                a[i],a[i+1]=a[i+1],a[i]
        else:
            if a[i]<0:
                i=i+1 
            else:
                a[i],a[i+1]=a[i+1],a[i]
    return a 
print(random())
