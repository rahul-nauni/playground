from typing import List

def binarySearch(arr: List[int], target: int, low: int, high: int) -> bool:
    while low <= high:
        if low == high:
            return arr[low] == target
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False
    

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])

    # edege case
    if target < matrix[0][0] or target > matrix[rows - 1][cols - 1]:
        return False
    
    for i in range(rows):
        if target >= matrix[i][0] and target <= matrix[i][-1]:
            return binarySearch(matrix[i], target, 0, cols - 1)
    
matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]
target = 13
print(searchMatrix(matrix, target))