from typing import List
def moveZeroes(nums: List[int]) -> None:
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[pos] = nums[pos], nums[i] # swap
            pos += 1
    print(nums)

nums = [0]
moveZeroes(nums)
