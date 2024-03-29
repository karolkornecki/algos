from functools import cache
from typing import List

# DP top-down
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        @cache
        def dp(r, c) -> int:
            if r >= rows or c >= cols or obstacleGrid[r][c] == 1:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            return dp(r, c + 1) + dp(r + 1, c)

        return dp(0, 0)


if __name__ == '__main__':
    s = Solution()
    assert s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert s.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1
