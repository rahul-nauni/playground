from typing import List
import collections
# count number of distinct elements in contiguous subarrays
def countDistinctCategories(arr: List[int]):
    if len(arr) == 1:
        return 1
    # dont use subarrays and save space complexity
    start = 0
    end = 0
    count = 0

    while end < len(arr):
        if arr[end] not in arr[start:end]:
            count += 1
        else:
            start += 1
        end += 1
    return count
        
print(countDistinctCategories([1, 2, 1]))