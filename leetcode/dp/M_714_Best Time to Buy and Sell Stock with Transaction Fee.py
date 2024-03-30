from functools import cache
from typing import List


# state: dp(i, holding) -> max profit up to i-th day,
# holding = 1 - holding shares at the day i-th, 0 means not holding and to be allowed to buy
# base cases: no more days -> 0
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(i, holding) -> int:
            if i == len(prices):
                return 0
            if holding == 1:
                return max(prices[i] - fee + dp(i + 1, 0), dp(i + 1, holding))
            else:
                return max(-prices[i] + dp(i + 1, 1), dp(i + 1, holding))

        return dp(0, 0)


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([1, 3, 2, 8, 4, 9], 2) == 8
    assert s.maxProfit([1, 3, 7, 5, 10, 3], 3) == 6
