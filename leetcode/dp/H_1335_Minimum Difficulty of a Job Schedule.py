from functools import cache
from typing import List

# DP bottop-up
class Solution2:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        pass
        # TODO
        # more challenging to implement but perform better then top-down apprach


# recursion without slicing -> DP top down
# ACCEPTED but poor performance ~2000ms but should be in 400-700ms
# (using own caching for key = days_left:start was ~3000ms)
class Solution1:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def min_d(days_left: int, start: int) -> int:
            number_of_tasks = len(jobDifficulty) - start
            if days_left > number_of_tasks:
                return -1
            if days_left == number_of_tasks:
                return sum(jobDifficulty[start:])
            if days_left == 1:
                return max(jobDifficulty[start:])
            # we have to do at least 1 task each day, 'm' is maximum number of tasks we can do each day
            m = number_of_tasks - days_left + 1
            min_score = 1e9
            for i in range(m):
                end = start + i + 1
                score = max(jobDifficulty[start:end]) + min_d(days_left - 1, end)
                min_score = min(min_score, score)

            return min_score

        return min_d(d, 0)


# recursion TLE
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        if d == n:
            return sum(jobDifficulty)
        if d == 1:
            return max(jobDifficulty)
        m = n - d + 1
        min_score = 1e9
        for i in range(m):
            min_score = min(
                min_score,
                max(jobDifficulty[0:i + 1]) + self.minDifficulty(jobDifficulty[i + 1:], d - 1)
            )
        return min_score


if __name__ == "__main__":
    s = Solution1()
    assert s.minDifficulty([1, 1, 1], 3) == 3
    assert s.minDifficulty([1, 1, 1], 4) == -1
    assert s.minDifficulty([6, 5, 4, 3, 2, 1], 2) == 7
    assert s.minDifficulty([7, 1, 7, 1, 7, 1], 3) == 15
    assert s.minDifficulty([11, 111, 22, 222, 33, 333, 44, 444], 6) == 843
    assert s.minDifficulty([33, 333, 44, 444], 2) == 477
    assert s.minDifficulty(
        [380, 302, 102, 681, 863, 676, 243, 671, 651, 612, 162, 561, 394, 856, 601, 30, 6, 257, 921, 405, 716, 126, 158,
         476, 889, 699, 668, 930, 139, 164, 641, 801, 480, 756, 797, 915, 275, 709, 161, 358, 461, 938, 914, 557, 121,
         964, 315], 10) == 3807
