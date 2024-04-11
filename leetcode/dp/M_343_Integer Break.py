from functools import cache


class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dp(left):
            if left < 0:
                return 0
            if left == 0:
                return 1
            val = 1
            for i in range(1, n + 1):
                val = max(val, i * dp(left - i))
            return val

        if n <= 3:
            return n - 1
        
        return dp(n)


if __name__ == "__main__":
    s = Solution()
    assert s.integerBreak(2) == 1
    assert s.integerBreak(3) == 2
    assert s.integerBreak(5) == 6
    assert s.integerBreak(10) == 36
