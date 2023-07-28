from typing import List

def selectionSort_asc(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        min = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < min: # find min
                min = arr[j] # update min
                arr[i], arr[j] = arr[j], arr[i] # swap with min
    return arr

def selectionSort_desc(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        max = arr[i]
        for j in range(i+1, n):
            if arr[j] > max:
                max = arr[j]
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [5, 3, 2, 1, 4]
print(selectionSort_asc(arr))
