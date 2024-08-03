import numpy as np
def rotate90():
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
 
    print("Enter the entries: ")
 

    entries = list(map(int, input().split()))
 
    matrix = np.array(entries).reshape(R, C)
    rotated_matrix = []
    for j in range(C):
        rotated_matrix.append(list(reversed(matrix[:, j])))
    unique=set(tuple(row) for row in rotated_matrix)
    rotate=np.array([list(row) for row in unique])
    rotated=np.transpose(rotate)
    formatted_matrix = "\n".join(" ".join(map(str, row)) for row in rotated)

    


            
            
            
    return formatted_matrix
print(rotate90())
