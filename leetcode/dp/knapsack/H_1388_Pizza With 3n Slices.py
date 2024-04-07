from functools import cache
from typing import List


# if we have circular array where we cannot take adjacent element,
# when we take first element we cannot take last and we can take last only if we don't take first
# so it is easy to split this problem into two parts and solve them separately then take max of two these results
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        class DP:
            def __init__(self, s):
                self.slices = s

            @cache
            def dp(self, i, left):
                if i >= len(self.slices) or left == 0:
                    return 0

                return max(
                    self.slices[i] + self.dp(i + 2, left - 1),
                    self.dp(i + 1, left)
                )

        n = len(slices)
        return max(
            # array with first element, it can be taken so the last element is eliminated
            DP(slices[0:n - 1]).dp(0, n // 3),
            # array without first element thus the last element can be taken
            DP(slices[1:n]).dp(0, n // 3)
        )


if __name__ == "__main__":
    s = Solution()
    assert s.maxSizeSlices([1, 2, 3, 4, 5, 6]) == 10
    assert s.maxSizeSlices([8, 9, 8, 6, 1, 1]) == 16
    assert s.maxSizeSlices([9, 5, 1, 7, 8, 4, 4, 5, 5, 8, 7, 7]) == 30
