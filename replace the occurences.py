st="apple"
c=list(st)
n=len(c)
ch1=input()
ch2=input()
for i in range(n):
    if c[i]==ch1 and c[i]!=ch2:
        c[i]=ch2
    elif c[i]!=ch1 and c[i]==ch2:
        c[i]=ch1
        
print(c)
        
    
