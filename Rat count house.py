n=int(input("enter quan of food in houses"))
a=[]
for i in range(n):
    ele=int(input("enter food"))
    a.append(ele)
r=int(input("no of rats"))
u=int(input("food units"))
def rat(a,n):
    req=r*u
    sum=0
    for i in range(n):
        sum=sum+a[i]
        print(i,sum)
        if sum>=req:
            break
    return i+1
        
print(rat(a,n))            
    
        
        
        
        
    
        
