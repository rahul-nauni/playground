from typing import List

class Solution:
    def merge(self, intervals: List[int]) -> List[int]:
        if len(intervals) == 1:
            return intervals
        
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = []

        for i in range(len(intervals)):
            if i == 0:
                merged.append(intervals[i])
            else:
                if intervals[i][0] > merged[-1][1]: # non-overlapping
                    merged.append(intervals[i])
                else:
                    merged[-1][0] = min(merged[-1][0], intervals[i][0])
                    merged[-1][1] = max(merged[-1][1], intervals[i][1])
                     
        return merged
    
s = Solution()
intervals = [[1, 4], [0, 0]]
print(s.merge(intervals))