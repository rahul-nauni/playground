# Find the sign of the product of all elements in nums
# Return 1 if product is positive, -1 if product is negative, 0 if product is 0
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Check if nums is empty
        if not nums or len(nums) == 0:
            return

        # Check if nums contains 0
        if any (num == 0 for num in nums):
            return 0
        
        negCount = 0 # Count number of negative numbers in nums
        
        for num in nums:
            if num < 0:
                negCount += 1
        
        if negCount % 2 == 0: # Even number of negative numbers
            return 1
        else:
            return -1

nums = [-1, -2, -3, -4, 3, 2, -1]    
s = Solution()
print(s.arraySign(nums))