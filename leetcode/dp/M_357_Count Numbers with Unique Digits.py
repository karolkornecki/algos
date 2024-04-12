# this is math problem instead of DP ihmo
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        v = n - 1
        r = 1
        # variation without repetition
        while v != 0:
            r *= (10 - v)
            v -= 1
        return 9 * r + self.countNumbersWithUniqueDigits(n - 1)


if __name__ == "__main__":
    s = Solution()
    assert s.countNumbersWithUniqueDigits(2) == 91
    assert s.countNumbersWithUniqueDigits(3) == 739
