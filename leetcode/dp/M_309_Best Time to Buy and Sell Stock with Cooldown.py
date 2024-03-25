from functools import cache
from typing import List


# DP top down
# state:  i - number of day; state = { 2 - holding shares, 1 - having cooldown, 0 - can buy }
# base cases: no more days -> 0
# recurrence relation: maximize possible actions
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(day, state) -> int:
            if day >= len(prices):
                return 0

            # if cooldown period I can only move to the next day
            if state == 1:
                return dp(day + 1, 0)

            do_nothing = dp(day + 1, state)
            if state == 0:
                buy = -prices[day] + dp(day + 1, 2)
                return max(do_nothing, buy)
            else:
                sell = prices[day] + dp(day + 1, 1)
                return max(do_nothing, sell)

        return dp(0, 0)


if __name__ == '__main__':
    s = Solution()
    assert s.maxProfit([1, 2, 3, 0, 2]) == 3
    assert s.maxProfit([1]) == 0
    assert s.maxProfit([1, 2, 4]) == 3
