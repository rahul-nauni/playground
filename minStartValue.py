def minStartValue(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return abs(nums[0]) + 1 if nums[0] < 1 else 1

        # Find minimum positive startvalue, initialise with 1
        startValue = 1
        
        for _ in range(len(nums)):
            sum = startValue
            for i in range(len(nums)):
                sum += nums[i]
                if sum < 1:
                    startValue += abs(sum) + 1
                    break
                   
        return startValue

nums = [1, -2, -3]
print(minStartValue(nums))