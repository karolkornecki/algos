from functools import cache
from typing import List


# DP top-down
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, holding) -> int:
            if i == len(prices):
                return 0
            if holding == 1:
                return max(prices[i] + dp(i + 1, 0), dp(i + 1, holding))
            else:
                return max(-prices[i] + dp(i + 1, 1), dp(i + 1, holding))

        return dp(0, 0)
