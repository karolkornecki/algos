from functools import cache

import math

# it does not perform well but it's ACCEPTED
class Solution:
    def numSquares(self, n: int) -> int:
        inf = int(1e9)

        @cache
        def dp(c):
            if c < 0:
                return inf
            if c == 0:
                return 0
            num = inf
            for i in range(int(math.floor(math.sqrt(c))), 0, -1):
                num = min(num, 1 + dp(c - int(math.pow(i, 2))))
            return num

        return dp(n)


if __name__ == "__main__":
    s = Solution()
    assert s.numSquares(12) == 3
    assert s.numSquares(13) == 2
