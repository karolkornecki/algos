from functools import cache
from typing import List


# DP - top-down
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(t):
            if t == 0:
                return 1
            if t < 0:
                return 0
            ways = 0
            for n in nums:
                ways += dp(t - n)
            return ways

        return dp(target)
