"""
Given a sorted array arr[] and a value X, find the k closest elements to X in arr[]. 

Examples: 

Input: K = 4, X = 35
       arr[] = {12, 16, 22, 30, 35, 39, 42, 
               45, 48, 50, 53, 55, 56}
Output: 30 39 42 45
"""
from typing import List

def findX(arr: List[int], x: int, low: int, high: int) -> int:
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return findX(arr, x, low, mid - 1)
    else:
        return findX(arr, x, mid + 1, high)

def kClosest(arr: List[int], k: int, x: int) -> List[int]:
    
    x_index = findX(arr, x, 0, len(arr) - 1)
    if x_index == -1:
        return []
    
    result = []
    left = x_index - 1
    right = x_index + 1
    count = 0
    while left >= 0 and right < len(arr) and count < k:
        if x - arr[left] < arr[right] - x:
            result.append(arr[left])
            left -= 1
        else:
            result.append(arr[right])
            right += 1
        count += 1
    
    while left >= 0 and count < k:
        result.append(arr[left])
        left -= 1
        count += 1
    
    while right < len(arr) and count < k:
        result.append(arr[right])
        right += 1
        count += 1
    
    return result



arr = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
k = 4
x = 35
print(kClosest(arr, k, x))