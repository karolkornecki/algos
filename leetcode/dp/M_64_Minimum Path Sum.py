from functools import cache
from typing import List


# DP bottom-up
class Solution1:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                elif r == 0:
                    dp[r][c] = grid[r][c] + dp[r][c - 1]
                elif c == 0:
                    dp[r][c] = grid[r][c] + dp[r - 1][c]
                else:
                    dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])
        return dp[m - 1][n - 1]


# DP top-down
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        inf = int(1e9)
        m = len(grid)
        n = len(grid[0])

        @cache
        def dp(r, c) -> int:
            if r >= m or c >= n:
                return inf
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            return grid[r][c] + min(dp(r + 1, c), dp(r, c + 1))

        return dp(0, 0)


if __name__ == '__main__':
    s = Solution1()
    assert s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert s.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
