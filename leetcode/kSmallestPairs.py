"""You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums."""

import heapq
import time

def kSmallestPairs(nums1, nums2, k):
    heap = [] # min heap
    pairs = []  # list of pairs with smallest sum
        
    # Edge cases
    if len(nums1) == 0 or len(nums2) == 0 or k is None:
        return []
    
    else:
        # Initialize heap with first k pairs with smallest sum
        for i in range(min(k, len(nums1))):
            heap.append([nums1[i] + nums2[0], i, 0])
        heapq.heapify(heap)
        
        # loop until k pairs are found or heap is empty
        while k > 0 and heap:
            sum, i, j = heapq.heappop(heap)
            
            # check if we have exhausted nums1 or nums2
            if i >= len(nums1) or j >= len(nums2):
                continue

            # add current pair to result
            pairs.append([sum, nums1[i], nums2[j]][1:])

            # consider next pair with nums[i] and nums[j + 1]
            if j + 1 < len(nums2):
                heapq.heappush(heap, [nums1[i] + nums2[j + 1], i, j + 1])

            # consider next pair with nums[i + 1] and nums[j]
            if j == 0 and i + 1 < len(nums1) and nums1[i+1] + nums2[0] < sum:
                heapq.heappush(heap, [nums1[i + 1] + nums2[j], i + 1, j])
                
            k -= 1
        
    return pairs

"""start = time.time()
pairs = kSmallestPairs([1, 2], [3], 3)
end = time.time()
print(pairs)"""

#----------------------------------------------------------------------------------------------------------
"""
Algorithm:
We initialize the heap with the first element of nums1 and nums2 because they are sorted in ascending order
so the first element of nums1 and nums2 will always be the smallest pair
"""
nums1 = [1, 7, 6]
nums2 = [2, 4, 11]
k = 3

heap = []   # min heap

def push(i, j):
    if i < len(nums1) and j < len(nums2):
        heapq.heappush(heap, (nums1[i] + nums2[j], i, j))
i, j = 0, 0
push(i, j)

pairs = []  # list of pairs with smallest sum
while heap and len(pairs) < k:
    #_,i, j = heapq.heappushpop(heap, (nums1[i] + nums2[j+1], i, j+1))
    _, i, j = heapq.heappop(heap)
    pairs.append([nums1[i], nums2[j]])
    push(i, j + 1)
    if j == 0:
        push(i + 1, j)
    print(f'current index: {i, j}')
    print(f'current pair: {pairs[-1]}')

print(pairs)