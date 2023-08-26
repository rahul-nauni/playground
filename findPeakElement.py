from typing import List

def divide(nums, left, right):
        if left == right:
            return left
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            return divide(nums, left, mid)
        else:
            return divide(nums, mid + 1, right)


def findPeakElement(nums: List[int]):
    return divide(nums, 0, len(nums) - 1)

nums = [1,2,1,3,5,6,4]
print(findPeakElement(nums))