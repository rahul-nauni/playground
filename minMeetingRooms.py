from typing import List
import heapq
class Solution:
    def check_room(self, start, rooms):
        if rooms[0] <= start:
            heapq.heappop(rooms)

    def allocate(self, end, rooms):
        heapq.heappush(rooms, end)

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1
        
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Initialize heap
        rooms = []
        heapq.heappush(rooms, intervals[0][1]) # end time of first interval

        for i in intervals[1:]:
            # check if we can reuse a room
            self.check_room(i[0], rooms)
            # allocate a new room
            self.allocate(i[1], rooms)

        return len(rooms)
"""
test case 1:
intervals = [[0,30],[5,10],[15,20]]
output = 2
test case 2:
intervals = [[7,10],[2,4]]
output = 1
test case 3:
intervals = [[5,8],[6,8]]
output = 2
test case 4:
intervals = [[1,5],[8,9]]
output = 1
"""

intervals = [[7,10],[2,4]]
print(Solution().minMeetingRooms(intervals))