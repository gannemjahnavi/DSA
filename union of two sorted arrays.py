a=[1,2,3,4,11,12]
b=[1,2,9,5,6,7,8]
c=[]
def union():
    for i in a:
        for j in b:
            if i==j:
                c.append(i)
    for i in a:
        if not i in b:
            c.append(i)
    for j in b:
        if not j in a:
            c.append(j)
    c.sort()
    return c
print(union())
