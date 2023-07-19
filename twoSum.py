import numpy as np
from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {} # value: index
        if(2 <= len(nums) <= 10**4):
            for i, n in enumerate(nums):
                diff = target - n
                if diff in map:
                    return [i, map[diff]]
                map[n] = i
            return

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)-1):
            j = i+1
            result = []
            while (j != len(nums)):
                if(nums[i] + nums[j]==target):
                    result.extend([i, j])
                    return result
                j += 1


nums = np.array([2,11,7,15])
target=9

result = twoSum(nums, target)
print(result)