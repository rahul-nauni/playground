from typing import List

def lengthOfLIS(arr: List[int]):
    if not arr:
        return 0
    
    LIS = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                LIS[j] = max(LIS[i] + 1, LIS[j])
            
    return max(LIS)

arr = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(arr))