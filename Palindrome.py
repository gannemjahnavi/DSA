a=[1,2,4,4,2,1]
n=len(a)
def palin(a,n):
    for i in range(n):
        for j in range(i):
            if a[j]==a[i]:
                return True
    return False
c=palin(a,n)
print(c)
