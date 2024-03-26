from functools import cache


# state: dp[i] how many ways we can paint up to "i" posts with "k" colors
# base cases: one post can be painted in k ways, two posts can be painted k*k ways,
# as we are allowed to paint two consecutive posts in the same color
# recurrence relation: how many ways we can paint i-th post where 3 <= i <= k ?
# we can paint i-th post with different color, so we have k-1 possible colors = (k-1) * dp[i-1]
# or we can paint with the same color and is only 1 option -> 1 * dp[i-1] but we need to be sure that dp[i-1] != dp[i-2]
# so as above there is k-1 way to paint in different colors so 1 * (k-1) * dp[i-1]
class Solution1:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        dp = [0 for _ in range(n)]
        dp[0] = k
        dp[1] = k * k
        for i in range(2, n):
            dp[i] = (k - 1) * dp[i - 1] + (k - 1) * dp[i - 2]
        return dp[n - 1]


# top-down
class Solution:
    def numWays(self, n: int, k: int) -> int:
        @cache
        def dp(i):
            if i == 0:
                return k
            if i == 1:
                return k * k
            return (k - 1) * dp(i - 1) + (k - 1) * dp(i - 2)

        return dp(n - 1)


if __name__ == "__main__":
    s = Solution()
    assert s.numWays(3, 2) == 6
    assert s.numWays(2, 5) == 25
