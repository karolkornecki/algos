from functools import cache
from typing import List

# DP top-down -> look at -> 188. Best Time to Buy and Sell Stock IV
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(day, transactions_left, holding) -> int:
            if transactions_left == 0 or day >= len(prices):
                return 0
            if holding == 1:
                # I can sell stock or do nothing
                return max(
                    dp(day + 1, transactions_left, holding),
                    prices[day] + dp(day + 1, transactions_left - 1, 0)
                )
            else:
                # I can buy stock or do nothing
                return max(
                    dp(day + 1, transactions_left, holding),
                    -prices[day] + dp(day + 1, transactions_left, 1)
                )

        return dp(0, 2, 0)
