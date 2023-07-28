def in_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1] , nums[j] = nums[j], nums[j-1]
            j -= 1
    return nums

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

def sortColors(nums):
    low = 0
    high = len(nums) - 1
    mid = 0
    while mid <= high:
        if nums[mid] == 0:
            #nums[i], nums[low] = nums[low], nums[i]
            swap(nums, mid, low)
            low += 1
            mid += 1
        elif nums[mid] == 2:
            #nums[i], nums[high] = nums[high], nums[i]
            swap(nums, mid, high)
            high -= 1
        else:
            mid += 1
    return nums

nums = [2, 0, 2, 1, 1, 0, 0, 1, 2, 0, 1, 0, 2, 1]
sorted_nums = sortColors(nums)
print(sorted_nums)