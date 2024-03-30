from functools import cache
from typing import List


# DP top-down
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        inf = int(1e9)
        n = len(matrix)

        @cache
        def dp(r, c) -> int:
            if r > n - 1 or c < 0 or c > n - 1:
                return inf
            if r == n - 1:
                return matrix[r][c]
            return matrix[r][c] + min([dp(r + 1, c - 1), dp(r + 1, c), dp(r + 1, c + 1)])

        min_falling = inf
        for i in range(n):
            min_falling = min(min_falling, dp(0, i))
        return min_falling


if __name__ == "__main__":
    s = Solution()
    assert s.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
    assert s.minFallingPathSum([[-19, 57], [-40, -5]]) == -59
