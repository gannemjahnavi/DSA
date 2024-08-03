import numpy as np
def setzero():
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
 
 
    print("Enter the entries: ")
 

    entries = list(map(int, input().split()))
 

    matrix = np.array(entries).reshape(R, C)
    rz=set()
    cz=set()
    for i in range(R):
        for j in range(C):
            if matrix[i][j]==0:
                rz.add(i)
                cz.add(i)
            
    for i in rz:
        matrix[i,:]=0
    for j in cz:
        matrix[:,j]=0
            
            
            
    return matrix
print(setzero())
