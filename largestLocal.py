from typing import List
from collections import deque
class Solution:
    # iterate through the values to get the max within the window
    # return the max
    
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # create maxLocal grid
        maxLocal = [[0 for i in range(len(grid[0]) - 2)] for j in range(len(grid) - 2)]
        
        # iterate through the grid
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                maxLocal[i][j] = max((grid[ii][jj] for ii in range(i, i + 3) for jj in range(j, j + 3)))
        return maxLocal
    
    def largestLocalOptimized(self, grid: List[List[int]]) -> List[List[int]]:
        def maxSlidingWindow(nums, k):
            q = deque() # monotonic queue to store the max values
            out = []
            for i, n in enumerate(nums):
                while q and nums[q[-1]] < n:
                    q.pop()
                q.append(i)
                if q[0] == i - k:
                    q.popleft()
                if i >= k - 1:
                    out.append(nums[q[0]])
            return out
        
        
        n = len(grid)
        maxLocal = [[0 for i in range(n - 2)] for j in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                subGrid = [grid[ii][jj] for ii in range(i, i + 3) for jj in range(j, j + 3)]

                maxVals = []
                for col in range(3):
                    maxVals.append(maxSlidingWindow(subGrid[col::3], 3))

                maxLocal[i][j] = max(maxVals[0][0], maxVals[1][0], maxVals[2][0])
        return maxLocal
                
grid = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,2,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1]
    ]
s = Solution()
print(s.largestLocal(grid))
          