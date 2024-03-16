from typing import List


class Solution:
    def minTaps(self, n: int, r: List[int]) -> int:
        ranges = [(i - r[i], i + r[i]) for i in range(0, n + 1)]
        ranges.sort()
        point = 0
        intervals = []
        while point < n:
            interval = find_interval(ranges, point)
            if interval is None or interval[1] - interval[0] == 0 or (len(intervals) > 0 and interval == intervals[-1]):
                return -1
            intervals.append(interval)
            point = interval[1]
        return len(intervals)


# TODO this search could be simplified
def find_interval(ranges, point):
    i = 0
    interval = None
    while i < len(ranges):
        begin, end = ranges[i]
        if begin <= point <= end:
            if interval is None or interval[1] - point < end - point:
                interval = (begin, end)
        if begin > point:  # stop scanning
            break
        i += 1
    return interval


if __name__ == '__main__':
    s = Solution()
    # assert s.minTaps(5, [3, 4, 1, 1, 0, 0]) == 1
    # assert s.minTaps(3, [0, 0, 0, 0]) == -1
    # assert s.minTaps(8, [4, 0, 0, 0, 0, 0, 0, 0, 4]) == 2
    assert s.minTaps(5, [3, 0, 1, 1, 0, 0]) == -1
    assert s.minTaps(5, [1, 1, 1, 1, 1, 1]) == 3
