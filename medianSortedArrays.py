import heapq
from typing import List

def getMedian(arr: List[int]):
    return arr[len(arr) // 2]

# Space complexity: O(m) + O(n)
# Time complexity
def heapifySorted(nums1: List[int], nums2: List[int]) -> int:
    heapq.heapify(nums1)
    heapq.heapify(nums2)

    q = heapq.merge(nums1, nums2)
    q = list(q)
    median = getMedian(q)

    return median

def mergeSorted(nums1: List[int], nums2: List[int]):
    i, j = 0, 0
    merged = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    return merged

nums1 = [1, 3]
nums2 = [2]
merged_nums = mergeSorted(nums1, nums2)
print(f"Merged nums array: {merged_nums}")
median = getMedian(merged_nums)
print(f"Median: {median}")

