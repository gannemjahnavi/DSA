from typing import *

def longestSuccessiveElements(a : List[int]) -> int:
    n=len(a)
    c=1
    longest=1
    a.sort()
    for i in range(0,n):
        if a[i]==a[i-1]:
            continue
        elif a[i]==a[i-1]+1:
            c+=1
        else:
            longest=max(longest,c)
            c=1
    return max(longest,c)
