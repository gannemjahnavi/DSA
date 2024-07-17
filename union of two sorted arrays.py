a=[1,2,3,4,11,12]
b=[1,2,9,5,6,7,8]
c=[]
d=[]
def union():
    for i in a:
        for j in b:
            if i==j:
                c.append(i)
    for i in a:
        if not i in b:
            d.append(i)
    for j in b:
        if not j in a:
            d.append(j)
    c.sort()
    d.sort()
    return c+d
print(union())
