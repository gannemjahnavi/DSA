a="man cat man bed"
n=int(input())
a=a.split()
b=dict()
for word in a:
    if word in b:
        b[word]+=1
    else:
        b[word]=1
for i in b.keys():
    if b[i]==n:
        print(i)
