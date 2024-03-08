# PREMIUM
from typing import List
from heapq import heappush, heappop

# the issue is to find max number of overlapping interval
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        min_rooms = 0
        rooms_now = 0
        pq = []
        for interval in intervals:
            heappush(pq, (interval[0], 'start'))
            heappush(pq, (interval[1], 'end'))
        while pq:
            (_, start_or_end) = heappop(pq)
            if start_or_end == 'start':
                rooms_now += 1
                min_rooms = max(min_rooms, rooms_now)
            if start_or_end == 'end':
                rooms_now -= 1
        return min_rooms


if __name__ == '__main__':
    s = Solution()
    print(s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
    print(s.minMeetingRooms([[7, 10], [2, 4]]))
    print(s.minMeetingRooms([[0, 30]]))
