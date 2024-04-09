from functools import cache


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def dp(a, b) -> int:
            if a >= b:
                return 0
            res = int(1e9)
            for i in range(a, b + 1):
                res = min(res, i + max(dp(a, i - 1), dp(i + 1, b)))
            return res

        return dp(1, n)


if __name__ == "__main__":
    s = Solution()
    assert s.getMoneyAmount(1) == 0
    assert s.getMoneyAmount(2) == 1
    assert s.getMoneyAmount(3) == 2
    assert s.getMoneyAmount(10) == 16
    assert s.getMoneyAmount(12) == 21
