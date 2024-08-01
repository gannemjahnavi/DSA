def checksubarrayelements():
    a=[1,2,3,4,5,9]
    b=[1,4,3,2,6,7,5]
    n=len(a)
    c=0
    for i in range(len(a)):
        if a[i] in b:
            c+=1
        else:
            break
        
    if c==n:
        print(True)
    else:
        print(False)
    return 0
checksubarrayelements()
    
                
                
