from functools import cache
from typing import List


class Solution1:
    def countBits(self, n: int) -> List[int]:
        res = []

        @cache
        def count(num):
            if num == 0:
                return 0
            return 1 + count(num & (num - 1))

        for i in range(0, n + 1):
            res.append(count(i))

        return res


# not DP solution - complexity O(N logN)
class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(x):
            c = 0
            while x != 0:
                c += x % 2
                x //= 2
            return c

        r = []
        for i in range(n + 1):
            r.append(count(i))
        return r


if __name__ == "__main__":
    s = Solution1()
    assert s.countBits(2) == [0, 1, 1]
    assert s.countBits(5) == [0, 1, 1, 2, 1, 2]
