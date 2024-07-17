def bit():
    st=input("enter string")
    n=len(st)
    sum=int(st[0])
    for i in range(n):
        if st[i]=='A':
            sum=sum & int(st[i+1])
        elif st[i]=='B':
            sum=sum | int(st[i+1])
        elif st[i]=='C':
            sum=sum ^ int(st[i+1])
    return sum
print(bit())
            
