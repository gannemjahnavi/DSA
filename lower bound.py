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
