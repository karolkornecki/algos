from functools import cache
from typing import List


# DP top-down
# state: dp(i,amount) -> number of ways we can change amount with a coins[i:]
# base cases: amount 0 we can change only 1 way without any coin, when we have no coins we cannot change so = 0
# recurrence relation: if coin is greater than amount we skip that coin
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(i, amount):
            if amount == 0:
                return 1
            if i == len(coins):
                return 0
            if amount < coins[i]:
                return dp(i + 1, amount)
            return dp(i, amount - coins[i]) + dp(i + 1, amount)

        return dp(0, amount)


if __name__ == '__main__':
    s = Solution()
    assert s.change(5, [1, 2, 5]) == 4
    assert s.change(3, [2]) == 0
    assert s.change(10, [10]) == 1
