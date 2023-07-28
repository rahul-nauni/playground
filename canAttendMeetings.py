from typing import List
class Solution():
    def canAttendMeetings(intervals: List[List[int]]) -> bool:
        if intervals is None:
            return False
        
        if len(intervals) == 1:
            return True
        
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0][1] if intervals else None
        for i in intervals[1:]:
            if i[0] < prev:
                return False
            prev = i[1]
        return True

intervals = [[13,15],[1,13]]
print(Solution.canAttendMeetings(intervals))