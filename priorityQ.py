import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if len(nums1) == 0 or len(nums2) == 0 or k is None:
            print("Empty list")
            return exit(1)
        
        pairs = []
        pq = []

        for num1 in nums1:
            for num2 in nums2:
                sum = num1 + num2
                heapq.heappush(pq, [sum, num1, num2])

        for i in range(k):
            pairs.append(heapq.heappop(pq)[1:])

        return pairs

nums1 = []
nums2 = [2, 4, 6]
k = 3

s = Solution()
pairs = s.kSmallestPairs(nums1, nums2, k)
print(pairs)