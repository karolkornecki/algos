# optimized tabular solution to store only two values
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev_prev = 1
        prev = 2
        for i in range(3, n + 1):
            current = prev + prev_prev
            prev_prev = prev
            prev = current
        return prev


# solution (tabular) - DP - bottom up approach
class Solution3:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [-1 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# recursive solution (memoization) - DP - top down approach
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [-1 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        return self.climb(n, dp)

    def climb(self, n, dp) -> int:
        if dp[n] != - 1:
            return dp[n]
        dp[n] = self.climb(n - 1, dp) + self.climb(n - 2, dp)
        return dp[n]


# recursive solution
# time limit exceeded
class Solution1:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(44))
