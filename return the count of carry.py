def carry():
    s1=input()
    s2=input()
    s11=list(s1)
    s22=list(s2)
    n=len(s11)
    m=len(s22)
    c=0
    for i in range(n):
        for j in range(m):
            if int(s11[n-i-1])+int(s22[n-j-1])>=10:
                c+=1
    return c
