def stringvalid():
    a=input()
    c=0
    d=0
    for i in a:
        if i=='#':
            c+=1
        elif i=='*':
            d+=1
    if c-d==0:
        print("valid")
    print("not valid")
    return 0
stringvalid()
            
