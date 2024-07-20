a=[1,2,3,3,3,4,5,6,7]
n=len(a)
c=[]
e=[]
def void():
    for i in a:
        if i not in c:
            d=a.count(i)
            if d==1:
                e.append(i)
            c.append(i)
        
            
    return e
print(void())
