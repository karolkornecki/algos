from functools import cache


# DP top-down
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(r, c) -> int:
            if r >= m or c >= n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            return dp(r + 1, c) + dp(r, c + 1)

        return dp(0, 0)


if __name__ == '__main__':
    s = Solution()
    assert s.uniquePaths(3, 7) == 28
    assert s.uniquePaths(3, 2) == 3
    assert s.uniquePaths(1, 1) == 1
