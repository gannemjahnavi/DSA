a=int(input())
b=a[::-1]
def binarytodec(b):
    c=0
    n=len(b)
    for i in range(n):
        c=c+(int(b[i])*pow(2,i))
    return c
def dectobinary(a):
    c = []
    while a > 0:
        c.append(a % 2)  
        a = a // 2 
    
    c.reverse()  
    return c


print(dectobinary(a))
