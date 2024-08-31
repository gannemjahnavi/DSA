arr=[2,3,4,5,6,4]
n=len(arr)
x=int(input())
arr=sorted(arr)
def lowerBound(arr: [int], n: int, x: int) -> int:
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=low+(high-low)//2
        if arr[mid]>=x:
            ans=mid
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
        else:
            ans=n
            

    return ans
def upperBound(arr: [int], n: int, x: int) -> int:
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=low+(high-low)//2
        if arr[mid]>x:
            ans=mid
            high=mid-1
        else:
            low=mid+1

    return ans
def firstlast(arr,n,x):
    lb=lowerBound(arr,n,x)
  
    if ((lb==n) or arr[lb]!=x) :
        return -1,-1
    return lb,upperBound(arr,n,x)-1
print(firstlast(arr,n,x))
