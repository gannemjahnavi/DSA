
def maxSubarraySum(arr) :
    max_current = max_global = 0
    
    for num in arr:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    
    return max_global
