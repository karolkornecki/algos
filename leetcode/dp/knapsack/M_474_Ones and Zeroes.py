from functools import cache
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dp(i, zeros_left, ones_left):
            if i >= len(strs):
                return 0

            zeros = strs[i].count('0')
            ones = strs[i].count('1')

            # if current string cannot be taken due to maximum 0 or 1 used then we just skip it
            if zeros_left - zeros < 0 or ones_left - ones < 0:
                return dp(i + 1, zeros_left, ones_left)
            else:
                # max of two actions: taking current string or not taking it
                return max(
                    1 + dp(i + 1, zeros_left - zeros, ones_left - ones),
                    dp(i + 1, zeros_left, ones_left)
                )

        return dp(0, m, n)


if __name__ == "__main__":
    s = Solution()
    assert s.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) == 4
