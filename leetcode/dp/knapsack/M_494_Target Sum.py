from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, s):
            # end is reached: all elements are used and target sum is reached as well
            if s == target and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            return dp(i + 1, s + nums[i]) + dp(i + 1, s - nums[i])

        return dp(0, 0)


if __name__ == "__main__":
    s = Solution()
    assert s.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
    assert s.findTargetSumWays([1], 1) == 1
