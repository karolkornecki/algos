from functools import cache
from typing import List

# DP top-down - memory limit exceeded - if this trick -> min(minProfit, p + profit[i]) is missed
# The solution is to reduce the problem to 2D and bottom up approach
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7

        # i = current considered crime
        # p = profit so far
        # left = members left to be able to participate in the crime
        @cache
        def dp(i, p, left) -> int:
            if left < 0:
                return 0

            if i >= len(profit):
                if p >= minProfit:
                    return 1
                return 0

            # min(minProfit, p + profit[i]) this is used to avoid unnecessary recursive call and leverage caching
            # since we reach minProfit adding more profit does not change the situation
            # because condition is already fulfilled
            return dp(i + 1, p, left) + \
                   dp(i + 1, min(minProfit, p + profit[i]), left - group[i])

        return dp(0, 0, n) % mod


if __name__ == "__main__":
    s = Solution()
    assert s.profitableSchemes(5, 3, [2, 2], [2, 3]) == 2
    assert s.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]) == 7
    assert s.profitableSchemes(100, 100,
                               [2, 5, 36, 2, 5, 5, 14, 1, 12, 1, 14, 15, 1, 1, 27, 13, 6, 59, 6, 1, 7, 1, 2, 7, 6, 1, 6,
                                1, 3, 1, 2, 11, 3, 39, 21, 20, 1, 27, 26, 22, 11, 17, 3, 2, 4, 5, 6, 18, 4, 14, 1, 1, 1,
                                3, 12, 9, 7, 3, 16, 5, 1, 19, 4, 8, 6, 3, 2, 7, 3, 5, 12, 6, 15, 2, 11, 12, 12, 21, 5,
                                1, 13, 2, 29, 38, 10, 17, 1, 14, 1, 62, 7, 1, 14, 6, 4, 16, 6, 4, 32, 48],
                               [21, 4, 9, 12, 5, 8, 8, 5, 14, 18, 43, 24, 3, 0, 20, 9, 0, 24, 4, 0, 0, 7, 3, 13, 6, 5,
                                19, 6, 3, 14, 9, 5, 5, 6, 4, 7, 20, 2, 13, 0, 1, 19, 4, 0, 11, 9, 6, 15, 15, 7, 1, 25,
                                17, 4, 4, 3, 43, 46, 82, 15, 12, 4, 1, 8, 24, 3, 15, 3, 6, 3, 0, 8, 10, 8, 10, 1, 21,
                                13, 10, 28, 11, 27, 17, 1, 13, 10, 11, 4, 36, 26, 4, 2, 2, 2, 10, 0, 11, 5, 22,
                                6]) == 692206787
