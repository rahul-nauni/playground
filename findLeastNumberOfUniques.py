# Least Number of Unique Integers after K Removals
from typing import List
from collections import defaultdict, Counter
import heapq
"""def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
    # error checking
    if k == len(arr):
        return 0
    if k == 0:
        return len(set(arr))
    
    map = Counter(arr)

    common = map.most_common()

    count = 0
    for i in range(len(map)):
        while k > 0 and map[i][1] > 0:
            if k >= map[i][1]:
                k -= map[i][1]
                map[i] = (map[i][0], 0)
            else:
                map[i] = (map[i][0], map[i][1] - k)
                k = 0
                break
        
        if map[i][1] != 0:
            count += 1
        
    return count"""

def findLeastNumOfUniques(arr: List[int], k: int) -> int:
    map = Counter(arr)

    frequencies = sorted(map.values())

    for i, freq in enumerate(frequencies):
        if k >= freq:
            k -= freq
            frequencies[i] = 0
        else:
            frequencies[i] -= k
            k = 0
            break

    return sum(freq > 0 for freq in frequencies)


arr = [4, 3, 1, 1, 3, 3, 2]
k = 3
print(findLeastNumOfUniques(arr, k))
#print(findLeastNumOfUniqueInts(arr, k))
