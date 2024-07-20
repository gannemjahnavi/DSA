def check():
    st=input()
    n=len(st)
    c=0
    d=0
    if n<4:
        return 0
    if st[0].isdigit():
        return 0
    for i in range(n):
        if st[i]>='0' and st[i]<='9':
            c=c+1
        if st[i]>='A'and st[i]<='Z':
            d=d+1
        elif st[i]==' ' or st[i]=='/':
            return 0
    if c>0 and d>0:
        return 1
    else:
        return 0
print(check())
           
    
