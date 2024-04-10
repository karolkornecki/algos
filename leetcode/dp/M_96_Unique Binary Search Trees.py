from functools import cache


# DP top-down
class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def dp(left: int) -> int:
            if left == 0:
                return 1
            if left <= 2:
                return left
            num = 0
            for i in range(1, left + 1):
                num += dp(i - 1) * dp(left - i)
            return num

        return dp(n)


if __name__ == "__main__":
    s = Solution()
    assert s.numTrees(1) == 1
    assert s.numTrees(2) == 2
    assert s.numTrees(3) == 5
    assert s.numTrees(4) == 14
    assert s.numTrees(5) == 42
    assert s.numTrees(6) == 132
    assert s.numTrees(7) == 429
