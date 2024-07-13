a=[1,2,3,0,0,2]
def zero(a):
    c=[x for x in a if x!=0]
    d=[x for x in a if x==0]
    return c+d
print(zero(a))
