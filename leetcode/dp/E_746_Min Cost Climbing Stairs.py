from functools import cache
from typing import List


# DP bottom up - space optimization
class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        two_back = cost[0]
        one_back = cost[1]
        if n == 2:
            return min(one_back, two_back)
        for i in range(2, n):
            current = min(one_back, two_back) + cost[i]
            two_back = one_back
            one_back = current
        return min(one_back, two_back)


# DP bottom up
class Solution1:
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


# DP top down
# target: reach step len(cost) - 1 or len(cost) - 2 with cheapest cost
# state: dp[i] - cost of reaching step i
# relation: cost[i] + min(dp[i-1], dp[i-2])
# base: dp[0] = cost[0], dp[1] = cost[1]
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        @cache
        def dp(i):
            if i == 0 or i == 1:
                return cost[i]
            return cost[i] + min(dp(i - 1), dp(i - 2))

        return min(dp(n - 1), dp(n - 2))


if __name__ == "__main__":
    s = Solution2()
    assert s.minCostClimbingStairs([10, 15, 20]) == 15
    assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
