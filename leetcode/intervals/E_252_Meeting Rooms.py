# PREMIUM
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda e: e[0])
        for i in range(0, len(intervals) - 1):
            if self._overlap(intervals[i], intervals[i + 1]):
                return False
        return True

    def _overlap(self, a, b):
        return max(a[0], b[0]) < min(a[1], b[1])


if __name__ == '__main__':
    s = Solution()
    print(s.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
    print(s.canAttendMeetings([[7, 10], [2, 4]]))
    print(s.canAttendMeetings([]))
