from functools import cache
from typing import List


# state = dp[current_day, transactions_left, holding_stock_flg]
# base cases: no more transactions ->, no more days -> 0
# recurrence relation: max of two actions: do nothing or (buy stock (if holding now) or sell stock (if not holding now))
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
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

        return dp(0, k, 0)


if __name__ == '__main__':
    s = Solution()

    assert s.maxProfit(2, [2, 4, 1]) == 2
    assert s.maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7
