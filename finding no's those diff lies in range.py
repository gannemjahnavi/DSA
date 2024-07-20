a=[12 ,3 ,14, 56, 77, 13]
N=len(a)
n=13
d=2
c=[]
def diff():
    for i in range(N):
        if abs(a[i]-n)<=d:
            c.append(a[i])
    c.sort()
    return c
print(diff())
            
