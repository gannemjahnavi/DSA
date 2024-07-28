def sumofonetwodigit():
    a=[1,23,1,1,45,999]
    n=len(a)
    f=0
    e=0
    for i in a:
        c=str(i)
        d=len(c)
        if d==2:
            f=f+1
        elif d==1:
            e=e+1
            
    return e+f
    
print(sumofonetwodigit())
            
