a=[1,2,4,3,9,2]
a=sorted(a)
n=len(a)
target=int(input())
def search(a,n,target):
    low=0
    high=n-1
    while(low<high):
        mid=int(low+high/2)
        if a[mid]==target:
            return a[mid]
        elif a[mid]<target:
            low=mid+1
        else:
            high=mid-1
            
    return -1
print(search(a,n,target))

    
    
