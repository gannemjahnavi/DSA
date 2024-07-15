a=[1,2,3,4,5,6,7,8,9]
n=len(a)
c=[]
e=[]
def xrotate(a,n):
    d=int(input("enter"))
    for i in range(0,d):
        c.append(a[i])
    for j in range(1,n):
        if a[j] not in c:
            e.append(a[j])
            
        
    return e+c
print(xrotate(a,n))
