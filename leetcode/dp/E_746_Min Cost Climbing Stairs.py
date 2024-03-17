from typing import List

# DP bottom up
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = dict()
        dp[0] = cost[0]
        dp[1] = cost[1]
        if n == 2:
            return min(dp[0], dp[1])
        for i in range(2, n):
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        return min(dp[n - 1], dp[n - 2])


if __name__ == "__main__":
    s = Solution()
    assert s.minCostClimbingStairs([10, 15, 20]) == 15
    assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
