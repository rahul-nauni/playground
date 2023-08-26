import heapq

nums1 = [1, 3]
nums2 = [2]

heapq.heapify(nums1)
heapq.heapify(nums2)

q = heapq.merge(nums1, nums2)
q = list(q)
median = q[len(q) // 2]

print(median)

