from functools import cache
from typing import List


# DP top-down (recursive + python caching)
# accepted
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def coin(money: int) -> int:
            if money == 0:
                return 0
            min_coins = 1e9
            for i in range(len(coins)):
                if money - coins[i] >= 0:
                    n = 1 + coin(money - coins[i])
                    min_coins = min(min_coins, n)
            return min_coins

        res = coin(amount)
        return res if res != 1e9 else -1


if __name__ == '__main__':
    s = Solution()
    assert s.coinChange([2, 1, 5], 11) == 3
    assert s.coinChange([2], 3) == -1
    assert s.coinChange([1], 0) == 0
    assert s.coinChange([186, 419, 83, 408], 6249) == 20
