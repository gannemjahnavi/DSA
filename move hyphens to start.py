def hyphen():
    st=input()
    a=""
    c=0
    for i in st:
        if i=='-':
            c+=1
        else:
            a+=i
    return ('-'*c)+a
print(hyphen())
            
